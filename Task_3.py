import hashlib

 # Initialising the cryptographic components

 # Procurement Officer's cryptographic components
POp = 1080954735722463992988394149602856332100628417
POq = 1158106283320086444890911863299879973542293243
POe = 106506253943651610547613
 # derived Procurement Officer cryptographic components
POn = POp * POq
PO_phi_n = (POp-1) * (POq-1)
POd = pow(POe, -1, PO_phi_n)
# fixed wrong variable being used to calculate private key

 # PKG cryptographic Parameters.
PKG_p = 1004162036461488639338597000466705179253226703
PKG_q = 950133741151267522116252385927940618264103623
PKG_e = 973028207197278907211
 # Derived Procurement Officer cryptographic components
PKG_n = PKG_p * PKG_q
PKG_phi_n = (PKG_p -1) * (PKG_q -1)
PKG_d = pow(PKG_e, -1, PKG_phi_n)
# another wrong variable used to calculate private key, changed to PKG_e and PKG_phi_n

 # initialising warehouse IDs
A_id = 126
B_id= 127
C_id = 128
D_id = 129
 # Derived encrypted IDs using PKGs secret key
Ag = pow(A_id, PKG_d, PKG_n)
Bg = pow(B_id, PKG_d, PKG_n)
Cg = pow(C_id, PKG_d, PKG_n)
Dg = pow(D_id, PKG_d, PKG_n)

 # initialising random number for each warehouse
Ar = 621
Br = 721
Cr = 821
Dr = 921
 # derived encrypted random numbers
A_er = pow(Ar, PKG_e, PKG_n)
B_er = pow(Br, PKG_e, PKG_n)
C_er = pow(Cr, PKG_e, PKG_n)
D_er = pow(Dr, PKG_e, PKG_n)

 # initialising the combined encrypted Warehouse IDs
t_key = pow((A_er * B_er * C_er * D_er), 1, PKG_n)

 # Retrieves the quantity of the item with the ID submitted by the user.
def query_item(item_id, filename):
    """ Retrieves the record with the id submitted by the user, and then returns the quantity value of the item."""
    logs = []
    logs.append(f"[TITLE] Query")
    logs.append(f"[SEARCH] search request made")
    logs.append(f"[ID] designated item id: {item_id}")
    logs.append(f"[FORWARDED] Search request forwarded to PKG")
    logs.append(f"[STORAGE] searching inventory records of: {filename}")
    file = open(filename, 'r')
    fl = []
    for line in file.readlines():
        fl.append(line)
    fl = fl[item_id].split(',')
    logs.append(f"[RETRIEVE] retrieved item {item_id} quantity: {fl[1]}\n")
    return {"record":fl[1],
            "logs": logs}


def hash_record(record):

    """Takes in a string record and returns the hash value of that record as an integer
    """
    hash_val = int(hashlib.md5(record.encode()).hexdigest(), 16)
    return hash_val


 # Signs message using the warehouses respective unique encrypted identifiers
def sign_message(message, encrypted_id, rand_num, n, originator, t_key= t_key):

    """ The warehouse generates a signature for the message using the encrypted random number, 
    the combined encrypted warehouse IDs, 
    and the encrypted ID of the warehouse itself."""

    # both message and t_key are integers, and must be concatenated together before being hashed,
    # they then will be returned as an integer hashed_message
    hashed_message = hash_record(str(t_key)+str(message))
    logs = []
    logs.append(f"[TITLE] Warehouse {originator} Signing Message")
    logs.append(f"[MESSAGE] Value to be signed: {message}")
    logs.append(f"[HASH] MD5 hash of message: {hashed_message}")
    logs.append(f"[MESSAGE] Message to be signed by Warehouse {originator}: {hashed_message}")
    logs.append(f"[KEYS] aggregate encrypted random numbers: {t_key}")
    logs.append(f"[KEYS] Encrypted id of Warehouse {originator}: {encrypted_id}")
    logs.append(f"[KEYS] Random number selected by Warehouse {originator}: {rand_num}")
    logs.append(f"[CALCULATION] {encrypted_id} * {rand_num}^{hashed_message} mod {n}")
    signature = pow(encrypted_id * pow(rand_num, hashed_message, n), 1, n)
    logs.append(f"[SIGNATURE] signature generated: {signature}\n")

    return {"originator": originator,
            "signature": signature,
            "logs": logs
            }


def multi_sig_msg(sig_A, sig_B, sig_C, sig_D, n, originator):
    """ Calculates the multi-signature based on the signatures of each warehouse.
        This runs once for each warehouse, simulating each node's calculation"""

    logs = []
    logs.append(f"[TITLE] Warehouse {originator} Generating Multi-Signature")
    logs.append(f"[SIGNATURE] Warehouse A: {sig_A}")
    logs.append(f"[SIGNATURE] Warehouse B: {sig_B}")
    logs.append(f"[SIGNATURE] Warehouse C: {sig_C}")
    logs.append(f"[SIGNATURE] Warehouse D: {sig_D}")
    logs.append(f"[CALCULATION] multi-signature: {sig_A} * {sig_B} * {sig_C} * {sig_D} mod {n}")

    multi_sig = pow((sig_A * sig_B * sig_C * sig_D),1, n)
    logs.append(f"[SIGNATURE] multi-signature: {multi_sig}\n")
    return {"originator": originator,
            "multisig":multi_sig,
            "logs":logs
            }


 # Encrypts data using public keys
