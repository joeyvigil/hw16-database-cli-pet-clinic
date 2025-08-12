#DONT FORGET TO IMPORT FUNCTIONS AFTER YOU MAKE THEM
from bp_appointments import complete_appointment, create_appointment, reschedule_appointments, view_appointments
from bp_auth import login, register
from bp_owner import delete_user, update_user, view_owner
from bp_pets import create_pet, delete_pet, update_pets, view_pets
from models import Owners, session


def welcome_menu():
    current_user = None
    
    while True:
        print("""
--------- Welcome to Pet Clinic --------
        1.) Login
        2.) Register
""")
        choice = input("select (1 or 2) or quit: ")
        if choice == '1':
            current_user= login()
            if current_user:
                return current_user

        elif choice == '2':
            current_user= register()
            if current_user:
                return current_user
        
        elif choice == 'quit':
            return
        else:
            print("Invalid response please try again.")

def owner_menu(current_user):
    while True:
        print("""
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back""")
        choice = input("choose 1-3: ")
        if choice == '1':
            current_user = view_owner(current_user)
        elif choice == '2':
            current_user = update_user(current_user)
        elif choice == '3':
            current_user = delete_user(current_user)
            return None
        elif choice == '4':
            return #Goes back to main menu
        else:
            print("Invalid Selection.")

def pets_menu(current_user):
    while True:
        print("""
1.) View my Pets
2.) Create Pet
3.) Update Pet
4.) Delete Pet
5.) Back""")
        choice = input("choose 1-5: ")
        if choice == '1':
            view_pets(current_user)
        elif choice == '2':
            create_pet(current_user)
        elif choice == '3':
            update_pets(current_user)
        elif choice == '4':
            delete_pet(current_user)
        elif choice == '5':
            return
        else:
            print("Invalid Selection.")

def appointments_menu(current_user):
    while True:
        print("""
1.) schedule appointment
2.) view appointments
3.) reschedule appointment
4.) Complete appointment
5.) Back
""")
        choice = input("choose 1-5: ")
        if choice == '1':
            create_appointment(current_user)
        elif choice == '2':
            view_appointments(current_user)
        elif choice == '3':
            reschedule_appointments(current_user)
        elif choice == '4':
            complete_appointment(current_user)
        elif choice =='5':
            return


def main():
    
    current_user = welcome_menu() 
    # current_user = session.get(Owners,2)
    #After you test you login and register functions, it might be more efficient
    #to set current_user to a user in your db so you don't have to log in everytime
    #you want to test something.
    
    if current_user:
        while True:
            print("""
        --------- Pet Clinic --------
        1.) Manage Profile
        2.) My Pets
        3.) My Appointments
        """)
            choice = input("choose 1-3: ")
            if choice == '1':
                owner_menu(current_user)
            elif choice == '2':
                pets_menu(current_user)
            elif choice == '3':
                appointments_menu(current_user)
            else:
                print("Invalid Selection.")
    

main()
    
