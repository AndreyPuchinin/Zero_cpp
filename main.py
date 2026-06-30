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

print('CARDS:\n')

for i, one_card in enumerate(cards):
    print(f"Card #{i+1}:\n{one_card}\n")

print('' + '='*50 + '\n')

print(f"Input string:\n{input_string}\n")

print('' + '='*50 + '\n')
print('SWAPS:\n')

for i, one_swap in enumerate(swaps):
    print(f"Swap #{i+1}:\n{one_swap}\n")

print('' + '='*50 + '\n')

print('NOTIFICATIONS:\n')


print("Errors:\n")
for i, one_error in enumerate(notifications[0]["errors"]):
	print(f"Error #{i+1}:\n{one_error}\n")

print('' + '-'*50 + '\n')
print(f"Warning:\n")
for i, one_warning in enumerate(notifications[1]["warnings"]):
	print(f"Warning #{i+1}:\n{one_warning}\n")

print('' + '-'*50 + '\n')
print(f"Note:\n")
for i, one_note in enumerate(notifications[2]["notes"]):
	print(f"Note #{i+1}:\n{one_note}\n")

print('' + '-'*50 + '\n')
print(f"Message:\n")
for i, one_message in enumerate(notifications[3]["messages"]):
	print(f"Message #{i+1}:\n{one_message}\n")
				
print('' + '='*50 + '\n')