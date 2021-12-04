# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# FikruAbasori,11.28.2021,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# pickling demo
customer_id = int(input("Enter an ID: "))
customer_name = str(input("Enter a Name: "))
customer_list = [{"CID": customer_id, "CName": customer_name}]
print(customer_list)

# store the data using the pickle.dump method
objFile = open("AppData.dat", "wb")
pickle.dump(customer_list, objFile)
objFile.close()

# Read the data back using the pickle.load method
objFile = open("Appdata.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData, type(objFileData))

for row in objFileData:
    for k, v in dict(row).items():
        print(k, v)

''' Error Handling Demo'''

# Demo 1
try:
    quotient = 10 / 0
    print(quotient)
except:
    print("There was an error! << Custom Message")

# Demo2

try:
    quotient = 10 / 0
    print(quotient)
except Exception as e:
    print("There was an error!")
    print("Built-In pythons error info: ")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())

# Demo 3

try:
    quotient = 12 / 0
    print(quotient)
except ZeroDivisionError as e:
    print("Please do not use Zero for the second number!")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There as an error!")
    print(e, e.__doc__, type(e), sep='\n')

''' Testing Both '''

try:
    customer_id = int(input("Enter an Id: "))
    customer_name = str(input("Enter a Name: "))
    lstCustomer = [customer_id, customer_name]
    print(lstCustomer)
except Exception as e:
    print("there was an error! Make sure to use integers for IDs. ")
    print(e, e.__doc__, type(e), sep='\n')

# store data using pickle.dump method

try:
    file = open("AppData.dat", "ab")
    pickle.dump(lstCustomer, file)
    file.close()
except Exception as e:
    print(" There was an error! Check file permissions. ")
    print(e, e.__doc__, type(e), sep='\n')

# read the data using pickle.load method

try:
    file = open("AppData.dat", "rb")
    file_data = pickle.load(file)
    file.close()
    print(file_data)
except FileNotFoundError as e:
    print(" The file must exist before trying to read it!")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a genera; error!")
    print(e, e.__doc__, tyep(e), sep='\n')
