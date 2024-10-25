# main.py
from todo_list import add_task, view_tasks, delete_task, todo_list_menu
from currency_converter import currency_converter
from password_generator import password_generator

def display_menu():
    print("\nMyDailyTools - Select a Program")
    print("1. Todo List")
    print("2. Currency Converter")
    print("3. Password Generator")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                todo_list_menu()
                todo_choice = input("Enter your choice: ")
                if todo_choice == "1":
                    add_task()
                elif todo_choice == "2":
                    view_tasks()
                elif todo_choice == "3":
                    delete_task()
                elif todo_choice == "4":
                    break
                else:
                    print("Invalid option. Please try again.")
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            password_generator()
        elif choice == "4":
            print("Exiting MyDailyTools. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
