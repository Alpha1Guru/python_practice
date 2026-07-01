#Basically any storage place for student Id and name
#probably excel or sql 
def load_student_id(student_ID_DB):
    pass
def get_user_request():
    pass
student_ID_DB = load_student_id() #Need to learn collections in order too annotate it properly
user_request = get_user_request("""What do you want to do today.
                     1. Pay for Math101 workbook
                     2. Mark Attendance for CSC205
                     3. Register For this Semester""")

#To Register for this Semester
def get_student_name():
    """I would probably use a form to get the student name and other details"""
    pass
def get_student_matric():
    """I would probably use a form to get the student matric and other details"""
    pass
student_matric = get_student_matric()
student_name = get_student_name()
if student_matric in student_ID_DB:
    print("You are already registered for this semester")
else:
    student_ID_DB.add(student_matric)
    print("You have been registered for this semester")
    #I would probably save the student name and matric in a database or file for future reference

#To pay for Stuff
def pay_for_X(payment_option):
    """I would probaly use some pay way gateway like flutterwave, palmpay or opay api
    I would handle failures and success and log each of them in a database"""
    pass
def save_to_payerlist_(payed_for_maths_DB, Transaction_Id):
    pass
payment_option = input("""Choose a payment option:
                       1. Opay
                       2. Palmpay
                       3. Card Option flutterwave
                       4. Make Transaction to Account
                       """)# The less the better. I would probaly force them to use Palmpay or Opay and make them use my code when registering for it. But less distractions maybe better too.


#To Mark Attendance
def load_attendace_DB():
    pass
def get_matric(matric):
    pass
def confirm_student_matric_exit(student_ID_DB, matric_provided):
    pass
def update_attendance_list(atttendance_for_maths_class):
    pass

attendance_for_maths_class = load_attendace_DB()
matric = get_matric("Give me your matric")
if confirm_student_matric_exit is False:
    print("This Matric Doesn't Exit, Try Registering or confirm your details and try again")
else:
    if matric in attendance_for_maths_class:
        print("Your name is already recorded in the attendance list")
    else: 
        attendance_for_maths_class.add(matric)
        update_attendance_list(attendance_for_maths_class)
        print("Your name have been saved:")

