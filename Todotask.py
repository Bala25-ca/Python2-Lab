import os
import json
from datetime import datetime, date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "datafile.txt")

class Todo_list:
    def __init__(self, datafile=DATA_FILE):
        self.datafile = datafile
        self.mylist = []
        self.load()

    def load(self):
        if not os.path.isfile(self.datafile):
            self.mylist = []
            return
        try:
            with open(self.datafile, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if not content:
                    self.mylist = []
                    return
                try:
                    self.mylist = json.loads(content)
                    if not isinstance(self.mylist, list):
                        raise ValueError("Task file must contain a list.")
                except json.JSONDecodeError:
                    lines = [line.strip() for line in content.splitlines() if line.strip()]
                    self.mylist = [{"task": line, "status": "pending", "due": ""} for line in lines]
        except OSError as error:
            print(f"Failed to load tasks: {error}")
            self.mylist = []

    def save(self):
        try:
            with open(self.datafile, 'w', encoding='utf-8') as file:
                json.dump(self.mylist, file, indent=2)
        except OSError as error:
            print(f"Failed to save tasks: {error}")


# Add new task to do:

    def add_task(self):
        task = input("Task to enter: ").strip()
        if not task:
            print("Task cannot be empty.")
            return
        due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        if due == "":
            due = ""
        self.mylist.append({"task": task, "status": "pending", "due": due})
        self.save()
        print("New task added\n")

# To view To-do tasks:
    def view_task(self):
        print("your todo list")
        if not self.mylist:
            print("no task")
        else:
            today = date.today()
            for index, task in enumerate(self.mylist, 1):
                due = task.get("due", "")
                due_text = ""
                if due:
                    try:
                        due_date = datetime.strptime(due, "%Y-%m-%d").date()
                        delta = (due_date - today).days
                        if delta > 0:
                            due_text = f"due in {delta} days"
                        elif delta == 0:
                            due_text = "due today"
                        else:
                            due_text = f"overdue by {-delta} days"
                    except ValueError:
                        due_text = f"due: {due}"
                status = task.get("status", "pending")
                line_parts = [f"{index}: {task['task']}", status]
                if due_text:
                    line_parts.append(due_text)
                print(" - ".join(line_parts))
        print("\n")

# Function to remove a task:

    def remove_task(self):
        if not self.mylist:
            print("no task to remove\n")
            return
        self.view_task()
        try:
            choice = int(input("Enter task number to remove: "))
            if 1 <= choice <= len(self.mylist):
                removed = self.mylist.pop(choice - 1)
                self.save()
                print(f"Removed task: {removed['task']}\n")
            else:
                print("Invalid task number\n")
        except ValueError:
            print("Invalid input\n")


# Function to mark a task as done:

    def mark_done(self):
        if not self.mylist:
            print("no task\n")
            return
        self.view_task()
        try:
            choice = int(input("Enter task number to mark done: "))
            if 1 <= choice <= len(self.mylist):
                self.mylist[choice - 1]["status"] = "done"
                self.save()
                print("Task marked as done\n")
            else:
                print("Invalid task number\n")
        except ValueError:
            print("Invalid input\n")


# Fucntion to display overdue-tasks using date format

    def is_task_overdue(self):
        """Check stored tasks and print which are overdue."""
        if not self.mylist:
            print("No tasks.")
            return
        today = date.today()
        any_overdue = False
        for i, task in enumerate(self.mylist, 1):
            due = task.get("due", "")
            if not due:
                continue
            try:
                due_date = datetime.strptime(due, "%Y-%m-%d").date()
            except ValueError:
                print(f"Task {i} '{task.get('task', str(task))}': invalid date format '{due}'")
                continue
            if due_date < today:
                print(f"Task {i} - '{task['task']}': OVERDUE (due {due})")               
                any_overdue = True            
        if not any_overdue:
            print("No overdue tasks.")
    


# Function to display choice_menu:
def menu():
    todo = Todo_list()
    while True:
        print("***Main Menu***")
        print("1. Add task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Mark task as done")
        print("5. Overdue_tasks")
        print("6. Quit")

        choice = input("Enter choice from menu: ")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_task()
        elif choice == "3":
            todo.remove_task()
        elif choice == "4":
            todo.mark_done()
        elif choice == '5':
            todo.is_task_overdue()
        elif choice == "6":
            exit()
        else:
            print("Enter valid choice")

# calling menu function
menu()