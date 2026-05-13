class success():
    def __init__(self):
        self.successful = False
        self.unsuccessful = False
        self.half_success = False
    
    def set_successful(self):
        self.successful = True
        self.unsuccessful = False
        self.half_success = False
    
    def set_unsuccessful(self):
        self.successful = False
        self.unsuccessful = True
        self.half_success = False

    def set_half_successful(self):
        self.successful = False
        self.unsuccessful = False
        self.half_success = True

    def get_state(self):
        if self.successful:
            return "successful"
        if self.unsuccessful:
            return "unsuccessful"
        if self.half_success:
            return "half_successful"


obj = success()
obj.set_unsuccessful()
print(obj.get_state())