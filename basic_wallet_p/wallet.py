from flask import Flask, jsonify, request


# Instantiate our Node
app = Flask(__name__)

# Account balances in a blockchain currency are not real values that are stored somewhere.
# Instead, wallet programs derive this balance by adding and subtracting all of the transactions for the user that are
# recorded in the ledger, to calculate the current balance.
#
# Build a simple wallet app using the front-end technology of your choice.  You will not be evaluated on the aesthetics of your app.
#
# This app should:
#     * Allow the user to enter, save, or change the `id` used for the program
#     * Display the current balance for that user
#     * Display a list of all transactions for this user, including sender and recipient
#

@app.route('/', methods=['POST'])
def home():
    pass


@app.route('/wallet', methods=['POST'])
def wallet():
    pass


@app.route('/transaction', methods=['POST'])
def transaction():
    pass


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
