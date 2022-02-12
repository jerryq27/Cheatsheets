// SPDX License-Identifier: MIT

// NFT Contract
// Where the tokenURI can be one of 3 different dogs.
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvanceCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum Breed {
        PUG,
        SHIBA_INU,
        ST_BERNARD
    }
    mapping(uint256 => Breed) public tokenIdToBreed;
    mapping(bytes32 => address) public requestIdToSender;

    //***** It's best practice to emit events when updating mappings.
    // indexed keyword makes it easier to search for this event.
    event RequestedCollectible(bytes32 indexed requestId, address requester);
    event BreedAssigned(uint256 indexed tokenId, Breed breed);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken) // For requesting randomness.
        ERC721("Dogie", "DOG")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        // Calling msg.sender here is ok.
        requestIdToSender[requestId] = msg.sender;
        emit RequestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Breed breed = Breed(randomNumber % 3); // Grabs a random breed.
        uint256 newTokenId = tokenCounter;
        tokenIdToBreed[newTokenId] = breed;
        emit BreedAssigned(newTokenId, breed);
        // Using msg.sender would be the VRFCoordinator contract here. Have to use another way to get the address creating this NFT.
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        // Need a tokenURI for each breed: pug, shiba inu, st bernard
        // Using OpenZeppelin funcitons to determine the sender is the one modifying the tokenURI.
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not sender or approved."
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
