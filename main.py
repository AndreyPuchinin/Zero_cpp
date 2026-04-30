import json

print("Zero first version!")

def add_card(name, usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals):
    "возвращаем словарь ключ значение"
    dictionary = {
				"name": name,
				"usual_vals": usual_vals,
				"selflink_vals": selflink_vals,
				"templ_vals": templ_vals,
                "selflink_templ_vals": selflink_templ_vals,
				"id_vals": id_vals
			}
    return dictionary


card1 = add_card("<number>",
				["1", "2"],
					[
						{
							"val": "<number><number>",
							"link_name": "<number>",
							"link_positions": [0]
						}
					],
				[],
                [],
				 [])
print(type(card1))