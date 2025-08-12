# from sqlalchemy.exc import IntegrityError
import os
from models import Owners, session #Need the Users model to create and search for users
#need the session to add users to our db

def login():
    os.system('cls||clear')
    print("-------------------- Login --------------------")
    email = input("email: ")
    password = input("Password: ")
    
    user = session.query(Owners).where(Owners.email==email).first()
    
    if user and user.password== password:
        print("Successfully logged in")
        print(f"Welcome back {user.name}")
        return user
    else:
        print("login failed")
    input()


def register():
    os.system('cls||clear')
    print("---------- Welcome! Please fill in the following to register: ----------")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("email: ")
    password = input("Password: ")
    try:
        new_owner = Owners(name= name, phone = phone, password = password, email = email)
        session.add(new_owner)
        session.commit()
        print(f"Welcome {name}")
        return new_owner
    # except IntegrityError as e:
    #     print("Username already in use")
    except Exception as e:
        print(f'issue creating this account: {e}')
    input()

