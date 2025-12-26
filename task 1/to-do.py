import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        print("Error reading file.")
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid input.")

def menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()