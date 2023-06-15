#!/usr/bin/env python
# coding: utf-8

# Q-1 How do you comment code in python ? what are different type of comment?

# In[3]:


python use  hash symbol ("#") for  single line comment
 for example = # print ("neha")
    
  pythone does not support multiline comment , but as pythone does not execute string which is not assinment 
variable .stirng is written inside the triple qoutes .
 for example= 
    '''  
    I am neha rana
    learning pythone'''


# Q-2 What are variable in python? How do you declare and assign value to variable?
# 

# In[4]:


'''variable in pythone is named identifier that store tha value . it act as an container to hold data 
    during program execution .
      syntax 
            <variable name> =<value>
                                      '''
my_var="neha rana"
b=2


# Q-3 How do you convert one datatype  to another in python?
#     

# In[9]:


# to convert datatype to another we use typecasting 
a=2
print(type(a))

b=34.56
print(type(b))

c= 3+5j
print(type(c))

name="neha rana"
print(type(name))


# Q-4 How do write and execute a python script from command line?

# In[11]:


'''
    To write and execute a python script from the command line ,we should follow the steps
1-   Open a text editor (notepad ) and write your python code in it . save the file with a (myscript.py).
   
2-   Open a command promt (windows )

3-    To run the python script ,type: python  myscript.py

4=     Press enter ,and the script should execute .
                                                   '''


# Q-5 Given a list my_list =[1,2,3,4,5], write the code to slice the list and obtain the sub-list [2,3].

# In[12]:


my_list=[1,2,3,4,5]
my_list[1:3]


# Q-6 What is a complex number in mathematics , and how is it represent in python ?

# In[13]:


# complex number are number which repersent real and imaginry part.
a=5+6j


# In[14]:


a


# In[15]:


type(a)


# Q-7 What is the correct way to declare a variable named age and assign the value 25 to it?

# In[16]:


age=25
print(age)
_age =25
print(_age)


# Q-8 Declare a variable named price and assign the value 9.99 to it . What datatype does this variable blong to?

# In[17]:


a=9.99
print(a)
# data type
print(type(a))


# Q-9 Create a variable named name and assign your fullname to it as a string . How would you print the value of this variable ?

# In[18]:


var_name="Neha Rana"
print (var_name)
print(type(var_name))


# Q-10 Given the string "Hello world" , extract the substring "world".

# In[19]:


a="Hello world"
print(a)


# In[20]:


len(a)


# In[21]:


a[5:11]


# Q-11 Create a variable named "is_student" and assign it a boolean value indicating you are currntly a student or not.

# In[24]:


age=int(input("enter your age"))
if (age<30):
   print("is_student=True")
else:
    print("is_student=False")


# In[ ]:




