# from sqlalchemy.exc import IntegrityError
from models import Owners, session #Need the Users model to create and search for users
#need the session to add users to our db



#Create Login function
#get email and password from user
#check database for owner with the given email
#if you find an owner, check if the found owners password is the same as the given password
#if so return user
def login():
    print(" ------------ Login ----------- ")
    email = input("email: ")
    password = input("Password: ")
    
    user = session.query(Owners).where(Owners.email==email).first()
    
    if user and user.password== password:
        print("Successfully logged in")
        print(f"Welcome back {user.name}")
        return user
    else:
        print("login failed")



#Create Register function
#get all info required to create an owner from the user
#try and create an Owner from the info (will fail if email is already in user)
#if you succeed return user
#except error and print message
def register():
    print("--------- Welcome! Please fill in the following to register: ----------")
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
    pass

