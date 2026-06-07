from CardManager import CardManager
import json

CardManager_object = CardManager()

values = [
    {
        "type": "usual",
        "value": "0"
    },
    {
        "type": "usual",
        "value": "0"
    },
    {
        "type": "selflink",
        "value": "<number><number>"
    },
    {
        "type": "template",
        "value": "<number>.0"
    },
    {
        "type": "id",
        "value": "<number><number>>"
    },
    {
        "type": "selflink",
        "value": "<number><number>"
    },
    {
        "type": "template",
        "value": "<number>.0"
    },
    {
        "type": "id",
        "value": "<number><number>>"
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
        "value": "<selflink-template>"
    },
    {
        "type": "selflink-template",
        "value": "<selflink-template>"
    },
    {
        "type": "id-selflink",
        "value": "<id-selflink>"
    },
    {
        "type": "id-selflink",
        "value": "<id-selflink>"
    },
    {
        "type": "id-template",
        "value": "<id-template>"
    },
    {
        "type": "id-template",
        "value": "<id-template>"
    },
    {
        "type": "id-selflink-template",
        "value": "<id-selflink-template>"
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

CardManager_object.create_card(True, 1)
CardManager_object.create_card("<number>", values)
print("Errors:")
print()
CardManager_object.print_errors()