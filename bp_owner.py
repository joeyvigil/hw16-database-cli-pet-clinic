from models import Owners, session

#View profile function
#displays the current users info
def view_owner(current_user):
    current_user.display()
    return current_user


#Update profile function
#displays current user info
#allows user to update any of the fields
#commits changes 
#shows changes and returns update current_user
def update_user(current_user):
    current_user.display()
    print("--------- Fill in desired changes, leave blank to keep: ----------")
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
    print("----- updated info: -----")
    current_user.display()
    return current_user

    
    


#Update profile function
#Ask user to confirm they want to delete
#if so delete the current user from the session
#commits changes 
#call main() to start the program over
def delete_user(current_user):
    choice = input("To confirm type 'delete': ")
    if choice== 'delete':
        session.delete(current_user)
        session.commit()
        return None
    else:
        print("return to menu")