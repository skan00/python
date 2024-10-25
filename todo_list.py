# todo_list.py
import pickle
import os

# File to store tasks
TASKS_FILE = "tasks.pkl"

# Load tasks from the file if available
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "rb") as file:
            return pickle.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "wb") as file:
        pickle.dump(tasks, file)

# List to store tasks
todo_list = load_tasks()

def todo_list_menu():
    print("\n--- Todo List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Modify Task")
    print("5. Back to Main Menu")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description}
    todo_list.append(task)
    save_tasks(todo_list)
    print("Task added and saved!")

def view_tasks():
    if todo_list:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task['title']} - {task['description']}")
    else:
        print("No tasks found.")

def delete_task():
    view_tasks()
    if todo_list:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            save_tasks(todo_list)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")

def modify_task():
    view_tasks()
    if todo_list:
        task_num = int(input("Enter the task number to modify: "))
        if 1 <= task_num <= len(todo_list):
            task = todo_list[task_num - 1]
            print(f"Modifying Task: {task['title']} - {task['description']}")
            new_title = input("Enter new title (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            if new_title:
                task['title'] = new_title
            if new_description:
                task['description'] = new_description
            save_tasks(todo_list)
            print("Task updated and saved.")
        else:
            print("Invalid task number.")
