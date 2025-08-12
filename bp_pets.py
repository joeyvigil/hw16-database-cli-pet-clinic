from models import Pets, session, Owners

#view pets function
#Takes in current user
#Loops over all of the current users pets (use the .pets relationship attribute to get list of pets)
#prints the pets info
def view_pets(current_user):
    current_user.display_pets()


#Create pets function
#gets pets info from user
#create Pets() from the info
#print new pet
def create_pet(current_user):
    name = input("pet name: ")
    species = input("species: ")
    breed = input('breed: ')
    age = input("age: ")
    new_pet=Pets(name=name, species=species, breed= breed, age = age, owner_id = current_user.id)
    session.add(new_pet)
    session.commit()
    print("Pet profile successfully created")


#Update pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#get updated info from the user
#set that pets info to the new info
#commit changes
#print new pet info
def update_pets(current_user):
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
        


#Delete pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#Ask user if they are sure they want to delete this pet
#delete pet from the session
#commit changes
def delete_pet(current_user):
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




