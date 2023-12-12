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
    print('Thank you for using the program. However, your mother.')
    
def contacts_menu():
    #sdfksdhfksjdhfkhfsdfdkhf
    print('')
    
def contacts_add():
    #fwejoierwji
    another = 'y'
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
    print('\nYour Mother')
    
def contacts_search():
    #ji
    print()
    
def contacts_edit():
    #uhkjhsdkfjhdskjdsfh
    print()
    
def contacts_delete():
    #r
    print()
    
def contacts_display():
    #POOP FART
    print()
    

    