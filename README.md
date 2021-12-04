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
