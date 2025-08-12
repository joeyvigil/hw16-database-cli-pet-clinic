import os
from models import Pets, session, Owners


def view_pets(current_user):
    os.system('cls||clear')
    current_user.display_pets()
    a=input("Press Enter")


def create_pet(current_user):
    os.system('cls||clear')
    print("-------------------- Enter Pet Info --------------------")
    name = input("pet name: ")
    species = input("species: ")
    breed = input('breed: ')
    age = input("age: ")
    new_pet=Pets(name=name, species=species, breed= breed, age = age, owner_id = current_user.id)
    session.add(new_pet)
    session.commit()
    print("Pet profile successfully created")
    input("Press Enter")


def update_pets(current_user):
    os.system('cls||clear')
    current_user.display_pets()
    choice = input("Enter name of pet you want to update: ")
    pet = session.query(Pets).where(Pets.name == choice, Pets.owner_id == current_user.id).first()
    if pet :
        print("To keep information, leave fields blank")
        name = input("pet name: ")
        species = input("species: ")
        breed = input('breed: ')
        age = input("age: ")
        if name:
            pet.name = name
        if species:
            pet.species = species
        if breed:
            pet.breed = breed
        if age:
            pet.age = age # type: ignore
        session.commit()
        print("Pet profile updated created")
    else:
        print("invalid pet selection")
    input("Press Enter")
        

def delete_pet(current_user):
    os.system('cls||clear')
    current_user.display_pets()
    choice = input("Enter name of pet you want to delete: ")
    pet = session.query(Pets).where(Pets.name == choice, Pets.owner_id == current_user.id).first()
    if pet:
        confirm = input("Enter 'delete' to confirm: ")
        if confirm == 'delete':
            session.delete(pet)
            session.commit()
            print("successfully deleted pet")
    else:
        print("invalid pet option")
    input("Press Enter")




