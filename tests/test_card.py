"""Независимые имитационные тесты проверки и нормализации Card."""

from pathlib import Path
import sys
import unittest
from typing import Any

# Добавляем корень проекта в путь импорта при прямом запуске этого файла.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Card import Card


VALUE_FIELDS = (
    "usual_vals",
    "selflink_vals",
    "templ_vals",
    "selflink_templ_vals",
    "id_vals",
    "id_selflink_vals",
    "id_templ_vals",
    "id_selflink_templ_vals",
)


def imitate(
    name_correctness: bool,
    correct: Any,
    incorrect: Any,
    few_vals: int,
    all_vals: int,
    few_types: int,
) -> tuple[bool, dict[str, Any], dict[str, Any]]:
    """Независимо строит вход, вычисляет ожидаемый результат и сравнивает его с Card.

    Аргументы задают классы эквивалентности имени карточки и её значений.
    Возвращаются признак совпадения, ожидаемая карточка и фактическая карточка.
    """
    # Формируем имя по параметрам сценария, не используя логику Card.
    if name_correctness and few_vals != 0 and few_types > 0:
        name = correct
    else:
        name = incorrect

    # Создаём входные и ожидаемые группы значений в фиксированном порядке полей.
    input_values: list[Any] = [[] for _ in VALUE_FIELDS]
    expected_values: list[list[dict[str, Any]]] = [[] for _ in VALUE_FIELDS]
    has_invalid_value = False

    # Заполняем выбранные типы корректными и некорректными примерами.
    # Для остальных типов задаём некорректную структуру.
    for type_index in range(len(VALUE_FIELDS)):
        if type_index >= few_types:
            input_values[type_index] = {"val": incorrect}
            has_invalid_value = True
            continue

        for value_index in range(all_vals):
            if value_index < few_vals:
                value = {"val": correct}
                input_values[type_index].append(value)
                if type(correct) is str:
                    expected_values[type_index].append(value.copy())
                else:
                    has_invalid_value = True
            else:
                value = {"val": incorrect}
                input_values[type_index].append(value)
                if type(incorrect) is not str:
                    has_invalid_value = True
                else:
                    expected_values[type_index].append(value.copy())

    # Вычисляем ожидаемый результат независимо от реализации класса Card.
    has_valid_name = type(name) is str and name != ""
    has_valid_value = any(expected_values)
    if not has_valid_name or not has_valid_value:
        expected_name = [None]
        expected_values = [[] for _ in VALUE_FIELDS]
        expected_status = "unsuccessful"
    else:
        expected_name = name
        expected_status = "half_successful" if has_invalid_value else "successful"

    expected_card: dict[str, Any] = {
        "status": expected_status,
        "name": expected_name,
    }
    expected_card.update(dict(zip(VALUE_FIELDS, expected_values)))

    # Передаём сформированные данные в Card и сравниваем публичный результат.
    actual_card = Card(name, *input_values).get_card()
    return expected_card == actual_card, expected_card, actual_card


# Семь исходных типовых сценариев для обычного быстрого запуска.
TEST_CASES: list[tuple[bool, Any, Any, int, int, int]] = [
    (False, "good", None, 0, -1, 0),
    (False, "good", None, 0, -1, 0),
    (True, "good", None, 0, 0, 2),
    (True, "good", None, 1, 4, 1),
    (True, "good", None, 2, 4, 2),
    (True, "good", None, 4, 5, 2),
    (True, "good", None, 4, 4, 8),
]

# Для полного перебора закомментируйте список TEST_CASES выше
# и раскомментируйте этот блок. Границы и сдвиги циклов сохранены из старых тестов.
# TEST_CASES = []
# for name_correctness in [True, False]:
#     for all_types in range(5):
#         for all_vals in range(5):
#             for few_vals in range(all_vals):
#                 TEST_CASES.append(
#                     (
#                         name_correctness,
#                         "good",
#                         None,
#                         few_vals - 2,
#                         all_vals - 2,
#                         all_types - 2,
#                     )
#                 )


class CardImitationTests(unittest.TestCase):
    """Запускает каждый независимый сценарий imitate отдельным тестом unittest."""


def _make_test(case: tuple[bool, Any, Any, int, int, int]):
    """Создаёт отдельный метод unittest для одного сценария imitate."""

    def test_case(self: CardImitationTests) -> None:
        name_correctness, correct, incorrect, few_vals, all_vals, few_types = case
        result, expected, actual = imitate(
            name_correctness, correct, incorrect, few_vals, all_vals, few_types
        )
        self.assertTrue(
            result,
            "Сценарий imitate завершился с несовпадением:\n"
            f"{name_correctness=}, {few_vals=}, {all_vals=}, {few_types=}\n"
            f"Ожидалось:\n{expected}\nПолучено:\n{actual}",
        )

    return test_case


# Регистрируем каждый сценарий отдельно, сохраняя прежнее число обычных тестов.
for case_number, test_case_data in enumerate(TEST_CASES, start=1):
    setattr(
        CardImitationTests,
        f"test_imitate_case_{case_number}",
        _make_test(test_case_data),
    )


if __name__ == "__main__":
    # Поддерживаем запуск тестов как отдельного файла.
    unittest.main()
