import json
from success_class.success import success
from typing import List
print("Zero second version!")


class Card:
	def __init__(self, name: str, usual_vals: List[str],
			selflink_vals: List[str], templ_vals: List[str], selflink_templ_vals: List[str],
            id_vals: List[str]):
		# Если self.name == None, карточка недействительна;
		# также недействительна, если все контейнеры значений пустые
		self.success = success()
		self.success.set_successful()

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
		
		contains_value = False 			# False = точно unsucessful
		exists_uncorrect_value = False  # False = точно sucessful
		for i, vals_one_type in enumerate(vals_types):
			if not isinstance(vals_one_type, List):
				self_vals_one_type = []
				self_vals_types[i] = self_vals_one_type
				exists_uncorrect_value = True
			else:
				for j, one_val_of_one_type in enumerate(vals_one_type):
					if type(one_val_of_one_type) != str:
						self_one_val_of_one_type = ''
						self_vals_types[i][j] = self_one_val_of_one_type
						exists_uncorrect_value = True
					else:
						contains_value = True
	
		# Если имя не строка, имя - пустая строка или нет ни одного корректного, то карточка недействительна
		if type(name) != str or name == '' or not contains_value:
			self.name = None
			self.usual_vals = []
			self.selflink_vals = []
			self.templ_vals = []
			self.selflink_templ_vals = []
			self.id_vals = []
			self.success.set_unsuccessful()
			return
		
		if type(name) == str and name != '':
			if exists_uncorrect_value:
				self.success.set_half_successful()
			else:
				self.success.set_successful()
				return
	
	def get_card(self):
		result_str = f'status={self.success.get_state()}\n'
		result_str += f'name={self.name}\n'
		
		result_str += f'usual_vals={[one_val for one_val in self.usual_vals]}\n'
		result_str += f'selflink_vals={[one_val for one_val in self.selflink_vals]}\n'
		result_str += f'templ_vals={[one_val for one_val in self.templ_vals]}\n'
		result_str += f'selflink_templ_vals={[one_val for one_val in self.selflink_templ_vals]}\n'
		result_str += f'id_vals={[one_val for one_val in self.id_vals]}\n'
		return result_str


def add_card(name, usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals):
    """возвращаем словарь ключ значение"""
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
print(type(card1),'\n')
card2 = Card("<number>",
				["1", "2"],
				[						
				"<number><number>",
				"<number>",
				"link_positions"
				],
				[],
                [],
				[])
print(card2.get_card())

def imitate(correct_name: bool, correct, incorrect, few_vals: int, all_vals: int, few_types: int):
	if correct_name:
		name = correct
	else:
		name = incorrect
	
	usual_vals = []
	selflink_vals = []
	templ_vals = []
	selflink_templ_vals = []
	id_vals = []

	vals_types = [usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals]
	
	for i, one_type in enumerate(vals_types):
		if i < few_types:
			for j in range(all_vals):
				if j < few_vals:
					one_type += [correct]
				else:
					one_type += [incorrect]
		else:
			vals_types[i] = incorrect
		
	#print('val_types = ', vals_types)
	new_card = Card(name, usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals)

	print(new_card.get_card())

	if not correct_name:
		name = None
		usual_vals = []
		selflink_vals = []
		templ_vals = []
		selflink_templ_vals = []
		id_vals = []
	
	expected = f'status=unsuccessful\n'

	expected += f'name={name}\n'
	expected += f'usual_vals={usual_vals}\n'
	expected += f'selflink_vals={selflink_vals}\n'
	expected += f'templ_vals={templ_vals}\n'
	expected += f'selflink_templ_vals={selflink_templ_vals}\n'
	expected += f'id_vals={id_vals}\n'
	print(expected)
	print(expected == new_card.get_card())

imitate(False, None, 'c++', 0, -1, 0)
