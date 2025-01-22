# University System
class Event:
    def __init__(self, payload: dict):
        self.payload = payload

class CourseRegisteredEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)

class RegistrationRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)


class University:
    def __init__(self, name):
        self.name = name
        self.courses = {} 
        self.queue = []    
    def add_course(self, course_name, capacity):
        self.courses[course_name] = self.courses.get(course_name, 0) + capacity

    def register_course(self, student, course_name):
        if course_name in self.courses and self.courses[course_name] > 0:
            self.courses[course_name] -= 1
            event = CourseRegisteredEvent({"student": student.name, "course": course_name})
            self.queue.append(event)
        else:
            event = RegistrationRejectedEvent({"student": student.name, "course": course_name, "reason": "No available slots"})
            self.queue.append(event)

    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            if isinstance(event, CourseRegisteredEvent):
                print(f"Course Registered: {event.payload}")
            elif isinstance(event, RegistrationRejectedEvent):
                print(f"Registration Rejected: {event.payload}")

class Student:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # Initialize university and student
    university = University("Wseiz University")
    student = Student("Fatih")

   
    university.add_course("Math 101", 3)
    university.add_course("Physics 101", 2)

    
    university.register_course(student, "Math 101")   # Successful
    university.register_course(student, "Physics 101") # Successful
    university.register_course(student, "Math 101")   # Successful
    university.register_course(student, "Math 101")   # Rejected (No slots left)

    
    university.process_events()
