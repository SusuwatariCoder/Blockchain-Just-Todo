from web3 import Web3


def demo1(private_key_A,account_A, account_B):
	"""
	A 向 B  发送一笔交易
	:param private_key_A:
	:param account_A:
	:param account_B:
	:return:
	"""
	ganache_url = "http://127.0.0.1:7545"      # 本地区块链
	web3 = Web3(Web3.HTTPProvider(ganache_url))
	"""
	发送 交易  A ==> B
	"""
	# 获取帐户nonce或交易计数。这是交易的必填字段，因为它可以防止出现双重支出问题
	nonce = web3.eth.getTransactionCount(account_A)
	# print(nonce)

	# 构造交易
	tx = {
	    'nonce': nonce,
	    'to': account_B,
	    'value': web3.toWei(1, 'ether'),
	    'gas': 2000000,
	    'gasPrice': web3.toWei('50', 'gwei'),
	}
	# print(tx)
	# 使用私钥对交易进行签名
	signed_tx = web3.eth.account.signTransaction(tx, private_key_A)
	# print(signed_tx)
	# 发送交易到网络中, 得到交易hash
	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	print(tx_hash)
	# 将交易哈希值转换为十六进制
	# 用ASCII表达式来表示一个字符型常量，或者用单引号内加反斜杠表示转义字符。
	# 'A', '\x2f', '\013';
	# 其中：\x表示后面的字符是十六进制数，\0表示后面的字符是八进制数。
	# 例如十进制的17用十六进制表示就是
	# ‘\x11’,用八进制表示就是‘\021’
	# BYTE是让人关注它的长度，而不需要关注它的类型
	print(web3.toHex(tx_hash))
	# bytea类型支持两种输入输出的外部格式："hex" 格式和PostgreSQL的历史"escape"格式。 这两种格式通常在输入中使用


	#Web3.py调用智能合约功能， 需要将智能合约部署到网络中。我将使用Remix创建一个智能合约
	"""
	部署的合约信息
	 transaction hash 	0xe292e034a90918de6e22a127041a00825b8f082edc9fb08972d4724da97adc7f
	 from 	0x8178d29064359C6a84CE0405169B5d8ef1E2fF9F
	 to 	FJYToken.(constructor)
	   
	  0xe292e034a90918de6e22a127041a00825b8f082edc9fb08972d4724da97adc7f
	  0x608060405234801561001057600080fd5b5061032d806100206000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806370a082311461005c5780637207c19f146100b3578063a9059cbb146100e0575b600080fd5b34801561006857600080fd5b5061009d600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061012d565b6040518082815260200191505060405180910390f35b3480156100bf57600080fd5b506100de60048036038101908080359060200190929190505050610145565b005b3480156100ec57600080fd5b5061012b600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061018b565b005b60006020528060005260406000206000915090505481565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555050565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054101515156101d857600080fd5b6000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054011015151561026557600080fd5b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540392505081905550806000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050505600a165627a7a72305820f2b62d482af3e908226bc450e2363464694ccf980b6a8b2277e2bd90ba164eb90029
	
	合约地址：
	https://ropsten.etherscan.io/tx/0x59b39549a4d8069793923e43481b78bb4b176b6093a3361580700fb32541bfe5
	"""

