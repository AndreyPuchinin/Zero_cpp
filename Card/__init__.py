"""Совместимая точка импорта модели карточки."""

from Models.CardModel import CardModel
from Models.system_behavior import create_card


def Card(
    name: object,
    usual_vals: object,
    selflink_vals: object,
    templ_vals: object,
    selflink_templ_vals: object,
    id_vals: object,
    id_selflink_vals: object,
    id_templ_vals: object,
    id_selflink_templ_vals: object,
) -> CardModel:
    """Создаёт CardModel для сохранения прежнего контракта импорта."""
    # Старые вызывающие стороны передают группы отдельными аргументами.
    values_by_type = [
        usual_vals,
        selflink_vals,
        templ_vals,
        selflink_templ_vals,
        id_vals,
        id_selflink_vals,
        id_templ_vals,
        id_selflink_templ_vals,
    ]
    return create_card(name, values_by_type)


__all__ = ["Card"]
