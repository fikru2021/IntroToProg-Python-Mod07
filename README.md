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
![image](https://user-images.githubusercontent.com/94755079/144726278-18d009c4-6ca3-4944-a056-7b1a49b97b2a.png)
