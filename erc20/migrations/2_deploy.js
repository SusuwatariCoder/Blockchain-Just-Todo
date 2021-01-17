// migrations/2_deploy.js
// 部署迁移脚本
const FJYToken = artifacts.require("FJYToken");

module.exports = async function (deployer) {
    await deployer.deploy(FJYToken, );
  };