"""
基于Python Web3.py 进行以太坊开发
"""
def demo1():
	"""
	连接以太坊网络，并完成区块链基本的查询，对测试账户余额进行查询
	:return:
	"""
	from web3 import Web3
	# Infura RPC URL
	infura_url = "https://mainnet.infura.io/v3/e3b9d71c697e42a190f780e7971d8113"

	web3 = Web3(Web3.HTTPProvider(infura_url))
	print(f"连接状态： {web3.isConnected()}")
	print(f"最新块：{web3.eth.blockNumber}")  # 以太坊最新块： 9725118
	# 测试账户: 0x21eb14be414eDC32A819525C231c3eE97dc811F8
	account = "0x21eb14be414eDC32A819525C231c3eE97dc811F8"
	money_wei = web3.eth.getBalance(account)
	maney_eth = web3.fromWei(money_wei, "ether")  # money_wei / pow(10, 18)

	print(f"账户余额： {money_wei} wei")  # 帐户余额用wei表示, ETH 的最小单位
	print(f"账户余额： {maney_eth} eth")  # 帐户余额用eth表示, ETH 的最小单位  0.0098ETH



def demo2():
	"""
	进行以太坊智能合约的调用 和 数据写入
	:return:
	"""
	import json
	from web3 import Web3
	infura_url = "https://mainnet.infura.io/v3/e3b9d71c697e42a190f780e7971d8113"
	web3 = Web3(Web3.HTTPProvider(infura_url))

	# 使用web3.eth.Contract()函数获得以太坊智能合约的Python表示形式
	# 函数需要两个参数：一个用于智能合约ABI，一个用于智能合约地址
	address = "0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0"

	# 例子 OMG 币的智能合约调用
	abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"bytes32"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"stop","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint128"}],"name":"push","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"name_","type":"bytes32"}],"name":"setName","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint128"}],"name":"mint","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"src","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"stopped","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"wad","type":"uint128"}],"name":"pull","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint128"}],"name":"burn","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"bytes32"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"start","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"src","type":"address"},{"name":"guy","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"symbol_","type":"bytes32"}],"payable":false,"type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]')
	# print(abi)
	contract = web3.eth.contract(address=address, abi=abi)
	# 实现了像几个功能totalSupply()，name()，symbol()，和balanceOf()

	totalSupply = contract.functions.totalSupply().call()
	print(f"Token: EOS ")
	print(f"发行总数： {totalSupply}")
	print(f"兑换ETH总价值：{web3.fromWei(totalSupply, 'ether')}")
	print(contract.functions.name().call())
	print(contract.functions.symbol().call()) # 代币符号 EOS

	# 账上金额
	balance = contract.functions.balanceOf('0x21eb14be414eDC32A819525C231c3eE97dc811F8').call()
	print(web3.fromWei(balance, 'ether'))

if __name__ == "__main__":

	demo1()
	demo2()




