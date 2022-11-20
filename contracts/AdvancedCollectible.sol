//SPDX Licence Identifier:MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokencounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum Breed {
        PUG,
        SHIBA_INU,
        ST_BERNARD
    }
    mapping(uint256 => Breed) public tokenIdtoBreed;
    mapping(bytes32 => address) public RequestidtoSender;
    event RequestedCollectible(bytes32 indexed requestid, address requester);
    event breedAssigned(uint256 indexed tokenid, Breed breed);

    constructor(
        address _vrfconsumer,
        address _linktoken,
        bytes32 _keyhash,
        uint256 _fee
    ) public VRFConsumerBase(_vrfconsumer, _linktoken) ERC721("DOGGIE", "DOG") {
        tokencounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public payable returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        RequestidtoSender[requestId] = msg.sender;
        emit RequestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Breed breed = Breed(randomNumber % 3);
        uint256 newTokenId = tokencounter;
        tokenIdtoBreed[newTokenId] = breed;
        emit breedAssigned(newTokenId, breed);
        address owner = RequestidtoSender[requestId];
        _safeMint(owner, newTokenId);
        tokencounter = tokencounter + 1;
    }

    function setTokenURI(uint256 tokenid, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenid),
            "ERC721: Caller is not Owner"
        );
        _setTokenURI(tokenid, _tokenURI);
    }
}
