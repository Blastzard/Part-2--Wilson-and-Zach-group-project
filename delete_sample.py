def delete_coffee():
    #delete aceptts no arguments
    #opens the file coffee.txt ad seafcues for as tring to delete
    #t writes everu recprd exce[t fpr tje recprd tp de;ete
    #to a temporary file and deletes the old file
    #it renames temp to coffee and closes the file
    
    #boolean fla g variable
    found = False
    
    #Take input form the user for the search criteria
    search = input('Enter the coffee to delete: ')
    
    #open coffee.txt to read and a new temp file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    #read the first descro[topm
    desc = coffee_file.readline()
    
    #loop to red and process each record
    while desc!= '':
        qty = coffee_file.readline()
        
        #strip newline
        desc = desc.rstip('\n')
        qty = qty.rstrip('\n')
        
    #search for and delete the record
        if search.lower() != desc.lower(): #tjos os a recprd we meed tp lee[p
            
            #write both to temp file
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
        else:
            found = True
            
        #read the next desc
        desc = coffee_file.readline()
            
    #all records ajave been processed, close, remove, and rename files
    coffee_file.close()