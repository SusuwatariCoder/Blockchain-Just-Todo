// contracts/FJYToken.sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

 
contract FJYToken is ERC20,Ownable {
    constructor() public ERC20("FangJinYan Token", "FJY") {
         _mint(msg.sender, 1e8 ether);
    }

    // 矿工 获得 Token
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= 2e8, "Max totalSupply");
        _mint(to, amount);
    }
}