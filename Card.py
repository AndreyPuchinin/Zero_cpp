import json
from success_class.success import success
from typing import List
from notification_classes import common_notification
#print("Zero second version!")


class Card:
	def __init__(self, name: str, usual_vals: List[list],
			selflink_vals: List[list], templ_vals: List[list], selflink_templ_vals: List[list],
            id_vals: List[list], id_selflink_vals: List[list], id_templ_vals: List[list],
			id_selflink_templ_vals: List[list]):
		# Если self.name == None, карточка недействительна;
		# также недействительна, если все контейнеры значений пустые
		self.notifications = common_notification.common_notification()
		self.success = success()
		self.success.set_successful()

		self.name = name
		self.usual_vals = usual_vals
		self.selflink_vals = selflink_vals
		self.templ_vals = templ_vals
		self.selflink_templ_vals = selflink_templ_vals
		self.id_vals = id_vals
		self.id_selflink_vals = id_selflink_vals
		self.id_templ_vals = id_templ_vals
		self.id_selflink_templ_vals = id_selflink_templ_vals

		# Проверяем значения карточек
		# Если контейнер значений не список, то делаем его пустым списком 
		# Если значение не строка, то делаем его пустой строкой
		# Если все значения оказались пустыми строками, то карточка недействительна
		vals_types = [usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals, id_selflink_vals, id_templ_vals, id_selflink_templ_vals]
		
		self_vals_types = [self.usual_vals,
            self.selflink_vals, self.templ_vals, self.selflink_templ_vals,
            self.id_vals, self.id_selflink_vals, self.id_templ_vals, 
			self.id_selflink_templ_vals]
		
		contains_value = False 			# False = точно unsucessful
		exists_uncorrect_value = False  # False = точно sucessful
		for i, vals_one_type in enumerate(vals_types):
			if not isinstance(vals_one_type, List):
				self_vals_one_type = []
				self_vals_types[i] = self_vals_one_type
				exists_uncorrect_value = True
			else:
				j = 0
				while j < len(vals_one_type):
					one_val_of_one_type = vals_one_type[j]

					if type(one_val_of_one_type) != dict or \
	   						type(one_val_of_one_type.get("val",None)) != str:
						# self_one_val_of_one_type = None
						# self_vals_types[i][j] = self_one_val_of_one_type
						self.notifications.add_warning_with_stack_nodes(f"Value {self_vals_types[i][j]} excepted from Card")
						del self_vals_types[i][j]				
						exists_uncorrect_value = True
					else:
						contains_value = True
						j += 1
	
		# Если имя - не строка, имя - пустая строка или нет ни одного корректного значения, то карточка недействительна
		if type(name[0]) != str or name[0] == '' or not contains_value:
			self.name = [None]
			self.usual_vals = []
			self.selflink_vals = []
			self.templ_vals = []
			self.selflink_templ_vals = []
			self.id_vals = []
			self.id_selflink_vals = []
			self.id_templ_vals = []
			self.id_selflink_templ_vals = []
			self.success.set_unsuccessful()
			return
		
		# Если имя - непустая строка
		if type(name[0]) == str and name[0] != '':
			# Если было хотя бы одно неправильное значение
			if exists_uncorrect_value:
				self.success.set_half_successful()
			# Если все были правильные
			else:
				self.success.set_successful()
				return
	
	def get_card(self):
		result_json = {
			"status": self.success.get_state(),
			"name": self.name,
			"usual_vals": self.usual_vals,
			"selflink_vals": self.selflink_vals,
			"templ_vals": self.templ_vals,
			"selflink_templ_vals": self.selflink_templ_vals,
			"id_vals": self.id_vals,
			"id_selflink_vals": self.id_selflink_vals,
			"id_templ_vals": self.id_templ_vals,
			"id_selflink_templ_vals": self.id_selflink_templ_vals
		}
	
		return result_json
	
	def get_notifications(self):
		return self.notifications.get_all_notifications()

