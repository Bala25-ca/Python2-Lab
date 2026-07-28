# Diary Entry Program (File I/O and OS Operations)
# Check if the diary file exists in the same directory as this script,
# and create or update it from there.

import os
import datetime
import Todotask

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "datafile.txt")

class Todo_list:
    def __init__(self, tasks=None):
        self.tasks = list(tasks) if tasks else []

    def add_task(self, task):
        if not isinstance(task, str):
            raise TypeError("Task must be a string.")
        task_text = task.strip()
        if not task_text:
            raise ValueError("Task cannot be empty.")
        self.tasks.append(task_text)
        return task_text

    def remove_task(self, index):
        if not isinstance(index, int):
            raise TypeError("Task index must be an integer.")
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        return self.tasks.pop(index)

    def list_tasks(self):
        return list(self.tasks)

    def save(self, datafile):
        with open(datafile, 'w', encoding='utf-8') as file:
            if self.tasks:
                file.write("\n".join(self.tasks) + "\n")
            else:
                file.write("")

    def load(self, datafile):
        self.tasks = []
        if not os.path.isfile(datafile):
            return
        with open(datafile, 'r', encoding='utf-8') as file:
            self.tasks = [line.rstrip("\n") for line in file if line.rstrip("\n")]


def is_file_exists(file_path):
    return os.path.isfile(file_path)


def create_file(datafile=DATA_FILE, content=None):
    if content is None:
        raise ValueError("Content is required.")
    todo = Todo_list()
    todo.load(datafile)
    todo.add_task(content)
    todo.save(datafile)
    print(f"{os.path.abspath(datafile)} updated successfully")


def read_file(file_path=DATA_FILE):
    todo = Todo_list()
    todo.load(file_path)
    content = todo.list_tasks()
    print("\n".join(content))
    return content


if __name__ == "__main__":
    print(is_file_exists(DATA_FILE))
    create_file(content="content")
    read_file()
    now = datetime.datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

