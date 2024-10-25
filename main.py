# main.py
from todo_list import todo_list_menu, add_task, view_tasks, delete_task, modify_task
from currency_converter import currency_converter
from password_generator import password_generator

def main_menu():
    while True:
        print("\n--- My Daily Tools ---")
        print("1. Todo List")
        print("2. Currency Converter")
        print("3. Password Generator")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            todo_list_operations()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            password_generator()
        elif choice == "4":
            print("Exiting My Daily Tools. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 4.")

def todo_list_operations():
    while True:
        todo_list_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            modify_task()
        elif choice == "5":
            print("Returning to main menu.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()
