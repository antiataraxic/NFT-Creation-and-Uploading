//SPDX Licence Identifier:MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    uint256 public tokencounter;

    constructor() public ERC721("DOGGY", "DOG") {
        tokencounter = 0;
    }

    function createCollectible(string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newtokenid = tokencounter;
        _safeMint(msg.sender, newtokenid);
        _setTokenURI(newtokenid, tokenURI);
        tokencounter = tokencounter + 1;
        return newtokenid;
    }
}