def imitate(name_correctness: bool, correct, incorrect, few_vals: int, all_vals: int, few_types: int):
	"""
	name_correctness : bool - является ли имя корректным
	correct - что вставлять в качестве корректного значения или имена
	incorrect - что вставлять в качестве НЕкорректного значения или имена
	few_vals - количество корректный значений в типе
	all_vals - общее количество значений в типе
	few_types - количество корректных типов
	"""
	# correct = [correct]
	# incorrect = [incorrect]
	# устанавливаем корректное или некорректное имя
	if name_correctness and few_vals != 0 and few_types > 0:
		name = [correct]
	else:
		name = [incorrect]
	
	usual_vals = []
	selflink_vals = []
	templ_vals = []
	selflink_templ_vals = []
	id_vals = []
	id_selflink_vals = []
	id_templ_vals = []
	id_selflink_templ_vals = []

	vals_types = [usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals, id_selflink_vals, id_templ_vals, id_selflink_templ_vals]
	
	# expexted
	exp_usual_vals = []
	exp_selflink_vals = []
	exp_templ_vals = []
	exp_selflink_templ_vals = []
	exp_id_vals = []
	exp_id_selflink_vals = []
	exp_id_templ_vals = []
	exp_id_selflink_templ_vals = []

	exp_vals_types = [exp_usual_vals,
            exp_selflink_vals, exp_templ_vals, exp_selflink_templ_vals,
            exp_id_vals, exp_id_selflink_vals, exp_id_templ_vals, exp_id_selflink_templ_vals]
	
	# Формируем значения для ввода в Card
	for i, one_type in enumerate(vals_types):
		if i < few_types:
			for j in range(all_vals):
				if j < few_vals:
					one_type += [{"val": correct}]
					exp_vals_types[i] += [{"val": correct}]
				else:
					one_type += [{"val": incorrect}]
		else:
			vals_types[i] = {"val": incorrect}  # Нужен ИНФОРМАТИВНЫЙ json 
			exp_vals_types[i] = []

	# выводим список типов значений	
	# print('\nval_types = ', vals_types)

	# формируем карточку
	new_card = Card(name, usual_vals,
            selflink_vals, templ_vals, selflink_templ_vals,
            id_vals, id_selflink_vals, id_templ_vals, id_selflink_templ_vals)

	# печатаем карточку
	# print(new_card.get_card())

	# если имя карточки некорректно, зануляем все значения
	if not name_correctness or few_vals <= 0:
		name = [None]
		exp_usual_vals = []
		exp_selflink_vals = []
		exp_templ_vals = []
		exp_selflink_templ_vals = []
		exp_id_vals = []
		exp_id_selflink_vals = []
		exp_id_templ_vals = []
		exp_id_selflink_templ_vals = []
	
	expected_status = ''

	# Формируем ожидаемый вывод теста
	if few_vals == all_vals:
		expected_status = f'successful'

	if all_vals > few_vals >= 0  and few_types != 0 and name_correctness:
		expected_status = f'half_successful'

	if few_vals <= 0 or few_types <= 0 or not name_correctness:
		expected_status = f'unsuccessful'

	expected_json = {
		"status": expected_status,
		"name": name,
		"usual_vals": exp_usual_vals,
		"selflink_vals": exp_selflink_vals,
		"templ_vals": exp_templ_vals,
		"selflink_templ_vals": exp_selflink_templ_vals,
		"id_vals": exp_id_vals,
		"id_selflink_vals": exp_id_selflink_vals,
		"id_templ_vals": exp_id_templ_vals,
		"id_selflink_templ_vals": exp_id_selflink_templ_vals
	}

	# выводим ожидаемый вывод теста 
	# print(expected_json)
	# print(new_card.get_card())
	# сравниваем ожидаемый вывод теста и реальный вывод
	# print(expected == new_card.get_card())
	
	return expected_json == new_card.get_card(), expected_json, new_card.get_card()


def global_tests_function():
	failed_tests = []

	# Функция-замыкание для одного теста
	def one_test(name_correctness: bool, correct, incorrect, few_vals: int, all_vals: int, few_types: int):
		result, expected, got = imitate(name_correctness, correct, incorrect, few_vals, all_vals, few_types)
		
		# print(f'{result=}\n\nexpected:\n{expected}\ngot:\n{got}\n')

		# Если тест не сработал - накапливаем
		if not result:
			# .extend изменяет существующий список, не создавая новую локальную переменную
			# Поэтому не будет возникать ошибки:
			# UnboundLocalError: cannot access local variable 'failed_tests' where it is not associated with a value
			failed_tests.extend([[name_correctness, few_vals, all_vals, few_types, expected, got]])
		
		return failed_tests

	return one_test

if __name__ == "__main__":
	# раскомментариваем global_tests если нужны ручные тесты
	global_tests = global_tests_function()

	# Если имя - не строка, имя - пустая строка или нет ни одного корректного значения, то карточка недействительна
	global_tests(False, 'good', None, 0, -1, 0)
	global_tests(False, 'good', None, 0, -1, 0)
	global_tests(True, 'good', None, 0, 0, 2)

	# Если имя - непустая строка И
	# Если было хотя бы одно неправильное значение
	global_tests(True, 'good', None, 1, 4, 1)
	global_tests(True, 'good', None, 2, 4, 2)
	global_tests(True, 'good', None, 4, 5, 2)

	# Если имя - непустая строка И
	# Если все были правильные
	all_failed_tests = global_tests(True, 'good', None, 4, 4, 8)

	#раскомментариваем DANGER_all_tests_zone если нужно проверить на всех случаях

	# result, expected, card_output = imitate(True, 'good', None, 2, 5, 2)
	# # print(f'{result}\n\n{expected}\n\n{card_output}')
# 
	# DANGER_all_tests_zone = global_tests_function()
	# tests_i = 0
	# for name_correctness in [True, False]:
	# 	for all_types in range(5):
	# 		for all_vals in range(5):
	# 			for few_vals in range(all_vals):
	# 				tests_i += 1 
	# 				DANGER_all_tests_zone(name_correctness, 'good', None, few_vals-2, all_vals-2, all_types-2)
	# all_failed_tests = DANGER_all_tests_zone(True,'final_test',None,0,0,0)
	# print(len(all_failed_tests),'TESTS FAILED FROM '+str(tests_i)+':\n')

	got_error = False
	for i, one_test in enumerate(all_failed_tests):
		name_correctness, few_vals, all_vals, few_types, expected, got = one_test
		print('Failed test #'+str(i+1)+':\n')
		print(f'{name_correctness=}, {few_vals=}, {all_vals=}, {few_types=}\n')
		print(f'Expected:\n\n{json.dumps(expected, indent=2)}\n')
		print(f'Got:\n\n{json.dumps(got, indent=2)}\n')
		print('========\n')
		got_error = True
	
	if not got_error:
		print('ALL TESTS ABOUT CARD CREATING PASSED SUCCESFULY!\n')
