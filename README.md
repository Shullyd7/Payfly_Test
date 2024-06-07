# Authentication System

## Overview

This is a simple authentication system implemented in Python. It allows users to register with a username and password, and then login using those credentials. The user data is securely stored in a JSON file, and passwords are hashed using SHA-256 for security.

## Features

- **User Registration:** Allows new users to create an account with a username and password.
- **User Login:** Allows existing users to log in with their credentials.
- **Secure Storage:** User passwords are hashed using SHA-256 before storing them in the JSON file.
- **Basic Error Handling:** Provides feedback for common errors such as duplicate usernames, incorrect passwords, and empty inputs.

## Approach

The system is implemented in a modular and reusable manner with the following main functions:

1. **load_user_data:** Loads user data from a JSON file. If the file does not exist, it returns an empty dictionary.
2. **save_user_data:** Saves user data to a JSON file.
3. **hash_password:** Hashes passwords using SHA-256 to ensure they are stored securely.
4. **register_user:** Registers a new user. It checks if the username already exists, hashes the password, and saves the user data. It also checks for empty inputs.
5. **login_user:** Logs in a user by checking if the username exists and if the hashed password matches the stored hash. It also checks for empty inputs.
6. **main:** Provides a simple menu for user interaction, allowing users to register, login, or exit the program.

## Challenges

### Data Security
Ensuring the security of user data, especially passwords, is crucial. To address this, passwords are hashed using the SHA-256 algorithm before being stored. This way, even if the JSON file is compromised, the actual passwords remain secure.

### File Handling
Handling the JSON file for storing user data involves ensuring that data is correctly loaded and saved, even in cases of concurrent access or unexpected crashes. Proper error handling and checking if the file exists were necessary to make the system robust.

### User Experience
Providing meaningful error messages and prompts enhances user experience. Implementing basic error handling ensures users understand what went wrong and how to correct it (e.g., informing users if a username is already taken, if an incorrect password is entered, or if any input is empty).

## Usage

1. **Run the Script**
    ```sh
    python auth_system.py
    ```

2. **Choose an Option**
    - `1` for user registration
    - `2` for user login
    - `3` to exit

3. **Follow the Prompts**
    - For registration: Enter a username and password. Empty values are not allowed.
    - For login: Enter the registered username and password. Empty values are not allowed.

## Requirements

- Python 3.x
- No additional libraries required (uses built-in modules: `json`, `hashlib`, `os`)

## File Structure

- `auth_system.py`: The main script containing all functionalities.
- `user_data.json`: The JSON file where user credentials are stored (created automatically when the first user registers).

## License

This project is licensed under the MIT License.