import json
import hashlib
import os

#JSON file where user data will be stored
USER_DATA_FILE = 'user_data.json'


def load_user_data():
    """Load user data from the JSON file."""
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)


def save_user_data(user_data):
    """Save user data to the JSON file."""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)


def hash_password(password):
    """Hash a password"""
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    """Register a new user with a username and password."""
    if not username or not password:
        print("Error: Username and password cannot be empty.")
        return

    user_data = load_user_data()

    if username in user_data:
        print("Error: Username already exists. Please choose a different username.")
        return

    hashed_password = hash_password(password)
    user_data[username] = hashed_password
    save_user_data(user_data)
    print("User registered successfully!")


def login_user(username, password):
    """Login a user with a username and password."""
    if not username or not password:
        print("Error: Username and password cannot be empty.")
        return

    user_data = load_user_data()

    if username not in user_data:
        print("Error: Username does not exist.")
        return

    hashed_password = hash_password(password)
    if user_data[username] == hashed_password:
        print("Login successful!")
    else:
        print("Error: Incorrect password.")


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()