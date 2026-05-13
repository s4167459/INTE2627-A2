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



 # Implement a mechanism that allows an authorised external user to submit a query request to the
 # distributed inventory system.

 # List containing authenticated user public key component {temporary}
auth_user_lst = (PO_n)


 # authorised user enters an identifier and the id of the item they wish to search for.
def auth_user_search(user_sig, search_id):


 # verification, may not be necessary
def verify_user_auth(user_sig):



 # encrypting search results.

def encrypt_search(result, public_key):

