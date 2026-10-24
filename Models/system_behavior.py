"""Проверка, нормализация и сериализация данных карточки."""

from .Card import Card


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


def initialize_card(card: Card, name: object, values_by_type: list[object]) -> list[str]:
    """Проверяет входные данные, обновляет модель и возвращает предупреждения."""
    # Переносим переданные группы значений в соответствующие поля модели.
    for one_type_values, values in zip(VALUES_TYPES, values_by_type):
        setattr(card, one_type_values, values)

    # Проверяем форму каждой группы и удаляем некорректные элементы.
    contains_value = False
    has_invalid_value = False
    warnings = []

    for one_type_values in VALUES_TYPES:
        values = getattr(card, one_type_values)
        if not isinstance(values, list):
            setattr(card, one_type_values, [])
            has_invalid_value = True
            continue

        index = 0
        while index < len(values):
            value = values[index]
            if type(value) is not dict or type(value.get("val", None)) is not str:
                warnings.append(f"Value {value} excepted from Card")
                del values[index]
                has_invalid_value = True
            else:
                contains_value = True
                index += 1

    # Недопустимое имя или отсутствие корректных значений делает карточку недействительной.
    if type(name) is not str or name == "" or not contains_value:
        card.name = [None]
        for one_type_values in VALUES_TYPES:
            setattr(card, one_type_values, [])
        card.status = "unsuccessful"
        return warnings

    # Назначаем успешность в зависимости от того, встретились ли ошибки в значениях.
    card.name = name
    card.status = "half_successful" if has_invalid_value else "successful"
    return warnings


def serialize_card(card: Card, status: str | None = None) -> dict[str, object]:
    """Формирует публичное словарное представление карточки."""
    # При необходимости используем переданный статус, сохраняя прежний формат результата.
    result = {"status": card.status if status is None else status, "name": card.name}
    result.update({one_type_values: getattr(card, one_type_values) for one_type_values in VALUES_TYPES})
    return result
