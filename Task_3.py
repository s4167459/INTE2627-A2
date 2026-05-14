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

 # Derived encrypted IDs
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
def multi_sig_msg(sig_1, sig_2, sig_3, sig_4, n):
    multi_sig = pow((sig_1 * sig_2 * sig_3 * sig_4),1, n)

    return multi_sig


 # TODO: URGENT create input tuple and make sure it returns message, signature, and multisig public component t.

 # Verifies the returned signatures to ensure they were not tampered
def Verify(A_id = 126,B_id,C_id,multi_sig, e, n):






    return result

""" Below is code test running the math, feel free to ignore, but delete before submission {temporary}"""

 # generate warehouse indi-sig
a_sig = sign_message(a)
b_sig = sign_message(b)
c_sig = sign_message(c)
d_sig = sign_message(d)

 # generate multi-sig{s} of multi-sig(t,s)
multi_sig = multi_sig_msg(fill_later)

returned_sig_validate(multi_sig, PKG_e, PKG_n)

