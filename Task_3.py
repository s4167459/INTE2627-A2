import Task_1
import Task_2


 # Initialising the cryptographic components



 # Procurement Officer's cryptographic components
PO_p = 1080954735722463992988394149602856332100628417
PO_q = 1158106283320086444890911863299879973542293243
PO_e = 106506253943651610547613
PO_n = p * q
PO_phi_n = (p-1) * (q-1)


 # Implement a mechanism that allows an authorised external user to submit a query request to the
 # distributed inventory system.

auth_user_lst = (PO_n)


 # authorised user enters an identifier and the id of the item they wish to search for.
def auth_user_search(user_sig, search_id):


 # verification, may not be necessary
def verify_user_auth(user_sig):

