// scripts/index.js
module.exports = async function main(callback) {
    try {
        // 获得本地节点 账户
        const accounts = await web3.eth.getAccounts();
        console.log(accounts)

        // 与合同交互 

        // 1. 抽象合同
        const YourName = artifacts.require("YourName");
        const name = await YourName.deployed();

        // 2. 调用方法
        value = await name.retrieve();

        console.log("你的名字是: ", value.toString());

        // 3. 改变变量
        await name.store("Lsy");

        newValue = await name.retrieve();
        console.log("你的新名字是: ", newValue.toString());

        callback(0)
    } catch (error) {
        console.error(error)
        callback(1)
    }
}