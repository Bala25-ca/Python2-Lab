# Diary Entry Program (File I/O and OS Operations)
# Check if the diary file exists in the current directory, if not create it
import os
def is_diary_file_exists(file_path):
    return os.path.isfile(file_path)
# Output: True or False depending on the existence of the file
print(is_diary_file_exists("diary.txt"))  

# Create a new diary entry and write it to the diary file
def create_file(filename, content):
    with open(filename, 'a') as file:
        print(f"{filename} file created successfully")
        content = str(input("Enter your diary entry: "))
        file.write(content + "\n")

create_file("diary.txt", "content")
def read_file(filename):
    file = open(filename, 'r')
    content = file.read()
    print(content)
read_file("diary.txt")


# Display the current date and time of the diary.txt file
import datetime
now = datetime.datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

