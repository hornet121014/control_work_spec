import service.connect as service
import model.reg_animal as registry
from model.counter import Counter

dict_pets = "Dog", "Cat", "Hamster"
dict_pack_animals = "Horse", "Camel", "Donkey"
dict_type = dict_pets + dict_pack_animals


def display_menu():
    print("\nAnimal Registry Menu:")
    print("1. Add new animal")
    print("2. Show animal commands")
    print("3. Teach new command to animal")
    print("4. Exit")

def run_menu():
    counter = Counter()
    try:
        while True:
            display_menu()
            choice = set_choice()

            if choice == "1":
                animal_type = set_animal_type()
                animal_name = set_animal_name()
                birth_date = set_birth_date()

                try:
                    table_name = registry.get_table(animal_type)
                    kind_id = registry.get_animal_type(animal_type)
                    registry.add_animal(table_name, kind_id, animal_name,"", birth_date)
                    print(f"{animal_name} added to the registry.")
                    counter.add()
                except Exception as e:
                    print("Please fill in all fields to add an animal.\n",e)
                print("Counter value:", counter.count)

            elif choice == "2":
                try:
                    animal_name = set_animal_name()
                    registry.show_commands(animal_name)
                except Exception as e:
                    print("Animal not found!")

            elif choice == "3":
                try:
                    animal_name = set_animal_name()
                    animal_command = set_animal_command()
                    registry.teach_command(animal_name, animal_command)
                except Exception as e:
                    print("Animal not found!")

            elif choice == "4":
                print("Exiting the program...")
                service.logout()
                break

            else:
                print("Invalid choice! Please enter a valid option.")
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise e


def set_choice():
    return input("Enter your choice: ")


def set_animal_type():
    try:
        animal_type = input(f"Enter the type of animal {str(dict_type)}: ")
        result = animal_type.capitalize().strip()
        if result in dict_type:
            return result
    except Exception:
        print("Unknown animal type!")


def set_animal_name():
    return input("Enter the name of the animal: ")


def set_birth_date():
    return input("Enter the birth date of the animal (YYYY-MM-DD): ")


def set_animal_command():
    return input("Enter the new command: ")


