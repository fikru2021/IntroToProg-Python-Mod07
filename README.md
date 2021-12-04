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


pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)
open the pickle file, use pickle.load() to load it to a var.

print(example_dict)
print(example_dict[3])
This shows that we have retabined the dict data-type.
https://pythonprogramming.net/python-pickle-module-save-objects-serialization/.  ( External site).

Create a new sub-folder called Assignment07 inside the _PythonClass folder

![image](https://user-images.githubusercontent.com/94755079/144726353-145842a7-ae3a-467c-845b-add47feb77f0.png)

Create a new project in PyCharm that uses the _PythonClass\Assignment07 folder as its location 
 
![image](https://user-images.githubusercontent.com/94755079/144726355-08291265-c706-4c5c-a8e2-1098ac957f48.png)

Fig 2. Showing a new project in Pychram in the right folder 
Create a file called, "Assigment07.py," in your project.

 
Fig3. Showing Assignment07.py in the right folder 
![image](https://user-images.githubusercontent.com/94755079/144726367-eb530994-d68c-4485-bd5d-fab89974a9b3.png)
Add code to your script that performs the assignment’s task. Don't forget to include the script's header.
-	Step 1: Import pickle from another code file 
 ’
-	Fig4.1 Showing code to import pickle 
-	Step 2: Pickling demo
 
-	Fig 4.2. Showing pickling demo 
-	Step 3: Store the data using the pickle.dump method
-	 
-	Fig 4.3. Showing a code that is used to store data using pickle.dump method
-	Step 4: Read the data back using the picke load method
![image](https://user-images.githubusercontent.com/94755079/144726385-919521da-1fb6-4a87-8183-00e5e4214834.png)

![image](https://user-images.githubusercontent.com/94755079/144726392-ddd71a93-62cb-4377-af8c-e2e20fedea06.png)
-	Step 5: Error handling 

![image](https://user-images.githubusercontent.com/94755079/144726400-7769de7a-8a32-4229-b547-d349a54adc05.png)

![image](https://user-images.githubusercontent.com/94755079/144726417-d1be4b08-c316-4272-b681-d5d624d60f93.png)
![image](https://user-images.githubusercontent.com/94755079/144726425-13c3eb94-9399-4429-9143-501bdf89ea53.png)

Run the script in BOTH PyCharm and an OS command/shell window and capture images of it working on your computer![image](https://user-images.githubusercontent.com/94755079/144726431-25ba9a11-6e0f-4c53-829b-b0bc3ed745f8.png)
![image](https://user-images.githubusercontent.com/94755079/144726439-45228f67-2eb4-4a03-97ce-c5edb065b3e0.png)

![Uploading image.png…]()
Summary
In general, working on this assignment, , I have learned about about exception handling and Python’s pickling module, and how you use them.
![Uploading image.png…]()



