from notification_classes import common_notification
from CardManager import CardManager
from Logger import Logger

class Zero:
    def __init__(self):
        # хранит ошибки, которые произошли при работе программы
        # и кладет их в Логгер
        self.notifications = common_notification.common_notification() 
        self.some_CardManager_obects = []
        # self.Parser_object = Parser()
        self.Logger_object = Logger()

    def warp_drive(self, values):
        # Парсит и анлизирует входной json (+инклюды!!),
        # генерирует лог-файл,
        # модифицирует карты фильтрами

        self.values = values
        # <!!!ВРЕМЕННЫЙ КОД!!!>
        CardManager_object1 = CardManager()
        CardManager_object2 = CardManager()
        
        # CardManager_object1.create_card("<digit>", [{"type": "usual", "value": ["0"]}])
        CardManager_object1.create_card(True, 1)
        CardManager_object2.create_card("<number>", values)
        self.some_CardManager_obects = [CardManager_object1, CardManager_object2]
        for one_CardManager_object in self.some_CardManager_obects:
            # print(one_CardManager_object.get_notifications_as_list())
            self.Logger_object.add_libruary(one_CardManager_object.get_libruary())
            self.Logger_object.add_notifications(one_CardManager_object.get_notifications_as_json())

        # проверки на обработку некорректных типов данных в методах Логгера
        self.Logger_object.add_libruary("some string instead of list")
        self.Logger_object.add_error("Some error from Logger")
        self.Logger_object.add_warning("Some warning from Logger")
        self.Logger_object.add_note("Some note from Logger")
        # self.Logger_object.add_message("Some message from Logger")
        self.Logger_object.add_input_string(123)
        self.Logger_object.add_swap("some string instead of tuple")
        return self.Logger_object.get_log()
        # </!!!!ВРЕМЕННЫЙ КОД!!!>