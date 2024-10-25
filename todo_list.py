# todo_list.py

# In-memory list to store tasks
todo_list = []

def todo_list_menu():
    print("\n--- Todo List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Back to Main Menu")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added!")

def view_tasks():
    if todo_list:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def delete_task():
    view_tasks()
    if todo_list:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
