import json
from abc import abstractmethod
from notification_classes import error, warning, note, message

class common_notification():
    def __init__(self):
        self.error = error.error()
        self.warning = warning.warning()
        self.note = note.note()
        self.message = message.message()
    
    def add_error(self, err: str):
        self.error.add_notification(err)

    def add_warning(self, warning: str):
        self.warning.add_notification(warning)

    def add_note(self, note: str):
        self.note.add_notification(note)

    def add_message(self, mes: str):
        self.message.add_notification(mes)

    def get_all_errors(self):
        return self.error.get_all_notifications()
    
    def get_all_warnings(self):
        return self.warning.get_all_notifications()
    
    def get_all_notes(self):
        return self.note.get_all_notifications()
    
    def get_all_messages(self):
        return self.message.get_all_notifications()
    
    def get_all_notifications(self):
        notifications = [
            {"errors" :self.get_all_errors()},
            {"warnings" :self.get_all_warnings()},
            {"notes" :self.get_all_notes()},
            {"messages" :self.get_all_messages()}
        ]
        return notifications