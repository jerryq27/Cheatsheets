// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/* Should be able to do:

1. Stake tokens
2. Unstake tokens
3. Issue reward tokens to users
4. Add allowed tokens
5. Get ETH value of tokens
*/
contract TokenFarm is Ownable {
    // List of allowed tokens.
    address[] public allowedTokens;
    // List of stakers in platform (also needed cause you can't loop through a map)
    address[] public stakers;
    // Mapping allowed token's address -> staker's address -> amount staked
    mapping(address => mapping(address => uint256)) public stakingBalance;
    // Mapping to keep track of how many unique tokens the user has staked.
    mapping(address => uint256) public uniqueTokensStaked;
    // Mapping for unique tokens to their Chainlink price feeds.
    mapping(address => address) public tokenPriceFeedMapping;
    IERC20 public dappToken;

    constructor(address _dappTokenAddress) public {
        // DAPP token we defined.
        dappToken = IERC20(_dappTokenAddress);
    }

    function setPriceFeedContract(address _token, address _priceFeed)
        public
        onlyOwner
    {
        tokenPriceFeedMapping[_token] = _priceFeed;
    }

    /** Function 1 - Stakes tokens sent in by users.
        _amount - amount of tokens to stake
        _token - the address of the ERC-20 token being staked
     */
    function stakeTokens(uint256 _amount, address _token) public {
        require(_amount > 0, "Amount must be more than 0");
        require(tokenIsAllowed(_token), "Token is currently not allowed");

        // We need the contract for the token (or an interface defined), or we can use OpenZeppelin's IERC20.sol
        // We transfer the tokens from the sender to this contract's address.
        // Using transferFrom() instead of transfer(), the former is from user to user, the latter is from the contract that owns the token.
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        updateUniqueTokensStaked(msg.sender, _token);
        stakingBalance[_token][msg.sender] =
            stakingBalance[_token][msg.sender] +
            _amount;

        // Check if the amount of unique tokens is 1, if so it's the first token for this user
        // So update the stakers list.
        if (uniqueTokensStaked[msg.sender] == 1) {
            stakers.push(msg.sender);
        }
    }

    /** Util function to update how many unique tokens a user is staking.
        _user - the address of the user staking
        _token - the address of the token being staked
    */
    function updateUniqueTokensStaked(address _user, address _token) internal {
        if (stakingBalance[_token][_user] <= 0) {
            uniqueTokensStaked[_user] = uniqueTokensStaked[_user] + 1;
        }
    }

    /** Function 2 - Unstakes tokens sent in by users.
        _token - the address of the ERC-20 token being staked
     */
    function unstakeTokens(address _token) public {
        uint256 balance = stakingBalance[_token][msg.sender];
        require(balance > 0, "Staking balance cannot be 0.");
        IERC20(_token).transfer(msg.sender, balance);
        stakingBalance[_token][msg.sender] = 0;
        // Counters Re-entrancy attack?
        uniqueTokensStaked[msg.sender] = uniqueTokensStaked[msg.sender] - 1;
    }

    /** Function 3 - Issues tokens to all stakers based on the value of tokens staked.
     */
    function issueTokens() public onlyOwner {
        for (uint256 i = 0; i < stakers.length; i++) {
            address recipient = stakers[i];
            // Send them a DAPP token reward based on total value staked.
            uint256 userTotalValue = getUserTotalValue(recipient);
            // Here we can use transfer() instead of transferFrom() since this contract holds the DAPP tokens.
            dappToken.transfer(recipient, userTotalValue);
        }
    }

    /** Util function that grabs the value of all unique tokens the user has staked.
        _user - the address of the user staking
        _token - the address of the token being staked
    */
    function getUserTotalValue(address _user) public view returns (uint256) {
        uint256 totalValue = 0;
        require(uniqueTokensStaked[_user] > 0, "No tokens staked!");
        for (uint256 i = 0; i < allowedTokens.length; i++) {
            totalValue =
                totalValue +
                getUserSingleTokenValue(_user, allowedTokens[i]);
        }
        return totalValue;
    }

    /** Util function that grabs the value of one unique token the user has staked.
        _user - the address of the user staking
        _token - the address of the token being staked
    */
    function getUserSingleTokenValue(address _user, address _token)
        public
        view
        returns (uint256)
    {
        if (uniqueTokensStaked[_user] <= 0) {
            return 0;
        }

        (uint256 price, uint256 decimals) = getTokenValue(_token);
        // Price of token * stakingBalance[_token][_user]
        // 10 ETH, ETH-->USD=100, 10 * 100 = 1000
        return ((stakingBalance[_token][_user] * price) / (10**decimals));
    }

    /** Util function that grabs the value of one unique token from Chainlink.
        _token - the address of the token being staked
    */
    function getTokenValue(address _token)
        public
        view
        returns (uint256, uint256)
    {
        // Price feed address
        address priceFeedAddress = tokenPriceFeedMapping[_token];
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            priceFeedAddress
        );

        (, int256 price, , , ) = priceFeed.latestRoundData();
        uint8 decimals = priceFeed.decimals();

        return (uint256(price), uint256(decimals));
    }

    /** Util function that only the owner can use. onlyOwner is from OpenZeppelin's Ownable.sol contract.
        _token - the address of the ERC-20 token being staked 
    */
    function addAllowedTokens(address _token) public onlyOwner {
        allowedTokens.push(_token);
    }

    /** Function 4 - Checks if token is allowed to be staked.
        _token - the address of the ERC-20 token being staked
        return: Whether or not that token is allowed to be staked in this Dapp.
     */
    function tokenIsAllowed(address _token) public returns (bool) {
        for (uint256 i = 0; i < allowedTokens.length; i++) {
            if (allowedTokens[i] == _token) {
                return true;
            }
        }
        return false;
    }
}
