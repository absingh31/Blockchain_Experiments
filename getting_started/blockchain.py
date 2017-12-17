from block import Block
from genesis import create_genesis_block
from new_block import next_block

''' Create a blockchain and add the genesis block '''

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

''' Number of blocks to add after the genesis block '''

num_of_blocks_to_add = int(input("Enter the number of blocks to be added to blockchain"))

''' Adding the blocks to chain '''
for i in range(0, num_of_blocks_to_add):
	block_to_add = next_block(previous_block)   # Taken from new_block.py
	blockchain.append(block_to_add)

	previous_block = block_to_add

	''' We have to tell every node about this transaction '''
	print("Block #{} has been added to the blockchain!".format(block_to_add.index))
	print("Hash: {}\n".format(block_to_add.hash))

