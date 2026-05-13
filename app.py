from flask import Flask, render_template, request, jsonify
import Task_2
# import Task_3  # uncomment when Task 3 is ready

app = Flask(__name__)


# Index Route

# Serves the main HTML interface
@app.route('/')
def index():
    return render_template('interface.html')


# Task 1

# Handles sign and verify only, no consensus to demonstrate Task 1 in isolation
@app.route('/sign_and_verify', methods=['POST'])
def sign_and_verify():
    data = request.get_json()
    node_id = data['node_id']
    quantity = data['quantity']
    price = data['price']
    location = data['location']

    # Build record string using current iter_val from Task_1
    record = f"{Task_2.Task_1.iter_val}, {quantity}, {price}, {location}"

    # Get originating node's RSA keys
    keys = Task_2.Task_1.get_node_keys(node_id)

    # Hash and sign record with originating node's private key
    hash_val = Task_2.Task_1.hash_record(record)
    signature = Task_2.Task_1.sign_record(record, keys['d'], keys['n'])

    # Each other node verifies signature using originator's public key
    verifications = {}
    for nid in ['A', 'B', 'C', 'D']:
        if nid != node_id:
            valid = Task_2.Task_1.verify_signature(record, signature, keys['e'], keys['n'])
            verifications[nid] = valid

    # Return all intermediate values for display in frontend
    return jsonify({
        'record': record,
        'hash': hex(hash_val),
        'signature': hex(signature),
        'verifications': verifications
    })


# Task 2

# Handles full process: sign -> verify -> BFT consensus -> store to demonstrate Task 1 and 2 together during marking
@app.route('/submit_record', methods=['POST'])
def submit_record():
    data = request.get_json()
    node_id = data['node_id']
    quantity = data['quantity']
    price = data['price']
    location = data['location']

    # Calls submit_record in Task_2 which runs the full pipeline
    # Returns record, hash, signature, per-node verifications, consensus votes and result
    result = Task_2.submit_record(node_id, quantity, price, location)
    return jsonify(result)


# Task 3 (placeholders)

# Handles authorised user query submission
# TODO: wire up Task_3 query submission function
@app.route('/query', methods=['POST'])
def query():
    pass

# Handles multi-signature verification of the queried result across nodes
# TODO: wire up Task_3 multi-signature verification function
@app.route('/verify_query', methods=['POST'])
def verify_query():
    pass

# Handles decryption and recovery of the protected query response at the user side
# TODO: wire up Task_3 decryption/recovery function
@app.route('/decrypt_result', methods=['GET'])
def decrypt_result():
    pass


# Main implementation

if __name__ == '__main__':
    app.run(debug=True)