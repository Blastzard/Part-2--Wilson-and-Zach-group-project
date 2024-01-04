
import os
#start of project 2

def contacts_main():
    #accepts no arguments
    #drives the program
    #calls contacts_menu and gets the choice from it
    
    #prime the loop
    choice = int(contacts_menu())
    
    #validate menu choice
   
        
    #loop to call the desired function
    while choice != 5:
        if choice == 1:
                contacts_add()
        elif choice == 2:
                contacts_edit()
        elif choice == 3:
                contacts_delete()
        elif choice == 4:
              contacts_display()
        choice = int(contacts_menu())  
    
    print('Thank you for using the program.')
    
def contacts_menu():
    #sdfksdhfksjdhfkhfsdfdkhf
    
    #display menu
    print('\nWelcome to the Contact Manager!')
    print('1. Add a record')
    print('2. Modify a record')
    print('3. Delete a record')
    print('4. Display all saved records')
    print('5. Exit')
    
    #prompts the user for a choice
    choice = (input('Enter a choice: '))
    
    return choice
    
    
def contacts_add():
    #fwejoierwji
    another = 'y'
    try:
        contacts_file = open('contacts.txt', 'a')
        while another.lower() == 'y':
            print('Enter the following contact data:\n')
            name = input('Name: ')
            street = input('Street address: ')
            phone = input('Phone number: ')
            email = input('Email address: ')
            
            contacts_file.write(name + '\n')
            contacts_file.write(street + '\n')
            contacts_file.write(phone + '\n')
            contacts_file.write(email + '\n')
            
            another = input('\nDo you wish to enter another contact? (y to continue): ')
            
        contacts_file.close()
    except IOerror:
        
def contacts_search():
    #team project
    #accepts no arguments
    #searches for a contact
    contacts_file=open("contacts.txt", "r")
    search=input("What contact would you like to read the info of? ")
    found=False
    name=(contacts_file.readline()).rstrip("\n")
    while name!="":
        street=(contacts_file.readline()).rstrip("\n")
        phone=(contacts_file.readline()).rstrip("\n")
        email=(contacts_file.readline()).rstrip("\n")
        if search.lower() == name.lower():
            print("Name: ", name)
            print("Street Address: ", street)
            print("Phone Number: ", phone)
            print("Email Address: ", email)
            found=True
        name=(contacts_file.readline()).rstrip("\n")
    if found==False:
        print("Contact not found.")
    contacts_file.close()
def contacts_edit():
    #team project
    #accepts no arguments
    #edits a contact
    contacts_file=open("contacts.txt", "r")
    temp_file=open("temp.txt", "w")
    search=input("What contact would you like to edit")
    new_name=input("What is the new name you want to add? ")
    new_street=input("What is the new address you want to add? ")
    new_phone=input("What is the new name you want to add? ")
    new_email=input("What is the new email you want to add? ")
    found=False
    name=(contacts_file.readline()).rstrip("\n")
    while name!="":
        street=(contacts_file.readline()).rstrip("\n")
        phone=(contacts_file.readline()).rstrip("\n")
        email=(contacts_file.readline()).rstrip("\n")
        if search.lower() == name.lower():
            temp_file.write(new_name+"\n")
            temp_file.write(new_street+"\n")
            temp_file.write(new_phone+"\n")
            temp_file.write(new_email+"\n")
            found=True
        else:
            temp_file.write(name+"\n")
            temp_file.write(street+"\n")
            temp_file.write(phone+"\n")
            temp_file.write(email+"\n")
        name=(contacts_file.readline()).rstrip("\n")
    if found==False:
        print("Contact not found.")
    else:
        print("Contact successfully edited.")
    contacts_file.close()
    temp_file.close()
    os.remove("contacts.txt")
    os.rename("temp.txt", "contacts.txt")
def contacts_delete():
    #Team Project
    #accepts no arguments
    #deletes a contact
    contacts_file=open("contacts.txt", "r")
    temp_file=open("temp.txt", "w")
    search=input("What contact would you like to Delete? ")
    found=False
    name=(contacts_file.readline()).rstrip("\n")
    while name!="":
        street=(contacts_file.readline()).rstrip("\n")
        phone=(contacts_file.readline()).rstrip("\n")
        email=(contacts_file.readline()).rstrip("\n")
        if search.lower() != name.lower():
            temp_file.write(name+"\n")
            temp_file.write(street+"\n")
            temp_file.write(phone+"\n")
            temp_file.write(email+"\n")
        else:
            found=True
        name=(contacts_file.readline()).rstrip("\n")
    if found==False:
        print("Contact not found.")
    else:
        print("Contact successfully edited.")
    contacts_file.close()
    temp_file.close()
    os.remove("contacts.txt")
    os.rename("temp.txt", "contacts.txt")
    
def contacts_display():
   
    #open file and read the first desc
    contacts_file = open('contacts.txt', 'r')
    name = contacts_file.readline()
    
    #loop to ead, strip, and output each record
    while name != '':
        
        street = contacts_file.readline()
        phone = contacts_file.readline()
        email = contacts_file.readline()
        
        #strip the newline
        name = name.rstrip('\n')
        street = street.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')
          
        
        print('\n''Name: ', name)
        print('Street Address: ', street)
        print('Phone Number: ', phone)
        print('Email Address: ', email)
        
        #refresh the description
        name = contacts_file.readline()
     
    #close file and notify user 
    contacts_file.close()
    print('\nAll records retrieved.')
