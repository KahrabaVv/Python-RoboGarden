import os

def add_task(task_list, task):
    """Adds a new task to the list."""
    task_list.append(task)
    print(f"Task '{task}' added successfully.")


def remove_task(task_list, task):
    """Removes a task from the list."""
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found in the list.")


def view_tasks(task_list):
    """Displays the current task list."""
    if not task_list:
        print("Your task list is empty.")
    else:
        print("\n--- Current Task List ---")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
        print("--------------------------")


def save_tasks_to_file(file_name, task_list):
    """Saves the current task list to a file."""
    try:
        with open(file_name, "w") as file:
            for task in task_list:
                file.write(task + "\n")
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks to file: {e}")


def load_tasks_from_file(file_name):
    """Loads tasks from a file into the task list."""
    if not os.path.exists(file_name):
        print("Task file not found. Starting with an empty task list.")
        return []

    try:
        with open(file_name, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        print("Tasks loaded successfully.")
        return tasks
    except Exception as e:
        print(f"Error loading tasks from file: {e}")
        return []


def main():
    """Main function to manage the task list."""
    file_name = "tasks.txt"
    task_list = load_tasks_from_file(file_name)

    while True:
        print("\n--- Task List Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            task = input("Enter the task to add: ").strip()
            add_task(task_list, task)

        elif choice == "2":
            task = input("Enter the task to remove: ").strip()
            remove_task(task_list, task)

        elif choice == "3":
            view_tasks(task_list)

        elif choice == "4":
            save_tasks_to_file(file_name, task_list)

        elif choice == "5":
            save_tasks_to_file(file_name, task_list)
            print("Exiting Task List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-5).")


if __name__ == "__main__":
    main()