def demo2():
	"""
	智能合约创建 部署 函数调用
	:return:
	"""
	import json

	abi = json.loads('''
	[
		{
			"constant": false,
			"inputs": [
				{
					"name": "initialSupply",
					"type": "uint256"
				}
			],
			"name": "MyToken",
			"outputs": [],
			"payable": false,
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"constant": false,
			"inputs": [
				{
					"name": "_to",
					"type": "address"
				},
				{
					"name": "_value",
					"type": "uint256"
				}
			],
			"name": "transfer",
			"outputs": [],
			"payable": false,
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"constant": true,
			"inputs": [
				{
					"name": "",
					"type": "address"
				}
			],
			"name": "balanceOf",
			"outputs": [
				{
					"name": "",
					"type": "uint256"
				}
			],
			"payable": false,
			"stateMutability": "view",
			"type": "function"
		}
	]
		''')

	ganache_url = "http://127.0.0.1:7545"
	web3 = Web3(Web3.HTTPProvider(ganache_url))
	# 设置了一个“默认”帐户，用于与区块链进行交互
	web3.eth.defaultAccount = web3.eth.accounts[0]
	address = web3.toChecksumAddress(web3.eth.defaultAccount)
	print(web3.eth.accounts[0])
	print(address)
	# 初始化合约
	contract = web3.eth.contract(address=address, abi=abi)

	tx_hash = contract.functions.transfer("0x8178d29064359C6a84CE0405169B5d8ef1E2fF9F", 11).transact()
	print(tx_hash)
	# 交易写入，等待挖矿
	web3.eth.waitForTransactionReceipt(tx_hash)
	print('收款方: {}'.format(contract.functions.balanceOf("0x8178d29064359C6a84CE0405169B5d8ef1E2fF9F").call()))



def demo3():
	"""
	用Python 部署智能合约 ， 并调用合约函数， 生成初始 Token 币

	:return:
	"""
	import json
	from web3 import Web3

	# 连接本地区块链网络
	ganache_url = "http://127.0.0.1:7545"
	web3 = Web3(Web3.HTTPProvider(ganache_url))

	# 获取 智能合约ABI和字节码
	abi = json.loads("""
	[
	{
		"constant": false,
		"inputs": [
			{
				"name": "initialSupply",
				"type": "uint256"
			}
		],
		"name": "MyToken",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
	""")
	bytecode = "608060405234801561001057600080fd5b5061032d806100206000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806370a082311461005c5780637207c19f146100b3578063a9059cbb146100e0575b600080fd5b34801561006857600080fd5b5061009d600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061012d565b6040518082815260200191505060405180910390f35b3480156100bf57600080fd5b506100de60048036038101908080359060200190929190505050610145565b005b3480156100ec57600080fd5b5061012b600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061018b565b005b60006020528060005260406000206000915090505481565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555050565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054101515156101d857600080fd5b6000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054816000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054011015151561026557600080fd5b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282540392505081905550806000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050505600a165627a7a72305820f2b62d482af3e908226bc450e2363464694ccf980b6a8b2277e2bd90ba164eb90029"
	# 将默认帐户设置为发送方
	web3.eth.defaultAccount = web3.eth.accounts[1]
	print(web3.eth.defaultAccount)
	# 实例化 进行合约部署
	FJYToken = web3.eth.contract(abi=abi, bytecode=bytecode)
	# 将其部署到网络，并等待这样的交易反馈
	tx_hash = FJYToken.constructor().transact()
	tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
	print(tx_hash)
	print(tx_receipt)
	print(f"合约地址{tx_receipt.contractAddress}")
	# 调用合约
	contract = web3.eth.contract(
		address=tx_receipt.contractAddress,
		abi=abi,
	)

	# 调用合约函数 初始化 Token 数量 5000
	tx_hash = contract.functions.MyToken(5000).transact()

	# 等待被挖矿打包
	web3.eth.waitForTransactionReceipt(tx_hash)
	print('Total Token: {}'.format(
		contract.functions.balanceOf(web3.eth.defaultAccount).call()
	))


if __name__ == "__main__":
	account_A = '0x545fB1B8Ea8dfa80C10B1C357116B24843D0D6a1'  # 账户A 地址
	account_B = '0x8178d29064359C6a84CE0405169B5d8ef1E2fF9F'  # 账户B 地址
	# A 的私钥
	private_key_A = '4187f60d82d6c794ecd46125e309aea3b6046eda12289397f39a414d6cadab0f'

	# web3.py 实现以太坊转账
	demo1(private_key_A, account_A, account_B)

	# web3.py 实现智能合约调用
	demo2()

	# web3.py 实现智能合约开发，部署，调用
	demo3()


