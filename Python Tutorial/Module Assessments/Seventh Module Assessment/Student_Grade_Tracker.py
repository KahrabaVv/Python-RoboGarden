import os

def input_and_store_grades(file_name):
    """
    This function allows students to input grades for each subject,
    validates the input, and stores the grades in a file.
    """
    try:
        with open(file_name, "a") as file:  # Open file in append mode
            while True:
                subject = input("Enter the subject name (or type 'done' to finish): ").strip()
                if subject.lower() == 'done':
                    break
                
                grade = input(f"Enter your grade for {subject}: ").strip()
                if not grade.replace('.', '', 1).isdigit():
                    raise ValueError(f"Invalid grade input: {grade}. Please enter a numeric value.")
                
                grade = float(grade)
                if grade < 0 or grade > 100:
                    raise ValueError(f"Grade out of range: {grade}. Please enter a value between 0 and 100.")
                
                file.write(f"{subject},{grade}\n")
                print(f"Grade for {subject} saved successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def calculate_and_display_average(file_name):
    """
    This function reads grades from the file and calculates the average grade.
    """
    try:
        if not os.path.exists(file_name):
            raise FileNotFoundError("Grade file not found. Start by entering your grades.")

        with open(file_name, "r") as file:
            lines = file.readlines()
        
        if not lines:
            print("No grades found. Please enter some grades first.")
            return
        
        total, count = 0, 0
        for line in lines:
            subject, grade = line.strip().split(",")
            total += float(grade)
            count += 1
        
        average = total / count
        print(f"\n--- Your Grades ---")
        for line in lines:
            subject, grade = line.strip().split(",")
            print(f"{subject}: {grade}")
        print(f"--- End of Grades ---\n")
        print(f"Your average grade is: {average:.2f}")
    except FileNotFoundError as e:
        print(e)
    except ValueError:
        print("Error: Invalid data format in the file. Please ensure all grades are numeric.")
    except PermissionError:
        print("Error: Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    The main function provides options for the student to input grades,
    calculate the average, and view their grades.
    """
    file_name = "student_grades.txt"

    while True:
        print("\n--- Grade Tracker ---")
        print("1. Input and store grades")
        print("2. Calculate and display average grade")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            input_and_store_grades(file_name)
        elif choice == "2":
            calculate_and_display_average(file_name)
        elif choice == "3":
            print("Exiting the grade tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
