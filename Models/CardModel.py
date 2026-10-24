"""Базовая модель карточки и её атомарная механика."""

from notification_classes import common_notification
from success_class.success import success


class CardModel:
    """Хранит данные карточки и выполняет их проверку после настройки сеттерами."""

    # Имена групп задают единый порядок проверки и формирования результата.
    VALUES_TYPES = (
        "usual_vals",
        "selflink_vals",
        "templ_vals",
        "selflink_templ_vals",
        "id_vals",
        "id_selflink_vals",
        "id_templ_vals",
        "id_selflink_templ_vals",
    )

    def __init__(self):
        # Инициализируем безопасные значения, чтобы модель работала и без сеттеров.
        self.name: str = None
        self.usual_vals: list[str] = []
        self.selflink_vals: list[str] = []
        self.templ_vals: list[str] = []
        self.selflink_templ_vals: list[str] = []
        self.id_vals: list[str] = []
        self.id_selflink_vals: list[str] = []
        self.id_templ_vals: list[str] = []
        self.id_selflink_templ_vals: list[str] = []
        self.status = "unsuccessful"
        self.notifications = common_notification.common_notification()
        self.success = success()
        self.success.set_unsuccessful()

    # Сеттеры образуют внешний контракт настройки данных карточки.
    def set_name(self, value: str) -> None:
        self.name = value

    def set_usual_vals(self, value: list[str]) -> None:
        self.usual_vals = value

    def set_selflink_vals(self, value: list[str]) -> None:
        self.selflink_vals = value

    def set_templ_vals(self, value: list[str]) -> None:
        self.templ_vals = value

    def set_selflink_templ_vals(self, value: list[str]) -> None:
        self.selflink_templ_vals = value

    def set_id_vals(self, value: list[str]) -> None:
        self.id_vals = value

    def set_id_selflink_vals(self, value: list[str]) -> None:
        self.id_selflink_vals = value

    def set_id_templ_vals(self, value: list[str]) -> None:
        self.id_templ_vals = value

    def set_id_selflink_templ_vals(self, value: list[str]) -> None:
        self.id_selflink_templ_vals = value

    def initialize(self) -> None:
        """Проверяет настроенные данные, нормализует их и назначает статус."""
        # Проверяем структуру каждой группы, удаляя некорректные значения.
        contains_value = False
        has_invalid_value = False

        for one_type_values in self.VALUES_TYPES:
            values = getattr(self, one_type_values)
            if not isinstance(values, list):
                setattr(self, one_type_values, [])
                has_invalid_value = True
                continue

            index = 0
            while index < len(values):
                value = values[index]
                if type(value) is not dict or type(value.get("val", None)) is not str:
                    self.notifications.add_warning_with_stack_nodes(
                        f"Value {value} excepted from Card"
                    )
                    del values[index]
                    has_invalid_value = True
                else:
                    contains_value = True
                    index += 1

        # Недопустимое имя или отсутствие корректных значений обнуляет карточку.
        if type(self.name) is not str or self.name == "" or not contains_value:
            self.name = [None]
            for one_type_values in self.VALUES_TYPES:
                setattr(self, one_type_values, [])
            self._set_status("unsuccessful")
            return

        # Сохраняем прежнее разделение результата на полный и частичный успех.
        self._set_status("half_successful" if has_invalid_value else "successful")

    def _set_status(self, value: str) -> None:
        """Синхронизирует текстовый статус с совместимым объектом успешности."""
        self.status = value
        if value == "successful":
            self.success.set_successful()
        elif value == "half_successful":
            self.success.set_half_successful()
        else:
            self.success.set_unsuccessful()

    def get_card(self) -> dict[str, object]:
        """Возвращает публичное словарное представление карточки."""
        # Формируем результат в установленном порядке ключей.
        result = {"status": self.success.get_state(), "name": self.name}
        result.update(
            {one_type_values: getattr(self, one_type_values) for one_type_values in self.VALUES_TYPES}
        )
        return result

    def get_notifications(self) -> dict[str, list]:
        """Возвращает уведомления, сформированные при проверке карточки."""
        return self.notifications.get_all_notifications()
