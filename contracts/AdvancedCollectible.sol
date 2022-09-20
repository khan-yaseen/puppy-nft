// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 keyhash;
    uint256 fee;
    enum Breed {
        PUG,
        SHIBA_INU,
        ST_BERNARD
    }
    // Emit event whenever you update mappings
    mapping(uint256 => Breed) public tokenIdToBreed;
    mapping(bytes32 => address) public requestIdToSender;
    event requestedCollectible(bytes32 indexed requestId, address requester); // "indexed" keyword just makes it easier to search for this event
    event breedAssigned(uint256 indexed tokenId, Breed breed);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("Doggie", "DOG")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public returns (uint256) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Breed breed = Breed(randomNumber % 3);
        uint256 newTokenId = tokenCounter;
        tokenIdToBreed[newTokenId] = breed;
        emit breedAssigned(newTokenId, breed);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        // _setTokenURI(tokenId, _tokenURI); TODO: Find a way to set the tokenURI in the fulfillRandomness function
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        // 3 tokenURIs for pug, shiba inu, st bernard
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not token owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
