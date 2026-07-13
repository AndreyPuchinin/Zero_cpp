from email import errors

from Zero import Zero
import json

values = [
            {
                "type": "usual",
                "value": "0"
            },
            {
                "type": "usual",
                "value": "0"
            },
            # {
            #     "type": "selflink",
            #     "value": 
            #     [
            #         "<number><number>",
            #         [
            #             {
			# 		        "link_name": "<number>",
			# 		        "link_positions": [0, 8]
			# 	        } 
            #         ]
            #     ]
            # },
            # {
            #     "type": "template",
            #     "value": 
            #     [
            #         "<number>.0",
            #         [
            #             {
			# 		        "link_name": "<number>",
			# 		        "link_positions": [0]
			# 	        } 
            #         ]
            #     ]
            # },
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
            # {
            #     "some error key": "some error value"
            # },
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
            # [
            #     "type", "value"
            # ],
            # True
        ]

Zero_object = Zero()
Zero_output = Zero_object.warp_drive(values)
cards = Zero_output.get('cards')
input_string = Zero_output.get('input_string')
swaps = Zero_output.get('swaps')
notifications = Zero_output.get('notifications')

result_str = ""

result_str += 'CARDS:\n\n'

for i, one_card in enumerate(cards):
    result_str += f"Card #{i+1}:\n"
    result_str += f"status={one_card.get("status", "")}\n"
    result_str += f"name={one_card.get('name', '')}\n"
    result_str += f"usual_vals={one_card.get('usual_vals', '')}\n"
    result_str += f"selflink_vals={one_card.get('selflink_vals', '')}\n"
    result_str += f"templ_vals={one_card.get('templ_vals', '')}\n"
    result_str += f"selflink_templ_vals={one_card.get('selflink_templ_vals', '')}\n"
    result_str += f"id_vals={one_card.get('id_vals', '')}\n"
    result_str += f"id_selflink_vals={one_card.get('id_selflink_vals', '')}\n"
    result_str += f"id_templ_vals={one_card.get('id_templ_vals', '')}\n"
    result_str += f"id_selflink_templ_vals={one_card.get('id_selflink_templ_vals', '')}\n"
    result_str += '\n'

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
if isinstance(notifications, dict) and isinstance(notifications["errors"], list) \
    and notifications["errors"] == []:
    result_str += ("\nNo errors found.\n\n")
else:
    for error_i, one_error in enumerate(notifications["errors"]):
        result_str += f"\nError #{error_i+1}/{len(notifications["errors"])}:\n\n"
        for current_level in one_error.get("Levels", ""):
            Levels_N = current_level.get("Levels_N", "")
            currnt_level = current_level.get("Level", "")
            Module = current_level.get("Module", "")
            Line = current_level.get("Line", "")
            Column = current_level.get("Column", "")
            Description = current_level.get("Description", "")
            Code_line = current_level.get("Code_line", "")
            result_str += (
                f"-Level: {currnt_level}/{Levels_N}\n"
                f"--Module: {Module}\n"
                f"--Line: {Line}\n"
                f"--Column: {Column}\n"
                f"--Description: {Description}\n"
                f"--Code_line: \"{Code_line}\"\n\n"
            )
        Error_text = one_error.get("Error_text", "")
        result_str += f"Error_text: \"{Error_text}\"\n\n"

result_str += '-'*50 + '\n'

result_str += f"\nWarning:\n"
if isinstance(notifications, dict) and isinstance(notifications["warnings"], list) \
    and notifications["warnings"] == []:
    result_str += "\nNo warnings found.\n\n"
else:
    for warning_i, one_warning in enumerate(notifications["warnings"]):
        result_str += f"\nWarning #{warning_i+1}/{len(notifications['warnings'])}:\n\n"
        for current_level in one_warning.get("Levels", ""):
            Levels_N = current_level.get("Levels_N", "")
            currnt_level = current_level.get("Level", "")
            Module = current_level.get("Module", "")
            Line = current_level.get("Line", "")
            Column = current_level.get("Column", "")
            Description = current_level.get("Description", "")
            Code_line = current_level.get("Code_line", "")
            result_str += (
                f"-Level: {currnt_level}/{Levels_N}\n"
                f"--Module: {Module}\n"
                f"--Line: {Line}\n"
                f"--Column: {Column}\n"
                f"--Description: {Description}\n"
                f"--Code_line: \"{Code_line}\"\n\n"
            )
        Warning_text = one_warning.get("Warning_text", "")
        result_str += f"Warning_text: \"{Warning_text}\"\n\n"

result_str += '-'*50 + '\n'

result_str += f"\nMessage:\n"
if isinstance(notifications, dict) and isinstance(notifications["messages"], list) \
    and notifications["messages"] == []:
    result_str += "\nNo messages found.\n\n"
else:
    for message_i, one_message in enumerate(notifications["messages"]):
        result_str += f"\nMessage #{message_i+1}/{len(notifications['messages'])}:\n\n"
        for current_level in one_message.get("Levels", ""):
            Levels_N = current_level.get("Levels_N", "")
            currnt_level = current_level.get("Level", "")
            Module = current_level.get("Module", "")
            Line = current_level.get("Line", "")
            Column = current_level.get("Column", "")
            Description = current_level.get("Description", "")
            Code_line = current_level.get("Code_line", "")
            result_str += (
                f"-Level: {currnt_level}/{Levels_N}\n"
                f"--Module: {Module}\n"
                f"--Line: {Line}\n"
                f"--Column: {Column}\n"
                f"--Description: {Description}\n"
                f"--Code_line: \"{Code_line}\"\n\n"
            )
        Message_text = one_message.get("Message_text", "")
        result_str += f"Message_text: \"{Message_text}\"\n\n"

result_str += '-'*50 + '\n'

result_str += f"\nNote:\n"
if isinstance(notifications, dict) and isinstance(notifications["notes"], list) \
      and notifications["notes"] == []:
    result_str += "\nNo notes found.\n\n"
else:
    for note_i, one_note in enumerate(notifications["notes"]):
        result_str += f"\nNote #{note_i+1}/{len(notifications['notes'])}:\n\n"
        for current_level in one_note.get("Levels", ""):
            Levels_N = current_level.get("Levels_N", "")
            currnt_level = current_level.get("Level", "")
            Module = current_level.get("Module", "")
            Line = current_level.get("Line", "")
            Column = current_level.get("Column", "")
            Description = current_level.get("Description", "")
            Code_line = current_level.get("Code_line", "")
            result_str += (
                f"-Level: {currnt_level}/{Levels_N}\n"
                f"--Module: {Module}\n"
                f"--Line: {Line}\n"
                f"--Column: {Column}\n"
                f"--Description: {Description}\n"
                f"--Code_line: \"{Code_line}\"\n\n"
            )
        Note_text = one_note.get("Note_text", "")
        result_str += f"Note_text: \"{Note_text}\"\n\n"

result_str += '='*50 + '\n'

with open("ZeroLog.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(Zero_output, indent=4, ensure_ascii=False))

with open("ZeroLog.txt", "w", encoding="utf-8") as file:
    file.write(result_str)

print("Log files generated successfully!")
print("Open 'ZeroLog.json' and 'ZeroLog.txt' to view the logs.")