"""
Python program to fetch student's marks from a dictionary.
"""
# Student dictionary with name and marks scored
student_marks = {
    'alice' : 85,
    'bob' : 70,
    'charlie' : 60,
    'david' : 95,
    'joe' : 80
}

#print(student_marks, type(student_marks))

def get_student_mark():
    while True:
        # requesting user to provide the student's name
        student_name = input("Enter student's name (or type 'quit' to exit): ").strip().lower()

        # checks if quit command provided
        if student_name == 'quit':
            print("Thank you. Visit again!.")
            break

        mark = student_marks.get(student_name)

        # conditional checking
        if mark is not None:
            print(f"{student_name.title()}'s marks: {mark}")
        else:
            print("Student not found.")

if __name__ == '__main__':
    get_student_mark()