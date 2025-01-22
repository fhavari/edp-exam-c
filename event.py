class Event:
    def __init__(self, payload: dict):
        self.payload = payload


class CourseRegisteredEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)


class RegistrationRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
