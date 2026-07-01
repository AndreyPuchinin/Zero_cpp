
from notification_classes import common_notification

class Logger:
    def __init__(self):
        self.cards = []
        self.inp_str = ''
        self.swaps = []

        # хранит ошибки, которые произошли при работе программы
        self.notifications = common_notification.common_notification()

    def add_libruary(self, libruary: list):
        if not isinstance(libruary, list):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of library:\n{libruary}\nExpected list, got {type(libruary)}")
            return

        # добавляет карту в лог
        self.cards += libruary

    def add_error(self, error: str):
        if not isinstance(error, str):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of error:\n{error}\nExpected str, got {type(error)}")
            return
        
        # добавляет ошибку в лог
        self.notifications.add_error_with_stack_nodes(error)

    def add_warning(self, warning: str):
        if not isinstance(warning, str):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of warning:\n{warning}\nExpected str, got {type(warning)}")
            return
        
        # добавляет предупреждение в лог
        self.notifications.add_warning_with_stack_nodes(warning)

    def add_note(self, note: str):
        if not isinstance(note, str):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of note:\n{note}\nExpected str, got {type(note)}")
            return
        
        # добавляет заметку в лог
        self.notifications.add_note_with_stack_nodes(note)

    def add_message(self, message: str):
        if not isinstance(message, str):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of message:\n{message}\nExpected str, got {type(message)}")
            return
        
        # добавляет сообщение в лог
        self.notifications.add_message_with_stack_nodes(message)

    def add_notifications(self, notifications: dict):
        if not isinstance(notifications, dict):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of notification:\n{notifications}\nExpected list, got {type(notifications)}"  )
            return

        # добавляет ошибку в лог
        self.notifications.add_notifications(notifications)
        #for one_notification in notifications:        
        #    one_local_notification = list(one_notification.items())
        #    if one_local_notification[0][0] == "errors":
        #        for one_error in one_local_notification[0][1]:
        #            self.notifications.add_error_with_stack_nodes(one_error)
#
        #    if one_local_notification[0][0] == "warnings":
        #        for one_warning in one_local_notification[0][1]:
        #            self.notifications.add_warning_with_stack_nodes(one_warning)
#
        #    if one_local_notification[0][0] == "notes":
        #        for one_note in one_local_notification[0][1]:
        #            self.notifications.add_note_with_stack_nodes(one_note)
#
        #    if one_local_notification[0][0] == "message":
        #        for one_message in one_local_notification[0][1]:
        #            self.notifications.add_message_with_stack_nodes(one_message)

    def add_input_string(self, inp_str: str):
        if not isinstance(inp_str, str):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of input string:\n{inp_str}\nExpected str, got {type(inp_str)}")
            return

        # добавляет входную строку в лог
        self.inp_str = inp_str

    def add_swap(self, swap: list):
        if not isinstance(swap, list):
            self.notifications.add_error_with_stack_nodes(f"Incorrect type of swap:\n{swap}\nExpected list, got {type(swap)}")
            return

        # добавляет обмен в лог
        self.swaps += swap

    def get_log(self):
        # возвращает все ошибки, которые произошли при работе программы
        log = {
            "cards": self.cards,
            "input_string": self.inp_str,
            "swaps": self.swaps,
            "notifications": self.notifications.get_all_notifications()
        }
        return log