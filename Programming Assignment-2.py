#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.	Write a Python program to convert kilometers to miles?
km=float(input("Enter kilometers to covert into miles"))
miles=km*0.6214
print(km, "Kilometers is equal to",miles)


# In[3]:


#2.	Write a Python program to convert Celsius to Fahrenheit?
celcius=float(input("Enter temperature in celcius to convert into fehrenheit "))
fehrenheit=(celcius*(9/5))+32
print(celcius,"C = ",fehrenheit,"F")


# In[4]:


#3.	Write a Python program to display calendar?
import calendar
year=int(input("Enter year "))
month=int(input("Enter month "))
print(calendar.month(year,month))


# In[7]:


#4.	Write a Python program to solve quadratic equation?
import math
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

d=(b**2)-(4*a*c)
exp1=(-b-math.sqrt(d))/(2*a)
exp2=(+b-math.sqrt(d))/(2*a)
print(exp1,exp2)


# In[ ]:





# In[ ]:




