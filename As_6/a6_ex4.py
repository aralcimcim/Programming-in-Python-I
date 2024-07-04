# K11720457
# Aral Cimcim

# Write the functions create_user, login, change_password.

import os
from  datetime import datetime
import pickle

def create_user(name: str, data: str, password:str, log_file = 'logs.txt'):

    file_name = f"{name}.pkl"

    if os.path.exists(file_name):
        with open(log_file, "a") as file:
            file.write(f"Attempted creation of existing user {name} at {datetime.now()}\n")

    else:
        user_credentials = {"name": name, "data": data, "password": password, "last_changed": datetime.now()}
        
        with open(file_name, "wb") as file:
            pickle.dump(user_credentials, file)

        with open(log_file, "a") as file:
            file.write(f"Created user {name} at {datetime.now()}\n")

        
def login(name: str, password: str, log_file = 'logs.txt'):

    file_name = f"{name}.pkl"
    
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            user_credentials = pickle.load(file)

        with open(log_file, "a") as file:
            file.write(f"Attempted login for user {name} at {datetime.now()}\n")
        
        if user_credentials["password"] == password:
            with open(log_file, "a") as file:
                file.write(f"Login successful for user {name} at {datetime.now()}\n")
            
        else:
            with open(log_file, "a") as file:
                file.write(f"Login failed for user {name} at {datetime.now()}\n")
    
    else:
        with open(log_file, "a") as file:
            file.write(f"Attempted login for non-existing user {name} at {datetime.now()}\n")
    
    return None


def change_password(name: str, old_password: str, new_password: str, log_file = 'logs.txt'):

    file_name = f"{name}.pkl"
    
    with open(log_file, "a") as file:
        file.write(f"Attempted password change for user {name} at {datetime.now()}\n")
    
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            user_credentials = pickle.load(file)
        
        if user_credentials["password"] == old_password:
            user_credentials["password"] == new_password
            user_credentials["last_changed"] == datetime.now()

            with open(file_name, "wb") as file:
                pickle.dump(user_credentials, file)

            with open(log_file, "a") as file:
                file.write(f"Password change successful for user {name} at {datetime.now()}\n")
        
        else:
            with open(log_file, "a") as file:
                file.write(f"Password change failed for user {name} at {datetime.now()}\n")

