// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {
    // This 'using A for B;' can be used to attach library functions(A) to any type(B) within a contract.
    using SafeMathChainlink for uint256;

    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;

    /*
        Constructor - this function runs when a contract is deployed.
    */
    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        // in this case, the owner is the person who deployed the contract.
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 minUSD = 50 * (10**18); // Minimum of $50 in wei.
        // if(msg.value < minUSD) {
        //     revert?
        // }

        // Solidity style would use 'require' which is a check before a function executes.
        require(
            getConversionRate(msg.value) >= minUSD,
            "You need to spend more ETH!"
        );
        // 'revert' unspent gas and funds are returned to the user.

        /*
            msg.sender & msg.value are predefined values in every contract.
            1. msg.sender - the sender of funds
            2. msg.value - the amount of funds
        */
        addressToAmountFunded[msg.sender] += msg.value;

        // Oracles are used to connect contracts to "outside world data".
        // Find ETH -> USD conversion.

        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        // Addresss from https://docs.chain.link/docs/ethereum-addresses/ Rinkeby: ETH->USD
        // AggregatorV3Interface priceFeed = AggregatorV3Interface(
        //     0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        // );

        // Using priceFeed defined in the constructor from deploy.py. Otherwise we can't use this library in local Ganache net.
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        // AggregatorV3Interface priceFeed = AggregatorV3Interface(
        //     0x8A753747A1Fa494EC906cE90E9f37563A8AF630e
        // );
        // This returns a Tuple of 5 values.
        // priceFeed.latestRoundData()

        // (
        //     uint80 roundId,
        //     int256 answer,
        //     uint256 startedAt,
        //     uint256 updatedAt,
        //     uint80 answeredInRound
        // ) = priceFeed.latestRoundData();

        // To fix unused variables warning, use blanks.
        (, int256 answer, , , ) = priceFeed.latestRoundData();

        /* 
            returns 320120819731 which is 3201.20819731
            
            Reason being that Solidity doesn't work with decimals,
            and these values should be seen as having 8 decimals places
        */
        // return uint256(answer);

        // Returns the answer in wei (18 decimal places).
        return uint256(answer * 10000000000);
    }

    // 100000000 = 1 gwei
    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethPrice = getPrice();

        // 320801998386.000000000000000000
        // uint256 ethAmountInUSD = (ethPrice * ethAmount);

        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        // 3208019983860
        // add 0s to get 18 decimal places
        // 0.000003208019983860

        // 0.000003208019983860 * 1 Gwei = USD price.
        return ethAmountInUSD;
    }

    function getEntranceFee() public view returns (uint256) {
        // minimum USD
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minimumUSD * precision) / price;
    }

    // Modifiers are used to change the behavior of a function in a declaritive way.
    modifier onlyOwner() {
        require(msg.sender == owner);
        // this underscore means 'rest of the function code.'
        _;
    }

    // function withdraw() payable public {
    //     // Add a require to make sure only the contract owner/admin can withdraw funds.
    //     require(msg.sender == owner);

    //     // tansfer is a function that can be called on any address to send ETH from one address to another.
    //     // 'this' refers to the current contract.
    //     // 'balance' is the current value of funds at that address.
    //     msg.sender.transfer(address(this).balance);
    // }

    // withdraw function using a modifier.
    function withdraw() public payable onlyOwner {
        msg.sender.transfer(address(this).balance);

        // Reset all the funder's fund value to 0.
        for (uint256 i = 0; i < funders.length; i++) {
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }
        // reset the funders array to a blank array.
        funders = new address[](0);
    }
}
