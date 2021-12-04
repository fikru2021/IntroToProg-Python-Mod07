Introduction:
Working on this assignment, I have learned about about exception handling and Python’s pickling module, and how you use them.
1) Exception Handling in Python
Python Try Except: The try block lets you test a block of code for errors, where as the except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try- and except blocks. When an error occurs, or exception as we call it , python will normally stop and generate an error message. Exceptions can be handled using the try statement:
For example: In this code below, the try block will generate an exception , because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")

Note: “ Since the try block raises an error, the except block will be executed. Without the try block, the program will crash and raise an error.” ( https://www.w3schools.com/python/python_try_except.asp. ) ( External site)
2) Pickling in Python

“ Pickling is the serializing and de-serializing of python objects to a byte stream. Unpicking is the opposite.” Pickling is used to store python objects. Objects likes lists, dictonaries, and class objects. Pickling is most useful with data analysis, where you are performing routine tasks on a data, such as pre-processing. In addition, it makes sense to use pickling if you are working with python-specific data types . such as dictonaries.

![image](https://user-images.githubusercontent.com/94755079/144726301-38f16fd6-1d36-4bae-8dc6-4c5871b88afd.png)

If you have a large dataset, for example, and you're loading that massive data set into memory every time you run the program, it may make a lot of sense to just pickle it, and then load that instead, because it will be far faster, again by 50 - 100x, sometimes far more depending on the size.
Example:

import pickle

example_dict = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

First, importpickle to use it, then define an exampke dictionary which is a pyhton object. Next open a file ( note that we open to write bytes in Python 3+), then we use pickle.dump() to put the dict into opened file, then close.
The above code will save the pickle file for us, now we need to cover how to access the pickled file:
![image](https://user-images.githubusercontent.com/94755079/144726339-776d67d9-1313-4c6a-ba8a-a27d97081bce.png)
