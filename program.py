# Helen Le / 11-01-25 / program allowing users to login (and then view accounts), register a new account or exit the program
import sys

# Simple menu system 
while True:
    print ('Please select one of these options: (l)ogin, (r)egister, (q)uit')
    selection = input()

# Log in  > View accounts (Component 2 & 3)
    if selection == 'l':
        print('Login to your existing account by following the below prompts.')
        # Prompting the user to enter in existing username
        while True: 
            existing_username = input('Please enter your username: ')

            # Field validation for username
            while len(existing_username) < 1:
                print('Please enter a username, this is a mandatory field.')
                existing_username = input('Please enter your username: ')

            # Prompting the user to enter in existing password
            existing_password = input('Please enter your password: ')

            # Field validation for password
            while len(existing_password) < 1:
                print('Please enter a password, this is a mandatory field.')
                existing_password = input('Please enter your password: ')

            # Opening accounts.txt and checking if the inputted username and password already exists
            login_successful = False # defining the variable while assuming login is unsuccessful
            with open('accounts.txt', 'r') as accounts:
                for acc in accounts:
                    strip_acc = acc.strip()
                    if str(existing_username + ',' + existing_password) == strip_acc:
                        login_successful = True
                        break
            # Letting user know if login is successful or not     
            if login_successful == True:
                print('Login successful.')
                print('Welcome to your account. Please select one of these options: (v)iew accounts, (q)uit')
                selection = input()

                if selection == 'v':
                    # Open the file and read lines
                    with open('accounts.txt', 'r') as accounts:
                        lines = accounts.readlines()

                    # Extract usernames and print each username in a numbered list
                    count = 0
                    for i, line in enumerate(lines, start=1):
                        username = line.strip().split(",")[0].strip("['")  # trimming spaces, removing brackets and extracting username
                        print(f"{i}. {username}")
                        count += 1
                    print('Total users = '+ str(count))
                    break # breaking the infinite loop so it won't prompt the user to enter their username & password when login is successful

                elif selection == 'q':
                    sys.exit()

            else: #if login_successful = False
                    print('Login unsuccessful, please ensure your username and password is valid and try again.')
                    break
    
 # Register (Component 1)
    elif selection == 'r':
        # Prompting the user to create a username
        print('Create a user account with us by following the below prompts.')
        new_username = input('Please create a username: ')

        # Field validation for username
        while len(new_username) < 1:
            print('Please enter a username, this is a mandatory field.')
            new_username = input('Please create a username: ')

        # Prompting the user to create a password
        new_password = input('Please create a password: ')

        # Field validation for password
        while len(new_password) < 10:
            print('Please ensure your password has a minimum of 10 characters.')
            new_password = input('Please create a password: ')
        else:
            print('User account creation successful.')
        #appending into accounts.txt
            creating_user_acc = open('accounts.txt', 'a')
            creating_user_acc.write('\n'+ new_username + ',' + new_password)
            creating_user_acc.close()

# Exit
    elif selection == 'q':
        sys.exit()