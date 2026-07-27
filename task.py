# Define class task
class task:
    def __init__(self, title, due_date, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def display_task(self):
        print(f"Title: {self.title}, Due: {self.due_date}, Completed: {self.completed}")

first = task("Java", "2 July", True)
first.display_task()