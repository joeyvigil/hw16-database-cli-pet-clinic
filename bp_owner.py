import os
from models import Owners, session


def view_owner(current_user):
    os.system('cls||clear')
    current_user.display()
    input()
    return current_user


def update_user(current_user):
    os.system('cls||clear')
    current_user.display()
    print("---------- Fill in desired changes, leave blank to keep: ----------")
    name = input("Name: ")
    phone = input("Phone: ")
    password = input("Password: ")
    if name:
        current_user.name = name
    if phone:
        current_user.phone = phone
    if password:
        current_user.password = password
    session.commit()
    print("-------------------- updated info: --------------------")
    current_user.display()
    input()
    return current_user


def delete_user(current_user):
    os.system('cls||clear')
    choice = input("To confirm type 'delete': ")
    if choice == 'delete':
        session.delete(current_user)
        session.commit()
        print("Account Successfully Deleted")
        return None
    else:
        print("return to menu")
    input()