import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Task number to mark as done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
