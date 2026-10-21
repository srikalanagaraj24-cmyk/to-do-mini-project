
import dailytask_management as tm

while True:

    print("\n===== TODO APPLICATION =====")
    print("1. Add Task to the to-do list")
    print("2. View Tasks of the to-do list")
    print("3. Update Task in the to-do list")
    print("4. Mark Task as Completed")
    print("5. Delete Task from the to-do list")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            tm.add_task()

        elif choice == 2:
            tm.view_tasks()

        elif choice == 3:
            tm.update_task()

        elif choice == 4:
            tm.complete_task()

        elif choice == 5:
            tm.delete_task()

        elif choice == 6:
            print("Thank you for using TODO Application!")
            break

        else:
            print("Invalid choice! Enter a number from 1 to 6.")

    except ValueError:
        print("Invalid input! Please enter a number.")