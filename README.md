# Comic-store_Simple-Py-APP
The Comic Book Store application is designed as a simple console-based application

Introduction:
The Comic Book Store application is designed as a simple console-based application that allows users to register, login, and manage their comic book inventory. It uses JSON data stored in a file to save and manage user information and inventory records. The application is structured into functions that handle specific tasks and a main function that serves as the entry point and user interface.

Code Structure and Functions:
2.1 load_data():
This function attempts to open and read the 'data.json' file containing user data. If the file does not exist, it initializes an empty data structure with a 'users' key. The function returns the loaded or initialized data.
def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'users': {}}
    return data
2.2 save_data(data):
This function takes the current data structure and saves it to the 'data.json' file, with a 4-space indentation for readability.
def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

2.3 register_user():
This function prompts the user for a username and password, checks if the username already exists in the data, and, if not, saves the new user's information in the 'data.json' file.
def register_user():
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    data = load_data()
    if username in data['users']:
        print('Username already exists!')
    else:
        data['users'][username] = {'password': password, 'inventory': []}
        save_data(data)
        print('User registered successfully!')
2.4 login_user():
This function prompts the user for their username and password, validates the provided credentials against the data, and returns the username if the login is successful. Otherwise, it returns None.
def login_user():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    data = load_data()
    if username not in data['users'] or data['users'][username]['password'] != password:
        print('Invalid username or password!')
        return None
    else:
        return username
2.5 add_book(username):
This function prompts the user to enter a book title and adds the book to the specified user's inventory in the data.
def add_book(username):
    book = input('Enter the title of the book to add: ')
    data = load_data()
    data['users'][username]['inventory'].append(book)
    save_data(data)
    print(f'{book} added to your inventory!')


2.6 remove_book(username):
This function prompts the user to enter a book title, checks if the book exists in the user's inventory, and removes it from the inventory if found.
def remove_book(username):
    book = input('Enter the title of the book to remove: ')
    data = load_data()
    if book not in data['users'][username]['inventory']:
        print(f'{book} is not in your inventory!')
    else:
        data['users'][username]['inventory'].remove(book)
        save_data(data)
        print(f'{book} removed from your inventory!')

2.7 show_inventory(username):
This function displays the user's inventory by accessing the data for the specified username.
def show_inventory(username):
    data = load_data()
    user_data = data['users'][username]
    if not user_data["inventory"]:
        print("your inventory is empty")
    else:
        print(user_data["inventory"])




Main Function and Application Flow:
3.1 Initial Menu:
The main function starts by welcoming the user to the application and presenting the initial menu with three options: Register, Login, and Exit. The user can choose their desired action by entering the corresponding number.

print('1. Register\n2. Login\n9. Exit')
choice = input('Enter your choice: ')

3.2 User Registration and Login:
If the user chooses to register or login, the relevant function (register_user() or login_user()) is called. In case of successful login, the username is returned, and the application proceeds to the inventory management menu.
if choice == '1':
    register_user()
elif choice == '2':
    username = login_user()

3.3 Inventory Management Menu:
After a successful login, the inventory management menu is presented to the user. They can choose to add a book, remove a book, show their inventory, or log out.
print(f'Welcome, {username}!\n1. Add Book\n2. Remove Book\n3. Show the Inventory\n4. Logout')
choice = input('Enter your choice: ')

3.4 Looping and Exiting:
The application keeps looping through the menus until the user decides to exit by choosing the appropriate option. The main function then terminates, ending the application.
elif choice == '9':
    break

 

