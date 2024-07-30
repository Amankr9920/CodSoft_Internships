# todo_list.py

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please select from the menu options.")

if __name__ == "__main__":
    main()