def RSA_encrypt(message,n,e):

    """This function encrypts both the initial request made by the Procurement Officer, and the data returned
       By the query when being returned to the Procurement Officer by the PKG
       """
    logs = []
    logs.append(f"[TITLE] RSA Encrypting")
    logs.append(f"[KEYS] n = {n}")
    logs.append(f"[KEYS] e = {e}")
    logs.append(f"[MESSAGE] message to be encrypted: {message}")
    ciphertext = pow(message,e,n)
    logs.append(f"[CALCULATION] {message}^{e} mod {n}")
    logs.append(f"[CIPHERTEXT] generated ciphertext: {ciphertext}\n")
    return {"message": message,
            "e": e,
            "n": n,
            "encrypted_message": ciphertext,
            "logs": logs
            }


 # Simulates the consensus check to ensure all nodes return the same value
def confirm_consensus(A_multi_sig, B_multi_sig, C_multi_sig, D_multi_sig, originator):

    """ This Function simulates the consensus check initiated by the PKG, ensuring that the multi-signature
        generated by each node matches and is therefore valid."""
    logs = []
    logs.append(f"[TITLE] Confirming Consensus")
    logs.append(f"[ORIGINATOR] Warehouse conducting confirmation: {originator}")
    logs.append(f"[SIGNATURE] Warehouse A: {A_multi_sig}")
    logs.append(f"[SIGNATURE] Warehouse B: {B_multi_sig}")
    logs.append(f"[SIGNATURE] Warehouse C: {C_multi_sig}")
    logs.append(f"[SIGNATURE] Warehouse D: {D_multi_sig}")

    if A_multi_sig == B_multi_sig == C_multi_sig == D_multi_sig:
        logs.append(f"[VERDICT] All signatures match\n")
        return {f"originator": originator,
                f"A_sig": A_multi_sig,
                f"B_sig": B_multi_sig,
                f"C_sig": C_multi_sig,
                f"D_sig": D_multi_sig,
                f"verdict": "All signatures match.",
                f"logs": logs
        }
    else:
        logs.append(f"[VERDICT] Mismatch detected.\n")
        return {f"originator": originator,
                f"A_sig": A_multi_sig,
                f"B_sig": B_multi_sig,
                f"C_sig": C_multi_sig,
                f"D_sig": D_multi_sig,
                f"Verdict": "Mismatch detected",
                f"logs": logs
        }

 # simulates Procurement Officer Verifying the returned signatures to ensure they were not tampered
def verify_signature(multi_sig, hashed_message, a= A_id, b= B_id, c= C_id, d= D_id, e= PKG_e, n= PKG_n, t= t_key):

    """We calculate 2 components the first using the multi-signature and the PKG public key components,
       We then check to see if it matches with the calculation done with the Warehouse IDs and the hashed message
       """
    logs = []
    logs.append(f"[TITLE] Verifying Signature")
    logs.append(f"[KEYS] e = {e}")
    logs.append(f"[KEYS] n = {n}")
    logs.append(f"[KEYS] aggregate encrypted random numbers: {t_key}")
    logs.append(f"[ID] Warehouse A ID: {A_id}")
    logs.append(f"[ID] Warehouse B ID: {B_id}")
    logs.append(f"[ID] Warehouse C ID: {C_id}")
    logs.append(f"[ID] Warehouse D ID: {D_id}")
    logs.append(f"[MESSAGE] Hashed message: {hashed_message}")
    logs.append(f"[SIGNATURE] Multi-Signature: {multi_sig}")

     # Calculates first half of the match-check to ensure returned signature is valid.
    first_half = pow(multi_sig, e, n)
    logs.append(f"[CALCULATION] First match check: {multi_sig}^{e} mod {n} = {first_half}")

     # Calculates second half of the match-check to ensure returned signature is valid.
    second_half = pow((a * b * c * d) * pow(t, hashed_message, n), 1, n)
    logs.append(f"[CALCULATION] Second match check: ({a} * {b} * {c} * {d}) * {t}^{hashed_message} mod {n} "
                f"= {second_half}")

    if first_half == second_half:
        logs.append(f"[VERDICT] Both equations have the same result, therefore the signature is valid\n")
        return {"first_half": first_half,
                "second_half": second_half,
                "logs": logs
                }
    else:
        logs.append(f"[VERDICT] Both equations do not match, therefore the signature is invalid\n")
        return {"first_half": first_half,
                "second_half": second_half,
                "logs": logs
                }


 # decrypts the encrypted message
def RSA_decrypt(encrypted_msg, d, n):

    logs = []
    logs.append(f"[TITLE] RSA Decrypting")
    logs.append(f"[KEYS] d = {d}")
    logs.append(f"[KEYS] n = {n}")
    logs.append(f"[CIPHERTEXT] encrypted data = {encrypted_msg}")
    msg = pow(encrypted_msg, d, n)
    logs.append(f"[CALCULATION] Decrypting ciphertext: {encrypted_msg}^{d} mod {n}")
    logs.append(f"[PLAINTEXT] plaintext message (the quantity of item requested): {msg}\n")

    return {"plaintext": msg,
            "logs": logs
            }
