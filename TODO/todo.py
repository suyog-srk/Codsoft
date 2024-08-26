tasks = []

def addtask():
    while True:
        print("Please enter the task to be added: ")
        addnewtask = input("")
        tasks.append(addnewtask)
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\nDo you want to add another task? (Y/N): ")
        addchoice = input("").upper()
        if addchoice != 'Y':
            break

def deltask():
    while True:
        if not tasks:
            print("No tasks to delete.")
            break
        print("Please select the task to be deleted (by number): ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        n = int(input()) - 1
        if 0 <= n < len(tasks):
            tasks.pop(n)
            print("Task deleted.")
        else:
            print("Invalid selection.")
        print("Do you want to delete another task? (Y/N): ")
        delchoice = input("").upper()
        if delchoice != 'Y':
            break

def modtask():
    while True:
        if not tasks:
            print("No tasks to modify.")
            break
        print("Please select the task to modified (by number): ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        m = int(input()) - 1
        if 0 <= m < len(tasks):
            print("Please enter the modified task: ")
            tasks[m] = input("")
            print("\nTask modified.")
        else:
            print("Invalid input.")
        print("Do you want to modify another task? (Y/N): ")
        updtchoice = input("").upper()
        if updtchoice != 'Y':
            break

def view_tasks():
    if tasks:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")

if __name__ == "__main__":
    while True:
        print("\n\nToDo")
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\n1. Add a new task")
        print("2. Delete a task")
        print("3. Modify a task")
        print("4. View all tasks")
        print("5. Exit")
        print("\nPlease select one of the above options:")
        user = int(input())

        if user == 1:
            addtask()
        elif user == 2:
            deltask()
        elif user == 3:
            modtask()
        elif user == 4:
            view_tasks()
        elif user == 5:
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid input, please try again.")
