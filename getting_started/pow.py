from block import Block
import json
import datetime as date

''' Blockchain block class definition '''

miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

def proof_of_work(last_proof):
	''' Create a variable that we will use to find our next prrof of work '''
	incrementor = last_proof + 1

	''' Keep incrementing the incrementor until it's equal to a number
	divisible by 9 and proof of work of the previous block in chain '''

	while not (incrementor%9 == 0 and incrementor%last_proof == 0):
		incrementor += 1

	''' Once that number is found I'll return it as a proof of our work '''

	return incrementor


@node.route('/mine', methods = ['GET'])
def mine():
	''' Get the last proof of work '''
	last_block = blockchain[len(blockchain)-1]
	last_proof = last_block.data['proof-of-work']

	''' Find the proof of work for the current block 
	being mined '''
	''' Note: The program will hang in here until a new proof-of-work is found '''
	proof = proof_of_work(last_proof)

	''' Once I find a valid proof of work, I know I can mine
	a block so I reward the miner by adding a transaction '''
	this_nodes_transactions.append(
		{"from": "network", "to": miner_address, "amount":1}
		)

	''' Now I can gather the data needed to create the new block '''
	new_block_data = {
		"proof-of-work": proof,
		"transactions": list(this_nodes_transactions)
	}

	new_block_index = last_block.index + 1 
	new_block_timestamp = this_timestamp = data.datetime.now()
	last_block_hash = last_block.hash

	''' Empty transaction list '''
	this_nodes_transactions[:] = []

	''' Now create the block! '''
	mined_block = Block(
		new_block_index,
		new_block_timestamp,
		new_block_data,
		last_block_hash
		)

	blockchain.append(mined_block)

	''' Return the data in json format '''

	return json.dumps{
	"index": new_block_index,
	"timestamp": new_block_timestamp,
	"data": new_block_data,
	"hash": last_block_hash
	}

