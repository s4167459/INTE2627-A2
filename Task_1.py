from fileinput import filename


# Functions defined before main code implementation

def read_file(filename):
    file = filename().open()
    file_contents = []
    file_contents = file.read()
    filename.close()
    return file_contents

def write_to_file(file_name, contents):
    file = file_name.open()
    file.write(contents)
    file.close()

 # test to see if file is successfully created, and then see what happens when csv is output through print()
def user_input_file_test():
    user_in = str(input("Enter CSV record: \n"))
    print("file has been overwritten with singular record for test purposes)")
    return user_in

 # Main Code Implementation

write_to_file("test_warehouse.csv", user_input_file_test())
