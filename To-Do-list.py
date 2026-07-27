import datetime
from datetime import datetime, date

class Todo_list:
    def __init__(self):
        self.mylist = []


# Add new task to do:

    def add_task(self):
        task = input("Task to enter: ")
        due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
        if due == "":
            due = None
        self.mylist.append({"task": task, "status": "pending", "due": due})
        print("new task added\n")

# To view To-do tasks:
    def view_task(self):
        print("your todo list")
        if not self.mylist:
            print("no task")
        else:
            for index, task in enumerate(self.mylist, 1):
                due = task.get("due") if isinstance(task, dict) else None
                due = f" (due: {due})" if due else ""
                print(f"{index}: {task['task']} - {task['status']} - {task['due']}")
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
            due = task.get("due") if isinstance(task, dict) else None
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

