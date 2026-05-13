from abc import ABC, abstractmethod
class notification(ABC):
    @abstractmethod
    def create_notification(self):
        pass
    
    @abstractmethod
    def get_all_notifications(self):
        pass