
from notification_classes import error

class Logger:
    def __init__(self):
        self.cards = []
        self.inp_str = ''
        self.swaps = []

        # хранит ошибки, которые произошли при работе программы
        self.errors = error.error()

    def add_libruary(self, libruary: list):
        if not isinstance(libruary, list):
            self.add_error([f"Incorrect type of library:\n{libruary}\nExpected list, got {type(libruary)}"])
            return

        # добавляет карту в лог
        self.cards += libruary

    def add_error(self, error: list):
        if not isinstance(error, list):
            self.add_error([f"Incorrect type of error:\n{error}\nExpected list, got {type(error)}"])
            return

        # добавляет ошибку в лог
        for one_error in error:
            self.errors.create_notification(one_error)

    def add_input_string(self, inp_str: str):
        if not isinstance(inp_str, str):
            self.add_error([f"Incorrect type of input string:\n{inp_str}\nExpected str, got {type(inp_str)}"])
            return

        # добавляет входную строку в лог
        self.inp_str = inp_str

    def add_swap(self, swap: list):
        if not isinstance(swap, list):
            self.add_error([f"Incorrect type of swap:\n{swap}\nExpected list, got {type(swap)}"])
            return

        # добавляет обмен в лог
        self.swaps += swap

    def get_log(self):
        # возвращает все ошибки, которые произошли при работе программы
        log = {
            "cards": self.cards,
            "input_string": self.inp_str,
            "swaps": self.swaps,
            "errors": self.errors.get_all_notifications()
        }
        return log