import json

def load_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'users': {}}
    return data

def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

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

def login_user():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    data = load_data()
    if username not in data['users'] or data['users'][username]['password'] != password:
        print('Invalid username or password!')
        return None
    else:
        return username

def add_book(username):
    book = input('Enter the title of the book to add: ')
    data = load_data()
    data['users'][username]['inventory'].append(book)
    save_data(data)
    print(f'{book} added to your inventory!')

def remove_book(username):
    book = input('Enter the title of the book to remove: ')
    data = load_data()
    if book not in data['users'][username]['inventory']:
        print(f'{book} is not in your inventory!')
    else:
        data['users'][username]['inventory'].remove(book)
        save_data(data)
        print(f'{book} removed from your inventory!')

def show_inventory(username) :
    data = load_data()
    user_data = data['users'][username]
    if not user_data["inventory"]:
        print("your inventory is empty")
    else:
        print(user_data["inventory"])


def main():
    print('Welcome to the SHU Comic Book Store!')
    while True:
        print('1. Register\n2. Login\n9. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            register_user()
        elif choice == '2':
            username = login_user()
            if username is not None:
                while True:
                    print(f'Welcome, {username}!\n1. Add Book\n2. Remove Book\n3. Show the Inventory\n4. Logout')
                    choice = input('Enter your choice: ')
                    if choice == '1':
                        add_book(username)
                    elif choice == '2':
                        remove_book(username)
                    elif choice == '3':
                        show_inventory(username)
                    elif choice == '4':
                        break
                    else:
                        print('Invalid choice!')
        elif choice == '9':
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
