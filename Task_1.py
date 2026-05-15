import hashlib
 # imports hashlib for hashing records

# Functions defined before main code implementation

def hash_record(record):
    """Takes in a string record and returns the hash value of that record as an integer
    """
    hash_val = int(hashlib.md5(record.encode()).hexdigest(), 16)
    return hash_val

def sign_record(record, d, n):
    """Takes in a string record and the private key (d, n) and returns the signature of the record as an integer
    """
    hash_val = hash_record(record)
    s = pow(hash_val, d, n)
    return s

def verify_signature(record, signature, e, n):
    """Takes in a string record, the signature of the record, and the public key (e, n) and returns True if the signature is valid and False otherwise
    """
    hash_val = hash_record(record)
    hash_from_signature = pow(signature, e, n)
    return hash_val == hash_from_signature

# Initialise the cryptographic parameters from key doc and derived from such

#Inv A
Ap = 1210613765735147311106936311866593978079938707
Aq = 1247842850282035753615951347964437248190231863
Ae = 815459040813953176289801
#Derived Inv A values
An = Ap * Aq
Ao_n = (Ap - 1) * (Aq - 1)
Ad = pow(Ae, -1, Ao_n)

#Inv B
Bp = 787435686772982288169641922308628444877260947
Bq = 1325305233886096053310340418467385397239375379
Be = 692450682143089563609787
#Derived Inv B values
Bn = Bp * Bq
Bo_n = (Bp - 1) * (Bq - 1)
Bd = pow(Be, -1, Bo_n)

#Inv C
Cp = 1014247300991039444864201518275018240361205111 #unfortunate naming scheme
Cq = 904030450302158058469475048755214591704639633
Ce = 1158749422015035388438057
#Derived Inv C values
Cn = Cp * Cq
Co_n = (Cp - 1) * (Cq - 1)
Cd = pow(Ce, -1, Co_n)

#Inv D
Dp = 1287737200891425621338551020762858710281638317
Dq = 1330909125725073469794953234151525201084537607
De = 33981230465225879849295979
#Derived Inv D values
Dn = Dp * Dq
Do_n = (Dp - 1) * (Dq - 1)
Dd = pow(De, -1, Do_n)

def get_node_keys(node_id):
    """Takes in a node ID and returns the corresponding public and private key values as a dictionary for convenience's sake"""
    keys = {
        'A': {'p': Ap, 'q': Aq, 'e': Ae, 'n': An, 'd': Ad},
        'B': {'p': Bp, 'q': Bq, 'e': Be, 'n': Bn, 'd': Bd},
        'C': {'p': Cp, 'q': Cq, 'e': Ce, 'n': Cn, 'd': Cd},
        'D': {'p': Dp, 'q': Dq, 'e': De, 'n': Dn, 'd': Dd},
    }
    return keys[node_id]
