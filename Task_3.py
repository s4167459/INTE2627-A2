import Task_1
import Task_2


 # Initialising the cryptographic components

 # Procurement Officer's cryptographic components
PO_p = 1080954735722463992988394149602856332100628417
PO_q = 1158106283320086444890911863299879973542293243
PO_e = 106506253943651610547613
 # derived Procurement Officer cryptographic components
PO_n = PO_p * PO_q
PO_phi_n = (PO_p-1) * (PO_q-1)
PO_d = pow(PO_e, -1, PO_n)

 # PKG cryptographic Parameters.
PKG_p = 1004162036461488639338597000466705179253226703
PKG_q = 950133741151267522116252385927940618264103623
PKG_e = 973028207197278907211
 # Derived Procurement Officer cryptographic components
PKG_n = PKG_p * PKG_q
PKG_phi_n = (PKG_p -1) * (PKG_q -1)
PKG_d = pow(PKG_e, -1, PKG_n)

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
t_key = pow((Ag * Bg * Cg * Dg),1, PKG_n)


 # Retrieves the quantity of the item with the ID submitted by the user.
def query_item(item_id, filename):
    logs = []
    logs.append(f"[SEARCH] search request made")
    logs.append(f"[ID] designated item id: {item_id}")
    logs.append(f"[FORWARDED] Search request forwarded to PKG")
    logs.append(f"[STORAGE] searching inventory records of: {filename}")
    file = open(filename, 'r')
    fl = []
    for line in file.readlines():
        fl.append(line)
    fl = fl[item_id].split(',')
    logs.append
    return fl[1]




# TODO: either use hash method from previous task or create new hash method and call inside of below function
# TODO: message hasn't been hashed yet, this will exclusively be a test format, full implementation after skeleton
 # Signs message using individual
def sign_message(message, encrypted_id, rand_num, n):

    signature = pow((encrypted_id * rand_num), message, n)

    return signature
""" Just a general note that the above sign_message method may function better in html if is a print instead of return
    if that turns out to be the case, feel free to switch it, William.
    
    Additional note for html implementation: call this function 4 times, once for each inventory signature,
    I'll leave an example of which variables to use below, 
"""


 # Calculates multi-signature using all warehouse signatures
def multi_sig_msg(sig_A, sig_B, sig_C, sig_D, n, originator):
    """ Calculates the multi-signature based on the signatures of each warehouse"""

    logs = []
    logs.append(f"[ORIGINATOR] Warehouse conducting multi-signature equation {originator}")
    logs.append(f"[SIGNATURE] Warehouse A: {sig_A}")
    logs.append(f"[SIGNATURE] Warehouse B: {sig_B}")
    logs.append(f"[SIGNATURE] Warehouse C: {sig_C}")
    logs.append(f"[SIGNATURE] Warehouse D: {sig_D}")
    logs.append(f"[CALCULATION] multi-signature: {sig_A} * {sig_B} * {sig_C} * {sig_D} mod {n}")

    multi_sig = pow((sig_A * sig_B * sig_C * sig_D),1, n)
    logs.append(f"[SIGNATURE] multi-signature: {multi_sig}")
    return {"originator": originator}


 # TODO: URGENT create input tuple and make sure it returns message, signature, and multisig public component t.


 # Encrypts data using public keys
def RSA_encrypt(message,n,e):
    logs = []
    logs.append(f"[KEYS] n = {n}")
    logs.append(f"[KEYS] e = {e}")
    logs.append(f"[MESSAGE] message to be encrypted: {message}")
    ciphertext = pow(message,e,n)
    logs.append(f"[CIPHERTEXT] generated ciphertext: {ciphertext}")
    return {"message": message,
            "e": e,
            "n": n,
            "encrypted_message": ciphertext
    }


 # Simulates the consensus check to ensure all nodes return the same value
def confirm_consensus(A_multi_sig, B_multi_sig, C_multi_sig, D_multi_sig, originator):

    logs = []
    logs.append(f"[ORIGINATOR] Warehouse conducting confirmation: {originator}")
    logs.append(f"[SIGNATURE] Warehouse A: {A_multi_sig}")
    logs.append(f"[SIGNATURE] Warehouse B: {B_multi_sig}")
    logs.append(f"[SIGNATURE] Warehouse C: {C_multi_sig}")
    logs.append(f"[SIGNATURE] Warehouse D: {D_multi_sig}")
    logs.append(f"[VERDICT] All signatures match")
    if A_multi_sig == B_multi_sig == C_multi_sig == D_multi_sig:
        return {f"originator": originator,
                f"A_sig": A_multi_sig,
                f"B_sig": B_multi_sig,
                f"C_sig": C_multi_sig,
                f"D_sig": D_multi_sig,
                f"verdict": "All signatures match.",
                f"logs": logs
        }
    else:
        return {f"A_sig": A_multi_sig,
                f"B_sig": B_multi_sig,
                f"C_sig": C_multi_sig,
                f"D_sig": D_multi_sig,
                f"Verdict": "Mismatch detected.",
                f"logs": logs
        }

 # simulates PKG Verifying the returned signatures to ensure they were not tampered
def verify_signature(multi_sig, hashed_message, a= A_id, b= B_id, c= C_id, d= D_id, e= PKG_e, n= PKG_n, t= t_key):

    """We calculate 2 components the first using the multi-signature and the PKG public key components,
       We then check to see if it matches with the calculation done with the Warehouse IDs and the hashed message
       """
    Logs = []
    first_half = pow(multi_sig, e, n)
    second_half = pow(((a * b * c * d) * pow(t,hashed_message),1,n))
    if first_half == second_half:
        return (f"first equation:\n"
                f"{multi_sig}^{e} mod {n}: {first_half}\n"
                f"\n"
                f"Second Equation: ({a} * {b} * {c} * {d}) * {t}^{hashed_message} mod {n}\n"
                f"Both equations have the same result, therefore the signature is valid\n"
                f"\nMessage has been forwarded")
    else:
        return (f"first equation:\n"
                f"{multi_sig}^{e} mod {n} = {first_half}\n"
                f"\n"
                f"Second Equation: ({a} * {b} * {c} * {d}) * {t}^{hashed_message} mod {n} "
                f"= {second_half}\n")


 # decrypts the encrypted message
def RSA_decrypt(encrypted_msg, d, n):
    """ The Procurement Officer decrypts the message after confirming the signatures are valid"""
    logs = []
    logs.append(f"[KEYS] d = {d}")
    logs.append(f"[KEYS] n = {n}")
    logs.append(f"[CIPHERTEXT] encrypted data = {encrypted_msg}")
    logs
    msg = pow(encrypted_msg, d, n)
    return

""" Below is code test running the math, feel free to ignore, but delete before submission {temporary}

 # generate warehouse indi-sig
a_sig = sign_message(a)
b_sig = sign_message(b)
c_sig = sign_message(c)
d_sig = sign_message(d)

 # generate multi-sig{s} of multi-sig(t,s)
multi_sig = multi_sig_msg(fill_later)

returned_sig_validate(multi_sig, PKG_e, PKG_n)

"""

print(query_item(1,"InvA.csv"))