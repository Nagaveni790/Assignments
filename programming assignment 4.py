#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1.	Write a Python Program to Find the Factorial of a Number?
num=int(input("Enter a number"))
factorial=1
if num<0:
    print("Sorry! Factorial doesnot exists on negetive number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial of",num,"is",factorial)
    


# In[15]:


#2.	Write a Python Program to Display the multiplication Table?
num=int(input("Enter a number to display multiplication table of it"))
for i in range(1,11):
    print(num,"x", i, "=",num*i)


# In[20]:


#3.	Write a Python Program to Print the Fibonacci sequence?

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[23]:


#4.	Write a Python Program to Check Armstrong Number?
num = int(input("Enter a number: "))


sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[27]:


#5.	Write a Python Program to Find Armstrong Number in an Interval?
lower = int(input("Enter a lower interval"))
upper = int(input("Enter an upper interval"))

for num in range(lower, upper + 1):

   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[35]:


#6.	Write a Python Program to Find the Sum of Natural Numbers?


num=int(input("Enter a number"))
if num < 0:
    print("enter a positive number")
else:
    sum = 0
    while(num > 0):
        
        sum += num
        num-=1
    print("Sum is",sum)


# In[ ]:




