# To-Do List App in Python

task = []

def show_task():
    if len(task) == 0:
     print("\n No task yet!")

     while True:
        addChoice = input("\n Do you want to add a task? (y/n): ")
        if addChoice == 'y' or addChoice == 'Y':
            add_task()
        elif addChoice == 'n' or addChoice == 'N':
            print("\n Goodbye!")
            print("\n Your task: ")
            break
        else:
            print("\n Invalid input. Please try again.")

    else:
     print("\n Your task: ")
    for i in range(len(task)):
     print(f"{i+1}. {task[i]}")
    print()


def add_task():

    print("\n Your task: ")
    for i in range(len(task)):
        print(f"{i + 1}. {task[i]}")
    print()

    task.append(input("\n Enter your task: "))
    print("\n Task added successfully!")


def remove_task():
    show_task()
    if len(task) > 0:
       task_no = int(input("\n Enter number of the task to remove: "))
       if 1 <= task_no <= len(task):
            task.remove(task[task_no-1])
            print("\n Task removed successfully!")
            print("\n Your task: ")
            for i in range(len(task)):
                print(f"{i + 1}. {task[i]}")
            print()
       else:
            print("\n Invalid input. Please try again.")

def edit_task():
    print("\n Your task: ")
    for i in range(len(task)):
        print(f"{i + 1}. {task[i]}")
    print()

    if task:
            try:
                task_no = int(input("\n Enter number of task you want to edit: "))
                if 1 <= task_no <= len(task):
                    new_task = input("\n Enter new task: ")
                    task[task_no -1] = new_task
                    print("\n Task edited successfully!")
                    print("\n Your task: ")
                    for i in range(len(task)):
                        print(f"{i + 1}. {task[i]}")
                    print()
                else:
                    print("\n Task not found!")

            except ValueError:
             print("\n Please enter a valid number!")

while True:
    print("\n **********Welcome to To-Do List App*************")
    print("[1] Show Tasks")
    print("[2] Add Task")
    print("[3] Delete Task")
    print("[4] Edit Task")
    print("[5] Exit")

    menuChoice = input("Enter your choice(1-5): ")
    if menuChoice == "1":
        show_task()
    elif menuChoice == "2":
        add_task()
    elif menuChoice == "3":
        remove_task()
    elif menuChoice == "4":
        edit_task()
    elif menuChoice == "5":
        exit()
    else:
        print("\n Please enter a valid choice!")
