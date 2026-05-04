import json
from typing import List
print("Zero second version!")


class Card:
	def __init__(self, name: str, usual_vals: List[str],
			selflink_vals: List[str], templ_vals: List[str], selflink_templ_vals: List[str],
            id_vals: List[str]):
		# Если self.name == None, карточка недействительна;
		# также недействительна, если все контейнеры значений пустые

		self.name = name
		self.usual_vals = usual_vals
		self.selflink_vals = selflink_vals
		self.templ_vals = templ_vals
		self.selflink_templ_vals = selflink_templ_vals
		self.id_vals = id_vals

		# Проверяем значения карточек
		# Если контейнер значений не список, то делаем его пустым списком 
		# Если значение не строка, то делаем его пустой строкой
		# Если все значения оказались пустыми строками, то карточка недействительна
		vals_types = [usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals]
		
		self_vals_types = [self.usual_vals,
            self.selflink_vals, self.templ_vals, self.selflink_templ_vals,
            self.id_vals]
		
		contains_value = False
		for i, vals_one_type in enumerate(vals_types):
			if type(vals_one_type) != List:
				self_vals_one_type = self_vals_types[i]
				self_vals_one_type = []
			for j, one_val_of_one_type in enumerate(vals_one_type):
				if type(one_val_of_one_type) != str:
					self_one_val_of_one_type = self_vals_types[i][j]
					self_one_val_of_one_type = ''
				else:
					contains_value = True

		if not contains_value:
			self.usual_vals = []
			self.selflink_vals = []
			self.templ_vals = []
			self.selflink_templ_vals = []
			self.id_vals = []
			return
		
		# Если имя - пустая строка, то карточка недействительна
		if name == '' or type(name) != str:
			self.name = None
			self.usual_vals = []
			self.selflink_vals = []
			self.templ_vals = []
			self.selflink_templ_vals = []
			self.id_vals = []
			return
			

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