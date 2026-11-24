# Project 1: To-Do List Application

# Set up variables
done = False
to_do_list = []


# Prints the current state of the To-Do list
def print_list():
    for number, task in enumerate(to_do_list):
        print(str(number + 1) + ". " + task)


# Print welcome message and options to select from
print("Welcome to the Simple To-Do List Application!")
while done == False:
    print("\nSelect an option (1-4).")
    print("1: Create a new task.")
    print("2: Edit an existing task.")
    print("3: Delete a task.")
    print("4: See the current To-Do List.")
    print("5: Quit the application.")
    choice = int(input("> "))

    # Adds items to the To-Do List
    if choice == 1:
        to_do_list.append(input("Type in the name of the task you want to add: "))
        print("Successfully added!")

    # Edit an existing item in the to-do list
    elif choice == 2:
        if len(to_do_list) == 0:
            print("There are no tasks to edit. Please try again.\n")
        else:
            print_list()
            edit_task_index = (
                    int(input("Type in the number of the task you want to edit: ")) - 1
            )
            new_item = input("Type in the name of the new task: ")
            to_do_list.pop(edit_task_index)
            to_do_list.insert(edit_task_index, new_item)
            print("Successfully edited!")

    # Deletes tasks in the To-Do List
    elif choice == 3:
        print_list()
        to_do_list.pop(
            int(input("Type in the number of the task you want to delete: ")) - 1
        )
        print("Successfully deleted!")
    # Prints the To-Do List
    elif choice == 4:
        print_list()

    # Quits the application
    elif choice == 5:
        done = True
print("Goodbye!")