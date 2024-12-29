import os
from datetime import datetime

def create_diary_entry(file_name):
    """
    This function allows users to create a new diary entry
    and saves it to a text file.
    """
    try:
        entry = input("Write your diary entry: ")
        timestamp = input("Do you want to add a timestamp? (yes/no): ").strip().lower()

        with open(file_name, "a") as file:  # Append mode to avoid overwriting existing entries
            if timestamp == "yes":
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{time_now}] {entry}\n")
            else:
                file.write(f"{entry}\n")

        print("Diary entry saved successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def view_diary_entries(file_name):
    """
    This function allows users to view all previous diary entries
    stored in the text file.
    """
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError("Diary file not found. Start by adding a new entry.")
        
        with open(file_name, "r") as file:
            entries = file.readlines()
        
        if entries:
            print("\n--- Your Diary Entries ---")
            for entry in entries:
                print(entry.strip())
            print("--- End of Entries ---\n")
        else:
            print("Your diary is empty. Start writing your first entry!")
    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print("Error: Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    The main function provides options to the user
    for creating and viewing diary entries.
    """
    file_name = "personal_diary.txt"

    while True:
        print("\n--- Personal Diary ---")
        print("1. Write a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            create_diary_entry(file_name)
        elif choice == "2":
            view_diary_entries(file_name)
        elif choice == "3":
            print("Exiting the diary application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
