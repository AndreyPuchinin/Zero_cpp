import json
from abc import abstractmethod
from notification_classes import base_notification

class message(base_notification.notification):
    def __init__(self):
        self.mes = []
    
    def add_notification(self, mes: str):
        self.mes += [mes]

    def get_all_notifications(self):
        return self.mes