from fileinput import filename


# Functions defined before main code implementation

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

 # Main Code Implementation
add_record(r"test_warehouse.csv", user_input_file_test())

print(read_file(r"test_warehouse.csv"))