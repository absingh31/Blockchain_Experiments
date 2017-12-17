from flask import Flask
from flask import request

node = Flask(__name__)

''' Store the transactions that this node has in a list '''
this_node_transactions = []

@node.route('/txion', methods = ['POST'])
def transactions():
	if request.method == 'POST':
		''' On each new post we extract the transaction data '''
		new_txion = request.get_json()

		''' Now we add the transaction to our list '''
		this_node_transactions.append(new_txion)

		''' Because the transaction was successfully submitted, I log it to my console '''
		print("New Transaction")
		print("From: {}".format(new_txion['from']))
		print("To: {}".format(new_txion['to']))
		print("Amount: {}\n".format(new_txion['amount']))

		''' Now let the client know it worked out '''

		return "Transaction submission successfull\n"

node.run()
