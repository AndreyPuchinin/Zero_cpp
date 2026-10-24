"""Модель данных карточки и распределённых по категориям значений."""

from dataclasses import dataclass, field


@dataclass(eq=False, repr=False)
class Card:
    """Хранит данные карточки, не выполняя проверку и преобразование данных."""

    # Основные данные карточки и группы значений сохраняются без обработки.
    name: object = None
    usual_vals: object = field(default_factory=list)
    selflink_vals: object = field(default_factory=list)
    templ_vals: object = field(default_factory=list)
    selflink_templ_vals: object = field(default_factory=list)
    id_vals: object = field(default_factory=list)
    id_selflink_vals: object = field(default_factory=list)
    id_templ_vals: object = field(default_factory=list)
    id_selflink_templ_vals: object = field(default_factory=list)

    # До проверки карточка считается недействительной.
    status: str = "unsuccessful"
