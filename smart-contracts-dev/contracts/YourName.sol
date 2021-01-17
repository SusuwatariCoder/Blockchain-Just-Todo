// contracts/YourName.sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract YourName is Ownable {
    // 一个存放名字的变量
    string  private name;
 
    // 先完成一个触发事件： 值改变时触发
    event NameChanged(string newName);

    // 存储一个新值到合约中
    function store(string memory newName) public onlyOwner {
        name = newName;
        // 规范： 必须触发事件，让区块链外部感知结果
        emit NameChanged(newName);
    }

    // 获取最新的值
    function retrieve() public view returns(string memory) {
        return name;
    }
}