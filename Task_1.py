from fileinput import filename
import hashlib
 # imports count to be able to increment the item_id attribute of the Record object
from itertools import count

 # Record class to create an object containing a new record to be added to inventory
 """
 I found that there may be too many difficulties with this approach when implementing in python, opted for dictionary
 instead, but left this here in case we decide it is a better option later.
 """
"""
class Record:

    item_id_iter = count()
    def __init__(self, item_id, quantity, price, location):

        self.quantity = quantity
        self.price = price
        self.location = location
        self.item_id = next(Record.item_id_iter)
"""
#shelved for now

Record.create_new_record()

first = Record(1,3,5,"A")

record_list = {}

record_list[1] = (1,3,5,"A")
print(record_list)


# Functions defined before main code implementation


global iter_val = var = 0

 # function keeps track of the iterative id of each subsequent record
 """
 I'm still trying to figure this out, but i essentially want this function to iterate on the id value for each record
 automatically. might just scrap it for manual entry
 """
def iterate_id():
    iter_val += 1

def get_new_record(quantity, price, location):
    record_id = iter_val
    final_str = f"{record_id}, {quantity}, {price}, {location}\n"
    iterate_id()
    if location.lower() == 'a':
        add_record(r'InvA.csv', final_str)

    elif location.lower() == 'b':
        add_record(r'InvB.csv', final_str)

    elif location.lower() == 'c':
        add_record(r'InvC.csv', final_str)

    elif location.lower() == 'd':
        add_record(r'InvD.csv', final_str)

def read_file(filename):
    file = open(filename)
    file_contents = []
    file_contents = file.read()
    file.close()
    return file_contents

def add_record(file_name, contents):
    file = open(file_name, mode="a")
    file.write(str(contents))
    file.close()

def clear_file(file_name):
    file = open(file_name, mode="w")
    file.write("")
    file.close()

 # test to see if file is successfully created, and then see what happens when csv is output through print()
def user_input_file_test():
    user_in = str(input("Enter CSV record: \n"))
    print("file has been overwritten with singular record for test purposes)")
    user_in += "\n"
    return user_in

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

 # Main Code Implementation

add_record(r"test_warehouse.csv", user_input_file_test())

print(read_file(r"test_warehouse.csv"))

 # to test for updates
