import json
from abc import abstractmethod
from notification_classes import notification

class error(notification.notification):
    def __init__(self):
        self.err = []
    
    def create_notification(self, err: str):
        self.err += [err]

    def get_all_notifications(self):
        # выводим красиво с табом в 4 пробела
        return self.err