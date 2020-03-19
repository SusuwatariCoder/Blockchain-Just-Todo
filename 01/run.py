from web3 import Web3
# 安装 web3.py : pipenv install web3
# 添加 infura ID 生成的URL
infura_url = "https://mainnet.infura.io/v3/e3b9d71c697e42a190f780e7971d8113"

web3 = Web3(Web3.HTTPProvider(infura_url))

print(f'网络连接状态：{web3.isConnected()}')  # 连接网络
print(f'区块数量: {web3.eth.blockNumber}')
print(f'最新区块信息：{web3.eth.getBlock("latest")}')
# print(web3.eth.getBalance("0x73706964657230330b09036a"))
print(web3.eth.contract())