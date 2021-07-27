#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1.	Write a Python Program to Find LCM?

def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second  number"))

print("The L.C.M. is", compute_lcm(num1, num2))


# In[4]:


#2.	Write a Python Program to Find HCF?
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second number"))

print("The H.C.F. is", compute_hcf(num1, num2))


# In[6]:


#3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

dec = int(input("Enter a decimal number"))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[12]:


#4.	Write a Python Program To Find ASCII value of a character?
c = input("Enter a character")
print("The ASCII value of '" + c + "' is", ord(c))


# In[14]:


#5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?


# Addition
def add(x, y):
    return x + y

#Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")


# In[ ]:




