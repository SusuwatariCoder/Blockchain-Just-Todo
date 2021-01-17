// test/YourName.test.js
// Load dependencies
const { expect } = require('chai');

// 加载合约
const YourName = artifacts.require('YourName');

contract('YourName', function(){
    beforeEach(async function(){
        this.YourName = await YourName.new();
    }) 

    // 测试用例
    it('retrieve returns a value previously stored', async function () {
         // 存一个值
        await this.YourName.store("LSY");

        // 测试值是否相同
        expect((await this.YourName.retrieve()).toString()).to.equal('LSY');
    })
})