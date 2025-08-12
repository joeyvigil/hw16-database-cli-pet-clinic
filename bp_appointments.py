import os
from models import Appointments, Owners, Pets, Vets, session
from datetime import datetime

#IMPORTANT when creating an appointment, it is required to convert the date string
# "YYYY-MM-DD" int a python date object

date_format = "%Y-%m-%d" #This will be used to format your date

#Syntax for date conversion

# new_date = datetime.strptime("Date String", date_format)
#example
today = datetime.strptime("2025-08-11", date_format)


def create_appointment(current_user):
    os.system('cls||clear')
    current_user.display_pets()
    choice = input("Which pet is this appointment for? (name): ")
    pet = session.query(Pets).where(Pets.name == choice, Pets.owner_id == current_user.id).first()
    if pet:
        print(f"Who do you wish to see {pet.name}?")
        all_vets = session.query(Vets).all()
        for vet in all_vets:
            vet.display()
        vet_name = input("Enter Vet Name: ")
        vet = session.query(Vets).where(Vets.name == vet_name).first()
        if vet:
            try:
                appointment_date = input(f"When would you like {pet.name} to see {vet.name}: (YYYY-MM-DD) ")
                notes = input(f"Whats going on with {pet.name}? ")
                date_obj = datetime.strptime(appointment_date,date_format)
                new_apt = Appointments(pet_id= pet.id, veterinarian_id = vet.id, appointment_date =date_obj, notes= notes)
                session.add(new_apt)
                session.commit()
                input(f"{pet.name} is all set to see {vet.name} on {appointment_date}")
            except Exception as e:
                print(e)
        else:
            input("invalid vet name")
    else:
        input("invalid pet name")
    input("Press Enter")
        

def reschedule_appointments(current_user):
    os.system('cls||clear')
    view_appointments(current_user)
    choice = input("select appointment by id: ")
    app = session.get(Appointments,choice)
    if app and app.pet.owner_id == current_user.id:
        try:
            print(" --------------------  -------------------- ")
            app.display()
            new_date = input("what is the new date? YYYY-MM-DD ? ")
            new_date=datetime.strptime(new_date,date_format)
            app.appointment_date=new_date
            session.commit()
            input(f"appointment successfully rescheduled to {new_date}")
        except Exception as e:
            print(e)
    input("Press Enter")
        

def complete_appointment(current_user):
    os.system('cls||clear')
    view_appointments(current_user)
    choice = input("select appointment by id: ")
    app = session.get(Appointments,choice)
    if app and app.pet.owner_id == current_user.id:
        app.status = 'Complete'
        session.commit()
        input("successfully complete appointment")


def view_appointments(current_user):
    os.system('cls||clear')
    for pet in current_user.pets:
        print(f"\n-------------------- {pet.name}'s appointments --------------------")
        for appoint in pet.appointments:
            appoint.display()
    input("Press Enter")
