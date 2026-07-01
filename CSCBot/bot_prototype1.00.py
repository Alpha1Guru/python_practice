"""The bot high level overview is to give a general idea of how the bot will work.
It is not a complete implementation but rather a guide for the implementation."""
import re
print("Welcome Your CSC Assistant Bot!")
print("How can I help you today?")
available_options = [
    "1. Mark Attendance for CSC205",
    "2. Register For this Semester",
    "3. Pay for Math101 workbook"]  
end_word = "exit"
def print_options():
    """This function will print the available options for the user."""
    print("\nAvailable options:")
    for option in available_options:
        print(f"\t{option}")
    print(f"Type '{end_word}' to quit the bot.\n")

def mark_attendance():
    """Function to mark attendance for CSC205."""
    def get_matric_num():
        csc_matric_format = r'240591\d{3}'  #240591245
        pattern = csc_matric_format
        while True:
            matric = input("Enter your matric number: ").strip()

            if re.match(pattern, matric):
                print("Matric number accepted.")
                return matric
            else:
                print("Invalid matric number format. Please try again.")

    def confirm_student_matric_exit(student_ID_DB, matric_provided):
        pass
    def update_attendance_list(atttendance_for_maths_class):
        pass

    attendance_for_maths_class = {"240591245"}  # Example attendance list
    matric = get_matric_num()
    if matric in attendance_for_maths_class:
        print("Your name is already recorded in the attendance list")
    else: 
        attendance_for_maths_class.add(matric)
        update_attendance_list(attendance_for_maths_class)
        print("Your name have been saved.")
    print(attendance_for_maths_class)
    print("Attendance marked successfully.")

def get_user_choice():
    """This function will get the user's choice from the available options.e.g 1, 2, or 3."""
    print("\nPlease choose an option by entering the corresponding number.")
    print_options()
    user_choice = input("Enter your choice: ")
    if user_choice.lower() == end_word:
        print("Exiting the bot. Thank you!")
        exit()
    elif user_choice not in [str(i) for i in range(1, len(available_options) + 1)]:
        print(f"\n'{user_choice}' is NOT AN option!!")
        return get_user_choice()
    else:
        print(f"You chose option {available_options[int(user_choice)-1]}.")
    return user_choice

def handle_choice(choice):
    """This function will handle the user's choice and call the appropriate function."""
    if choice == "1":
        # Call the function to mark attendance
        print("Marking attendance for CSC205...")
        # Here you would call the function to mark attendance
        mark_attendance()
    elif choice == "2":
        # Call the function to register for this semester
        print("Registering for this semester...")
        # Here you would call the function to register
    elif choice == "3":
        # Call the function to pay for Math101 workbook
        print("Paying for Math101 workbook...")
        # Here you would call the function to pay

user_choice = get_user_choice()
handle_choice(user_choice)
print("Thank you for using the CSC Assistant Bot! Have a great day!")

