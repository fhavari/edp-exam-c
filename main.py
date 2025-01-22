from university import University
from student import Student

if __name__ == "__main__":
    
    university = University("Wseiz University")
    student = Student("Fatih")

    university.add_course("Math 101", 3)
    university.add_course("Physics 101", 2)

    university.register_course(student, "Math 101")   # Successful
    university.register_course(student, "Physics 101") # Successful
    university.register_course(student, "Math 101")   # Successful
    university.register_course(student, "Math 101")   # Rejected (No slots left)

    university.process_events()