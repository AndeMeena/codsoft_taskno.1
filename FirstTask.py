import json
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, due_date):
        task = {
            "name": name,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{i}. {task['name']} - {task['description']} (Due: {task['due_date']}) [{status}]")

    def update_task(self, index, name=None, description=None, due_date=None, completed=None):
        if 0 <= index < len(self.tasks):
            if name: self.tasks[index]["name"] = name
            if description: self.tasks[index]["description"] = description
            if due_date: self.tasks[index]["due_date"] = due_date
            if completed is not None: self.tasks[index]["completed"] = completed
        else:
            print("Invalid task index!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index!")

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

# Example Usage
if __name__ == "__main__":
    todo = ToDoList()
    todo.load_from_file()

    print("Welcome to the To-Do List!")
    while True:
        print("\nOptions: 1. Add Task  2. View Tasks  3. Update Task  4. Delete Task  5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Task Name: ")
            description = input("Task Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(name, description, due_date)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            index = int(input("Task Number to Update: ")) - 1
            name = input("New Name (or leave blank): ")
            description = input("New Description (or leave blank): ")
            due_date = input("New Due Date (or leave blank): ")
            completed = input("Completed? (yes/no or leave blank): ").lower() == "yes"
            todo.update_task(index, name, description, due_date, completed)
        elif choice == "4":
            index = int(input("Task Number to Delete: ")) - 1
            todo.delete_task(index)
        elif choice == "5":
            todo.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
