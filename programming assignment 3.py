#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# In[9]:


#2.	Write a Python Program to Check if a Number is Odd or Even?

num=int(input("Enter a number"))
if num%2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# In[12]:


#3.	Write a Python Program to Check Leap Year?

year=int(input("Enter year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


# In[17]:


#4.	Write a Python Program to Check Prime Number?
num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# In[18]:


#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




