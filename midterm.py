
pets = []  # starts empty — the user adds pets as the program runs\

def display_menu():
    # print the menu, return the user's choice
    pass

while True: 
    print("1. Add a pet")
    print("2. View all pet")
    print("3. Counts available vs adopted")
    print("4. Find a pet by name")
    print("5. Exit")

    choice = input("Choose an option [1-5]: ")

    if choice == 1:
        def add_pet(pet_list):
            add_petname = input("Name: ")
            add_petanimaltype = input("Animal Type: ")
            add_petstatus = input("Status: ")
        print(f"{add_petname} - {add_petanimaltype} - {add_petstatus}")
        pass
        pets.append(add_pet)

    elif choice == 2:
        def view_pets(pet_list):
            for view_pets in pet_list:
                print(view_pets)

    elif choice == 3:
        def count_available_adopted(pet_list):
            pass
    # loop through, count Available vs Adopted, return both

    elif choice == 4:
        def find_pet(pet_list):
            pass
    # ask for a name, search the list, print result or "not found"

    elif choice == 5:
        print("Exit")
    else:
        print()