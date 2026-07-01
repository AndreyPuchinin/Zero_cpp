from abc import abstractmethod
from notification_classes import base_notification

class warning(base_notification.notification):
    def __init__(self):
        self.war = []
    
    def add_notification(self, war: str):
        self.war += [war]

    def get_all_notifications(self):
        return self.war