
import task_datas as td

def add_task():
    description = input("enter the task description:")

    if description.strip() == " ":
        print(" task description cannot be empty")
        return 

    task = {
        "ID": td.new_ID,
        "description": description,
        "status": "Pending"   
    }

    td.dailytask.append(task)
    td.new_ID += 1

    print("task added successfully")

def view_tasks():
    if len(td.dailytask) == 0:
        print("no taskes exits")
        return

    for task in td.dailytask:
         print("\nID:", task["ID"])
         print("Task:", task["description"])
         print("Status:", task["status"])

def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))

        for task in td.dailytask:
            if task["ID"] == task_id:
                description = input("Enter new task description: ")

                if description.strip() == "":
                    print("Task description cannot be empty!")
                    return

                task["description"] = description
                print("Task updated successfully!")
                return

        print("Task ID not found!")

    except ValueError:
        print("Enter a valid numeric ID!")


def complete_task():
    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in td.dailytask:
            if task["ID"] == task_id:
                if task["status"] == "Pending":
                    task["status"] = "Completed"
                    print("Task marked as completed!")
                else:
                    print("Task is already completed!")
                return

        print("Task ID not found!")

    except ValueError:
        print("Enter a valid numeric ID!")


def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in td.dailytask:
            if task["ID"] == task_id:
                td.dailytask.remove(task)
                print("Task deleted successfully!")
                return

        print("Task ID not found!")

    except ValueError:
        print("Enter a valid numeric ID!")
