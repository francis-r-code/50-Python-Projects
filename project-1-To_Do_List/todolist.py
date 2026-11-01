#Project 1: To-Do List Application

done = False
toDoList = []

def printList():
    for number, task in enumerate(toDoList):
        print(str(number + 1) + ". " + task)

print("Welcome to the Simple To-Do List Application!")

while done == False:
    print("\nSelect an option (1-4).")
    print("1: Create a new task.")
    print("2: Edit an existing task.")
    print("3: Delete a task.")
    print("4: See the current To-Do List.")
    print("5: Quit the application.")
    choice = int(input("> "))

    if choice == 1:
        toDoList.append(input("Type in the name of the task you want to add: "))
        print("Successfully added!")

    elif choice == 2:
        if len(toDoList) == 0:
            print("There are no tasks to edit. Please try again.\n")
        else:
            printList()
            editTaskIndex = (
                int(input("Type in the number of the task you want to edit: ")) - 1
            )
            newItem = input("Type in the name of the new task: ")
            toDoList.pop(editTaskIndex)
            toDoList.insert(editTaskIndex, newItem)
            print("Successfully edited!")

    elif choice == 3:
        printList()
        toDoList.pop(
            int(input("Type in the number of the task you want to delete: ")) - 1
        )
        print("Successfully deleted!")

    elif choice == 4:
        printList()

    elif choice == 5:
        done = True

print("Goodbye!")
