from block import Block
import datetime as date


def create_genesis_block():
	'''Manually construct block with 
	   index zero and arbitrary previous hash'''
	timestamp = date.datetime.now()
	return Block(0, timestamp, "Genesis Block", "0")
