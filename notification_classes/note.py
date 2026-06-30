import json
from abc import abstractmethod
from notification_classes import base_notification

class note(base_notification.notification):
    def __init__(self):
        self.note = []
    
    def add_notification(self, note: str):
        self.note += [note]

    def get_all_notifications(self):
        return self.note