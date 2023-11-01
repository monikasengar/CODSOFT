#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import array
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

# combined formulas
digi_alpha = DIGITS + CHARACTERS
ALL_CH = DIGITS + CHARACTERS + SYMBOLS

#getting length input
length = int(input("Enter length:")) 

#complexity choice
print("Select comlexity:\n"\
         "1. only digits\n"\
         "2. only alphabets\n"\
         "3. digits, alphabets\n"\
         "4. complex\n")
complexity= int(input("select complexity:"))


if complexity == 1:
        count = 0
        while (count < length):
            count = count + 1
            print(random.choice(DIGITS), end='')
    
elif complexity == 2:
        count = 0
        while (count < length):
            count = count + 1
            print(random.choice(CHARACTERS), end='')   
    
    
elif complexity == 3:
        count = 0
        while (count < length):
            count = count + 1
            print(random.choice(digi_alpha), end='')   

    
elif complexity == 4:
        count = 0
        while (count < length):
            count = count + 1
            print(random.choice(ALL_CH), end='')   

    

else:
      print("Invalid Input")
    
    
    

