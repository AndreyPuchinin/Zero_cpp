"""Оркестрация настройки и запуска механики модели карточки."""

from .CardModel import CardModel


VALUE_SETTERS = (
    "set_usual_vals",
    "set_selflink_vals",
    "set_templ_vals",
    "set_selflink_templ_vals",
    "set_id_vals",
    "set_id_selflink_vals",
    "set_id_templ_vals",
    "set_id_selflink_templ_vals",
)


def create_card(name: object, values_by_type: list[object]) -> CardModel:
    """Настраивает модель карточки сеттерами и запускает её проверку."""
    # Создаём модель с безопасными значениями по умолчанию и передаём параметры.
    card = CardModel()
    card.set_name(name)
    for setter_name, values in zip(VALUE_SETTERS, values_by_type):
        getattr(card, setter_name)(values)

    # Запускаем механику после завершения настройки модели.
    card.initialize()
    return card
