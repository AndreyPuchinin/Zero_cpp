from email.mime import text

from Zero import Zero
import json

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

Zero_object = Zero()
Zero_output = Zero_object.warp_drive(values)
cards = Zero_output.get('cards')
input_string = Zero_output.get('input_string')
swaps = Zero_output.get('swaps')
notifications = Zero_output.get('notifications')

result_str = ""

result_str += '\nCARDS:\n\n'

for i, one_card in enumerate(cards):
    result_str += f"Card #{i+1}:\n{one_card}\n\n"

result_str += '='*50 + '\n'

result_str += f"\nInput string:\n\"{input_string}\"\n"

result_str += '\n' + '='*50 + '\n'
result_str += '\nSWAPS:\n'

if swaps == []:
    result_str += "\nNo swaps found.\n"
else:
    for i, one_swap in enumerate(swaps):
        result_str += f"\nSwap #{i+1}:\n{one_swap}\n"

result_str += '\n' + '='*50 + '\n'

result_str += '\n' + 'NOTIFICATIONS:\n'

result_str += '\n' + "Errors:\n"
if notifications[0]["errors"] == []:
	result_str += ("\nNo errors found.\n")
else:
	for i, one_error in enumerate(notifications[0]["errors"]):
		result_str += f"\nError #{i+1}:\n{one_error}\n"

result_str += '\n' + '-'*50 + '\n'

result_str += f"\nWarning:\n"
if notifications[1]["warnings"] == []:
    result_str += "\nNo warnings found.\n"
else:
	for i, one_warning in enumerate(notifications[1]["warnings"]):
		result_str += f"\nWarning #{i+1}:\n{one_warning}\n"
	
result_str += '\n' + '-'*50 + '\n'

result_str += f"\nMessage:\n"
if notifications[3]["messages"] == []:
    result_str += "\nNo messages found.\n"
else:
	for i, one_message in enumerate(notifications[3]["messages"]):
		result_str += f"\nMessage #{i+1}:\n{one_message}\n"   
				
result_str += '\n' + '-'*50 + '\n'

result_str += f"\nNote:\n"
if notifications[2]["notes"] == []:
    result_str += "\nNo notes found.\n"
else:
	for i, one_note in enumerate(notifications[2]["notes"]):
		result_str += f"\nNote #{i+1}:\n{one_note}\n"

result_str += '\n' + '='*50 + '\n'

with open("ZeroLog.txt", "w", encoding="utf-8") as file:
    file.write(result_str)