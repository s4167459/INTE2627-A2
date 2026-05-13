import Task_1

# Byzantine Fault Tolerant consensus - chosen because the scenario requires handling
# malicious/inconsistent nodes, not just crashes. With 4 nodes, system tolerates 1 byzantine
# node and requires 3/4 agreement to accept a record.


def simulate_node_verification(record, signature, originator_id):
    """
    Each node independently verifies signature using originator's public key.
    Returns True/False representing that node's vote.
    """
    keys = Task_1.get_node_keys(originator_id)
    return Task_1.verify_signature(record, signature, keys['e'], keys['n'])


def bft_consensus(record, signature, originator_id):
    """
    Simplified BFT consensus round.
    All non-originating nodes verify record signature and cast vote.
    Consensus passes if >= 3 of 4 nodes approve (tolerates 1 byzantine node).
    Returns dict with each node's vote and final consensus result.
    """
    nodes = ['A', 'B', 'C', 'D']
    votes = {}

    for node_id in nodes:
        if node_id == originator_id:
            # Originator would auto-vote yes as they created and signed it
            votes[node_id] = True
        else:
            votes[node_id] = simulate_node_verification(record, signature, originator_id)

    approvals = sum(votes.values())
    threshold = 3  # BFT threshold is floor((4-1)/3) + 1 thus needs 3 of 4 votes
    consensus_reached = approvals >= threshold

    return {
        'votes': votes,
        'approvals': approvals,
        'threshold': threshold,
        'consensus_reached': consensus_reached
    }


def store_to_all_nodes(record):
    """
    After consensus, store accepted record to every node's local CSV.
    Simulates each node appending to their own local database.
    """
    node_files = {
        'A': r'InvA.csv',
        'B': r'InvB.csv',
        'C': r'InvC.csv',
        'D': r'InvD.csv',
    }
    for node_id, filepath in node_files.items():
        Task_1.add_record(filepath, record + '\n')


def submit_record(node_id, quantity, price, location):
    """
    Full Task 1 lifecycle: create -> sign -> verify -> consensus -> store
    Returns a dict the frontend can display at each step
    """
    # Create record string
    record = f"{Task_1.iter_val}, {quantity}, {price}, {location}"

    # Get originating node's keys
    keys = Task_1.get_node_keys(node_id)

    # Sign with originating node's private key
    signature = Task_1.sign_record(record, keys['d'], keys['n'])
    hash_val = Task_1.hash_record(record)

    # Every other node verifies with originator's public key
    verification_results = {}
    for nid in ['A', 'B', 'C', 'D']:
        if nid != node_id:
            valid = Task_1.verify_signature(record, signature, keys['e'], keys['n'])
            verification_results[nid] = valid

    # BFT consensus round
    consensus = bft_consensus(record, signature, node_id)

    #  Store to all nodes if consensus passed
    if consensus['consensus_reached']:
        store_to_all_nodes(record)
        Task_1.iterate_id()

    return {
        'record': record,
        'hash': hex(hash_val),
        'signature': hex(signature),
        'verifications': verification_results,
        'consensus': consensus,
        'accepted': consensus['consensus_reached']
    }
