from notification_classes import error
from CardManager import CardManager
from Logger import Logger

class Zero:
    def __init__(self):
        # хранит ошибки, которые произошли при работе программы
        # и кладет их в Логгер
        self.errors = error.error() 
        self.some_CardManager_obects = []
        # self.Parser_object = Parser()
        self.Logger_object = Logger()

    def warp_drive(self):
        # Парсит и анлизирует входной json (+инклюды!!),
        # генерирует лог-файл,
        # модифицирует карты фильтрами

        # <!!!ВРЕМЕННЫЙ КОД!!!>
        CardManager_object1 = CardManager()
        CardManager_object2 = CardManager()
        self.some_CardManager_obects += [CardManager_object1, CardManager_object2]
        values = [
            {
                "type": "usual",
                "value": ["0"]
            },
            {
                "type": "usual",
                "value": ["0"]
            },
            {
                "type": "selflink",
                "value": 
                [
                    "<number><number>",
                    [
                        {
					        "link_name": "<number>",
					        "link_positions": [0, 8]
				        } 
                    ]
                ]
            },
            {
                "type": "template",
                "value": 
                [
                    "<number>.0",
                    [
                        {
					        "link_name": "<number>",
					        "link_positions": [0]
				        } 
                    ]
                ]
            },
            {
                "type": "id",
                "value": ["<number><number>>"]
            },
            {
                "type": "selflink",
                "value": ["<number><number>"]
            },
            {
                "type": "template",
                "value": ["<number>.0"]
            },
            {
                "type": "id",
                "value": ["<number><number>>"]
            },
            {
                "type": "some error type",
                "value": "SMTH"
            },
            {
                "some error key": "some error value"
            },
            {
                "type": "selflink-template",
                "value": ["<selflink-template>"]
            },
            {
                "type": "selflink-template",
                "value": ["<selflink-template>"]
            },
            {
                "type": "id-selflink",
                "value": ["<id-selflink>"]
            },
            {
                "type": "id-selflink",
                "value": ["<id-selflink>"]
            },
            {
                "type": "id-template",
                "value": ["<id-template>"]
            },
            {
                "type": "id-template",
                "value": ["<id-template>"]
            },
            {
                "type": "id-selflink-template",
                "value": ["<id-selflink-template>"]
            },
            {
                "type": "id-selflink-template",
                "value": "<id-selflink-template>"
            },
            [
                "type", "value"
            ],
            True
        ]

        CardManager_object1.create_card("<digit>", [{"type": "usual", "value": ["0"]}])
        CardManager_object1.create_card(True, 1)
        CardManager_object2.create_card("<number>", values)
        for one_CardManager_object in self.some_CardManager_obects:
            self.Logger_object.add_libruary(one_CardManager_object.get_libruary())
            self.Logger_object.add_error(one_CardManager_object.get_errors_as_list())

        # проверки на обработку некорректных типов данных в методах Логгера
        self.Logger_object.add_libruary("some string instead of list")
        self.Logger_object.add_error("some string instead of list")
        self.Logger_object.add_input_string(123)
        self.Logger_object.add_swap("some string instead of tuple")
        return self.Logger_object.get_log()
        # </!!!!ВРЕМЕННЫЙ КОД!!!>