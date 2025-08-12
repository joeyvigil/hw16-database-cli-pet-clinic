from models import Appointments, Owners, Pets, Vets, session
from datetime import datetime

#IMPORTANT when creating an appointment, it is required to convert the date string
# "YYYY-MM-DD" int a python date object

date_format = "%Y-%m-%d" #This will be used to format your date

#Syntax for date conversion

# new_date = datetime.strptime("Date String", date_format)
#example
today = datetime.strptime("2025-08-11", date_format)


#Create new appointment
#display pets
#Choose the pet you wish to create an appointment for
#query them out of the db using their name
#display vets
#Choose the vet you with to create an appointment with
#Query them out of the db
#Gather the rest of the info for the appointment
#Convert the date string to python date object
#Create the Appointment() (remind you'll need the pet id and the vet id)
def create_appointment(current_user):
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
            appointment_date = input(f"When would you like {pet.name} to see {vet.name}: (YYYY-MM-DD) ")
            notes = input(f"Whats going on with {pet.name}? ")
            date_obj = datetime.strptime(appointment_date,date_format)
            new_apt = Appointments(pet_id= pet.id, veterinarian_id = vet.id, appointment_date =date_obj, notes= notes)
            session.add(new_apt)
            session.commit()
            print(f"{pet.name} is all set to see {vet.name} on {appointment_date}")
        else:
            print("invalid vet name")
    else:
        print("invalid pet name")
        
        

#Reschedule appointments
#Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
#Select an appointment by id
#ask user for new date
#convert date
#update the appointment date

def reschedule_appointments(current_user):
    view_appointments(current_user)
    choice = input("select appointment by id: ")
    app = session.get(Appointments,choice)
    if app and app.pet.owner_id == current_user.id:
        print("-----------------------")
        app.display()
        new_date = input("what is the new date? YYYY-MM-DD ? ")
        new_date=datetime.strptime(new_date,date_format)
        app.appointment_date=new_date
        session.commit()
        print(f"appointment successfully rescheduled to {new_date}")
        

#Complete appointments
#Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
#query the appointment by id
#change appointment.status to 'complete"
#print success message
def complete_appointment(current_user):
    view_appointments(current_user)
    choice = input("select appointment by id: ")
    app = session.get(Appointments,choice)
    if app and app.pet.owner_id == current_user.id:
        app.status = 'Complete'
        session.commit()
        print("successfully complete appointment")


#View Appointments
def view_appointments(current_user):
    for pet in current_user.pets:
        print(f"========= {pet.name}'s appointments============")
        for appoint in pet.appointments:
            appoint.display()
