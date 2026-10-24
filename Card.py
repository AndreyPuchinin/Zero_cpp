"""Совместимый интерфейс Card на основе модели данных МИ."""

from typing import List

from Models.Card import Card as CardModel
from Models.system_behavior import initialize_card, serialize_card
from notification_classes import common_notification
from success_class.success import success


class Card(CardModel):
    """Проверяет данные карточки и сохраняет прежний внешний интерфейс."""

    def __init__(
        self,
        name: str,
        usual_vals: List[list],
        selflink_vals: List[list],
        templ_vals: List[list],
        selflink_templ_vals: List[list],
        id_vals: List[list],
        id_selflink_vals: List[list],
        id_templ_vals: List[list],
        id_selflink_templ_vals: List[list],
    ):
        super().__init__()
        # Подготавливаем контейнеры уведомлений и статус карточки.
        self.notifications = common_notification.common_notification()
        self.success = success()

        # Выполняем проверку через поведенческий слой и передаём предупреждения наружу.
        warnings = initialize_card(
            self,
            name,
            [
                usual_vals,
                selflink_vals,
                templ_vals,
                selflink_templ_vals,
                id_vals,
                id_selflink_vals,
                id_templ_vals,
                id_selflink_templ_vals,
            ],
        )
        for warning in warnings:
            self.notifications.add_warning_with_stack_nodes(warning)

        # Синхронизируем прежний объект успешности с результатом проверки модели.
        if self.status == "successful":
            self.success.set_successful()
        elif self.status == "half_successful":
            self.success.set_half_successful()
        else:
            self.success.set_unsuccessful()

    def get_card(self):
        # Возвращаем карточку в прежнем формате словаря.
        return serialize_card(self, self.success.get_state())

    def get_notifications(self):
        # Возвращаем накопленные предупреждения и остальные уведомления.
        return self.notifications.get_all_notifications()


if __name__ == "__main__":
    # При прямом запуске файла выполняем тесты карточки.
    import unittest

    unittest.main(module="tests.test_card")
