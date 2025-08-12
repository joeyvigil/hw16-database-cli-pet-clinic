#DONT FORGET TO IMPORT FUNCTIONS AFTER YOU MAKE THEM
from bp_appointments import complete_appointment, create_appointment, reschedule_appointments, view_appointments
from bp_auth import login, register
from bp_owner import delete_user, update_user, view_owner
from bp_pets import create_pet, delete_pet, update_pets, view_pets
from models import Owners, session
import os


def welcome_menu():
    current_user = None
    
    while True:
        os.system('cls||clear')
        print("""-------------------- Welcome to Pet Clinic --------------------
    1.) Login
    2.) Register
    3.) Exit
        """)
        choice = input("Choose 1-3: ")
        if choice == '1':
            current_user= login()
            if current_user:
                return current_user

        elif choice == '2':
            current_user= register()
            if current_user:
                return current_user
        
        elif choice == '3':
            return
        else:
            print("Invalid response please try again.")

def owner_menu(current_user):
    while True:
        os.system('cls||clear')
        print("""-------------------- User Profile Menu -------------------- 
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back
    """)
        choice = input("Choose 1-3: ")
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
        os.system('cls||clear')
        print("""-------------------- Pets Menu -------------------- 
    1.) View my Pets
    2.) Create Pet
    3.) Update Pet
    4.) Delete Pet
    5.) Back
        """)
        choice = input("Choose 1-5: ")
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
        os.system('cls||clear')
        print("""-------------------- Appointments Menu -------------------- 
    1.) Schedule Appointment
    2.) View Appointments
    3.) Reschedule Appointment
    4.) Complete Appointment
    5.) Back
        """)
        choice = input("Choose 1-5: ")
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
    
    if current_user:
        while True:
            os.system('cls||clear')
            print("""-------------------- Main Menu --------------------
    1.) Manage Profile
    2.) My Pets
    3.) My Appointments
    4.) Exit 
            """)
            choice = input("Choose 1-4: ")
            if choice == '1':
                owner_menu(current_user)
            elif choice == '2':
                pets_menu(current_user)
            elif choice == '3':
                appointments_menu(current_user)
            elif choice == '4':
                return
            else:
                print("Invalid Selection.")
    

main()
    
