#!/usr/bin/env python
# coding: utf-8

# # User friendly contact book

# In[ ]:


print("welcome to our contact book")

import sys
 
# initial phonebook function
def initial_phonebook():
    cols = 6
    phone_book = []
    print("\nEnter contact details in the following order (ONLY):" )
    print(" * indicates mandatory fields")
    print("....................................................................")
    temp = []
    for j in range(cols):
                     
            if j == 0:
                  while True:
                    t = input("Enter name*")
                    if t.strip():  # Checking for a non-empty name
                       if t.isalpha():
                          temp.append(t)
                       if t.isdigit():
                          print("invalid input")
                          temp.append(str(input("Enter name:")))
                    
                       break # Exit the loop if a non-empty name is provided
                    else:
                       t = str(input("Name is a mandatory field. Please enter name"))
                       temp.append(t)
                       break
            if j == 1:
                
                 while True:
                    s = input("Enter number*")
                    if s.strip():  # Checking for a non-empty name
                       if s.isdigit():
                          temp.append(s)
                       if s.isalpha():
                          print("invalid input")
                          temp.append(int(input("Enter number:")))
                    
                       break  # Exit the loop if a non-empty name is provided
                    else:
                       s = int(input("Name is a mandatory field. Please enter number"))
                       temp.append(s)
                       break
                
                
               
                 
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                     
            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            
            if j == 4:
                temp.append(
                    str(input("Enter category(Family/Friends/Work/Others): ")))
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None
                     
    phone_book.append(temp)
    # appending a 1-D array temp into a 2-D array phone_book
    print(phone_book) #printing array pb for first time
    return phone_book


#menu function
def menu():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("\                                      \n")
    print("\tMain Menu\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Update contact")
    print("7. Exit phonebook")
    cho = input("Please enter your choice: ")
    while True:
        if cho.strip():  # Checking for a non-empty name
                if cho.isdigit():
                 cho = int(cho)
                else:
                  if cho.isalpha():
                   cho = int(input("enter integer choice"))
                if cho in arr:
                  return cho
                else:
                  while True:
                    
                     print("Enter choice from menu")
                     cho = int(float(str(input("enter correct choice"))))
                     return cho
                  else:
                     menu()
                     
                
                
                break  # Exit the loop if a non-empty name is provided
        else:
               cho = int(input("Blank space! Please enter choice"))
               if cho in arr:
                     return cho
               else:
                     menu()
               break
        
    return cho


#function to add a contact
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            while True:      
                    t = input("Enter name*")
                    if t.strip():  # Checking for a non-empty name
                       if t.isalpha():
                          dip.append(t)
                       if t.isdigit():
                          print("invalid input")
                          dip.append(str(input("Enter name:")))
                    
                       break  # Exit the loop if a non-empty name is provided
                    else:
                       t = str(input("Name is a mandatory field. Please enter name"))
                       dip.append(t)
                       break
          
            
        if i == 1:
             while True:
                    s = input("Enter number*")
                    if s.strip():  # Checking for a non-empty name
                       if s.isdigit():
                          dip.append(s)
                       if s.isalpha():
                          print("invalid input")
                          dip.append(int(input("Enter number:")))
                    
                       break  # Exit the loop if a non-empty name is provided
                    else:
                       s = int(input("Name is a mandatory field. Please enter number"))
                       dip.append(s)
                       break
             
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
            if dip[i] == '' or dip[i] == ' ':
                    dip[i] = None
        
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
            if dip[i] == '' or dip[i] == ' ':
                    dip[i] = None
        
        if i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others): ")))
            if dip[i] == '' or dip[i] == ' ':
                    dip[i] = None
    print(dip)
    pb.append(dip)
    return pb 

#function to remove a contact
def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            # The pop function removes entry at index i
            print("This contact has now been removed")
            return pb
    
    if temp == 0:
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")
         
        return pb

#function to delete all contacts
def delete_all(pb):
    k = str(input("Are you sure, you want to delete all(yes/no)"))
    if k == 'yes':
      return pb.clear()
      print("All contacts deleted")
    if k == 'no':
       menu()
    

#function to search existing contact
def search_existing(pb):
    choice = int(input("Enter search criteria\n\n\
    1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\
    \nPlease enter: "))
   
    temp = []
    check = -1
     
    if choice == 1:
    # This will execute for searches based on contact name
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 2:
    # This will execute for searches based on contact number
        query = int(
            input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 3:
    # This will execute for searches based on contact's e-mail address
        query = str(input("Please enter the e-mail ID\
        of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 4:
    # This will execute for searches based on contact''s date of birth
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)\
            of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 5:
    # This will execute for searches based on contact category
        query = str(
            input("Please enter the category of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
        # All contacts under query category will be shown using this feature
         
    else:
        print("Invalid search criteria")
        return -1
    if check == -1:
        return -1
        # returning -1 indicates that the query did not exist in the directory
    else:
        display_all(temp)
        return check
       
#function to update a contact        
def update_contact(pb):
    namee = str(input("Enter the name of contact you want to update:"))
    for i in range(len(pb)):
        if namee == pb[i][0]:
                check = i
            
                pb[check][1]= int(input("Enter new number:"))
                pb[check][2]= str(input("Enter new email:" ))
                pb[check][3]= str(input("Enter new date of birth"))
                pb[check][4]= str(input("Enter new category-Family/Friends/Work/Others"))
    print("Contact updated")
    return pb
      
# displays all function
def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])


#exit function           
def thanks():
    k = str(input("Are you sure, you want to exit(yes/no)"))
    if k == 'yes'or k == 'y':
      print("Thank you for using our contact book")
      sys.exit("Goodbye, have a nice day ahead!")
    
    if k == 'no' or k == 'n':
       menu()
    
   
    
ch = 2
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5, 6, 7):
    ch = menu() #assigning cho value to ch
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    elif ch == 6:
        update_contact(pb)
    elif ch == 7:
        thanks()
    else:
        menu()




# In[ ]:




