// migrations/2_deploy.js
// 部署迁移脚本
const YourName = artifacts.require("YourName");

module.exports = async function (deployer) {
    await deployer.deploy(YourName);
  };