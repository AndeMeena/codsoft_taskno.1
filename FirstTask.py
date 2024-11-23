import json
from datetime import datetime

# Class to represent a task
class Task:
    def _init_(self, title, description="", due_date=None, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def _repr_(self):
        status = "✔" if self.completed else "✘"
        return f"{self.title} ({status}) - Due: {self.due_date or 'No due date'}"

# Class to manage the to-do list
class TodoList:
    def _init_(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title, description="", due_date=None):
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task._dict_ for task in self.tasks], f)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return [Task(**task) for task in json.load(f)]
        except FileNotFoundError:
            return []

# Example usage
todo = TodoList()
todo.add_task("Buy groceries", "Milk, Eggs, Bread", "2024-11-23")
todo.list_tasks()