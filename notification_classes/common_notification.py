import inspect
import os
from abc import abstractmethod
from unittest import result
from notification_classes import error, warning, note, message

class common_notification():
    def __init__(self):
        self.error = error.error()
        self.warning = warning.warning()
        self.note = note.note()
        self.message = message.message()
    
    # Глобальная функция, анализирующая стек вызовов
    def get_stack_node(self):
        """
        Выводит полную информацию о стеке вызовов:
        - модуль (файл)
        - номер строки
        - колонка (позиция начала вызова в строке)
        - описание уровня
        - сам код строки
        """
        stack = inspect.stack()

        level = 1
        result_str = "Stack trace:\n"
        # Идём с конца стека (глобальный уровень) к началу (место вызова)
        for i in range(len(stack) - 1, 0, -1):
            frame = stack[i]
            info = frame[0]  # сам объект фрейма

            # 1. Модуль (берём только имя файла, без полного пути)
            module = os.path.basename(frame.filename)

            # # Предотвращаем попадение вывода в стек вызовов результата методов данного класса
            # if "common_notification" in module:
            #     print(11111111)
            #     return ""


            # 2. Номер строки
            lineno = frame.lineno

            # 3. Позиция начала вызова в строке (колонка)
            col_offset = self._get_col_offset(frame, info)

            # Описание уровня
            func_name = frame.function
            if func_name == '<module>':
                desc = "Global level (module)"
            else:
                desc = f"Method/Function '{func_name}'"

            # Сам код строки
            code_line = frame.code_context[0].strip() if frame.code_context else "Failed to get code line"

            # Форматированный вывод
            result_str += f"-Level: {level}/{len(stack) - 1}\n"
            result_str += f"--Module: {module}\n"
            result_str += f"--Line: {lineno}\n"
            result_str += f"--Column: {col_offset}\n"
            result_str += f"--Description: {desc}\n"
            result_str += f"--Code_line: {code_line}\n"
            level += 1

            if i != 1:  # Если дошли до места вызова, выходим из цикла
                result_str += "\n"

        return result_str


    def _get_col_offset(self, frame, info):
        """
        Получает колонку (позицию) начала текущего вызова в строке.
        В Python 3.11+ используется frame.positions, 
        в старых версиях — поиск подстроки в тексте строки.
        """
        # Современный способ (Python 3.11+)
        positions = getattr(info, 'positions', None)
        if positions is not None:
            # positions = (start_lineno, end_lineno, start_col_offset, end_col_offset)
            return positions[2]

        # Fallback для старых версий Python: ищем имя функции в строке
        code = frame.code_context[0] if frame.code_context else ""
        func_name = frame.function

        # Ищем "имя_функции(" в строке
        search_pattern = f"{func_name}("
        idx = code.find(search_pattern)
        if idx != -1:
            return idx

        # Если не нашли — возвращаем 0
        return 0

    def add_error_without_stack_nodes(self, err: str):
        self.error.add_notification(err)

    def add_warning_without_stack_nodes(self, warning: str):
        self.warning.add_notification(warning)

    def add_note_without_stack_nodes(self, note: str):
        self.note.add_notification(note)

    def add_message_without_stack_nodes(self, mes: str):
        self.message.add_notification(mes)

    def add_error_with_stack_nodes(self, err: str):
        error_str = f"\n{self.get_stack_node()}\nError_text: \"{err}\"\n"
        self.error.add_notification(error_str)

    def add_warning_with_stack_nodes(self, warning: str):
        warning_str = f"\n{self.get_stack_node()}\nWarning_text: \"{warning}\"\n"
        self.warning.add_notification(warning_str)

    def add_note_with_stack_nodes(self, note: str):
        note_str = f"\n{self.get_stack_node()}\nNote_text: \"{note}\"\n"
        self.note.add_notification(note_str)

    def add_message_with_stack_nodes(self, mes: str):
        message_str = f"\n{self.get_stack_node()}\nMessage_text: \"{mes}\"\n"
        self.message.add_notification(message_str)

    def add_notifications(self, notifications: list):
        if not isinstance(notifications, list):
            self.add_error_with_stack_nodes(f"Incorrect type of notification:\n{notifications}\nExpected list, got {type(notifications)}")
            return

        for one_notification in notifications:
            if not isinstance(one_notification, dict):
                self.add_error_with_stack_nodes(f"Incorrect type of notification:\n{one_notification}\nExpected dict, got {type(one_notification)}")
                continue

            for key, value in one_notification.items():
                if key == "errors" and value != []:
                    for one_error in value:
                        self.add_error_without_stack_nodes(one_error)
                elif key == "warnings" and value != []:
                    for one_warning in value:
                        self.add_warning_without_stack_nodes(one_warning)
                elif key == "notes" and value != []:    
                    for one_note in value:
                        self.add_note_without_stack_nodes(one_note)
                elif key == "messages" and value != []:
                    for one_message in value:
                        self.add_message_without_stack_nodes(one_message)
                else:
                    self.add_error_with_stack_nodes(f"Unknown notification type: {key}")

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