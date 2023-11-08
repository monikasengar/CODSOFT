#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
num= int(input("Enter number of times you want to calculate:"))

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
def exit():
    ch = str(input("Are you sure to exit(y/n)"))
    if ch == 'y':
        sys.exit()
    if ch == 'n':
        select = int(input("Select operation"))

count= 0
while(count<num):
    count= count + 1
    print("Please select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n"
          "5. Exit\n")

    # Taking input from the user
    select = int(input("Select operations form 1, 2, 3, 4 :"))

    
    if select == 1:
                  number_1 = int(input("Enter first number: "))
                  number_2 = int(input("Enter second number: "))  
                  print(number_1, "+", number_2, "=",
                             add(number_1, number_2))

    elif select == 2:
                  number_1 = int(input("Enter first number: "))
                  number_2 = int(input("Enter second number: "))  
                  print(number_1, "-", number_2, "=",
                            subtract(number_1, number_2))

    elif select == 3:
                  number_1 = int(input("Enter first number: "))
                  number_2 = int(input("Enter second number: "))  
                  print(number_1, "*", number_2, "=",
                           multiply(number_1, number_2))

    elif select == 4:
                   number_1 = int(input("Enter first number: "))
                   number_2 = int(input("Enter second number: ")) 
                   print(number_1, "/", number_2, "=",
                          divide(number_1, number_2))
    elif select == 5:
                   exit()
    
    else:
                    print("Invalid input")
                    select = int(input("Enter valid input"))


# In[ ]:




