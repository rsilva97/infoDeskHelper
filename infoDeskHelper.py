import os

def addContact(dictionary):
    outputFile = open('extensions.txt', 'a') # opens file for writing (append)
    os.system('cls') # clears the prompt
    contact = input('Type the name of the new contact: ') # asks for a contact name
    extension = input('Type this contact\'s extension: ') # asks for the contact's extension
    outputFile.write(contact + '_' + extension + '\n') # adds the contact's information to the file
    outputFile.close() # closes the file
    dictionary[contact] = extension # creates an instance of the new contact in the extensions dictionary
    proceed = input('New contact created. Press Enter to continue. ') # prints a message confirming the creation of the new contact

def main():
    inputFile = open('extensions.txt', 'r') # opens file for reading
    inputFile.readline() # skips first line
    extensionsDict = {} # creates a dictionary that will store the extensions
    for line in inputFile: # for every remaining line in the file...
        line = line.strip() # removes '\n' from line
        extensionsDict[line.split('_')[0]] = line.split('_')[1] # adds contact as key and extension as value to the extensions dictionary
    inputFile.close() # closes the input file

    running = True # creates a variable that keeps the main loop running
    while running:
        os.system('cls') # clears the prompt
        userInput = input('Who are you looking for? ') # asks the user for a contact name
        if userInput.lower() == 'add': # in case the user wants to add a new contact...
            addContact(extensionsDict) # calls the function addContact
        elif userInput.lower() == 'exit': # in case the user wants to exit the program...
            running = False # changes the variable value and stops the loop
        else:
            matchList = []
            if len(userInput) == 0: # displays the entire list to the user
                for key in extensionsDict:
                    if userInput.lower() in key.lower():
                        matchList.append(key)  
            elif userInput[0] == '*': # displays all contact names that start with a specific letter
                for key in extensionsDict:
                    if key[0].lower() == userInput[1].lower():
                        matchList.append(key)
            else:
                for key in extensionsDict: # displays all contact names that contain the input provided by the user
                    if userInput.lower() in key.lower():
                        matchList.append(key)       
            if len(matchList) != 0:
                os.system('cls') # clears the prompt
                print('Here are the results that match your search: ' + userInput + '\n')
                for item in matchList: # displays all matches found to the user
                    print(item + ': ' + extensionsDict[item])
                proceed = input('\nPress Enter to proceed. ')
                if proceed.lower() == 'exit': # in case the user wants to exit the program...
                    running = False # changes the variable value and stops the loop
            else:
                newContact = input('\nNo matches found. Type "add" to add a new contact or press Enter to proceed. ')
                if newContact.lower() == 'add': # in case the user wants to add a new contact...
                    addContact(extensionsDict) # calls the function addContact
                elif newContact.lower() == 'exit': # in case the user wants to exit the program...
                    running = False # changes the variable value and stops the loop

main()
