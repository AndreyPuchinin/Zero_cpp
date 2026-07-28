import json
from collections.abc import Callable
from notification_classes import common_notification
from Card import Card

class CardManager():
	def __init__(self):
		self.name = None
		self.libruary = [] # хранит объекты класс Card
		self.notifications = common_notification.common_notification() # хранит ошибки, которые произошли при создании карточек
	
	def gen_value_links_info(self, value_str: str):
		'''
		input str
		output json 
		{
			"val": "<number><number>",
			"link_name": "<number>",
			"link_positions": [0, 8]
		}
		'''
		return {"val": value_str}

	def validate_value_type(self, real_value_type_str: str,\
							check_value_type_func: Callable[[str,str],bool],\
							value:str,\
							one_type_values_list: list):
		if check_value_type_func(self.name, real_value_type_str):
			informated_val_value = self.gen_value_links_info(value)
			one_type_values_list.append(informated_val_value)
			return True
		else:
			return False

	def if_type_from_user_is_rigth(self, user_value_type: str, value: str, values_to_fill: list):
		selflink_vals, usual_vals, templ_vals, selflink_templ_vals, \
		id_vals, id_selflink_vals, id_templ_vals, id_selflink_templ_vals = values_to_fill
		if user_value_type == 'selflink':
			if self.validate_value_type(user_value_type, self.is_selflink_value, value, selflink_vals):
				return True
		elif user_value_type == 'usual':
			if self.validate_value_type(user_value_type, self.is_usual_value, value, usual_vals):
				return True
		elif user_value_type == 'template':
			if self.validate_value_type(user_value_type, self.is_template_value, value, templ_vals):
				return True
		elif user_value_type == 'selflink-template':
			if self.validate_value_type(user_value_type, self.is_selflink_template_value, value, selflink_templ_vals):
				return True
		elif user_value_type == 'id':
			if self.validate_value_type(user_value_type, self.is_id_value, value, id_vals):
				return True
		elif user_value_type == 'id-selflink':
			if self.validate_value_type(user_value_type, self.is_id_selflink_value, value, id_selflink_vals):
				return True
		elif user_value_type == 'id-template':
			if self.validate_value_type(user_value_type, self.is_id_template_value, value, id_templ_vals):
				return True
		elif user_value_type == 'id-selflink-template':
			if self.validate_value_type(user_value_type, self.is_id_selflink_template_value, value, id_selflink_templ_vals):
				return True
		else:
			pass #логируем ошибку
		return False
	
	def if_type_from_user_is_wrong(self, value: str, values_to_fill: list):
		selflink_vals, usual_vals, templ_vals, selflink_templ_vals, \
		id_vals, id_selflink_vals, id_templ_vals, id_selflink_templ_vals = values_to_fill

		if  self.validate_value_type('selflink', self.is_selflink_value, value, selflink_vals):
			return True
		if self.validate_value_type('usual', self.is_usual_value, value, usual_vals):
			return True
		if self.validate_value_type('template', self.is_template_value, value, templ_vals):
			return True
		if self.validate_value_type('selflink-template', self.is_selflink_template_value, value, selflink_templ_vals):
			return True
		if self.validate_value_type('id', self.is_id_value, value, id_vals):
			return True
		if self.validate_value_type('id-selflink', self.is_id_selflink_value, value, id_selflink_vals):
			return True
		if self.validate_value_type('id-template', self.is_id_template_value, value, id_templ_vals):
			return True
		if self.validate_value_type('id-selflink-template', self.is_id_selflink_template_value, value, id_selflink_templ_vals):
			return True
		
		#логируем ошибку
		return False
		
	def values_validate(self, values: list):
		# инициализируем списки для каждого типа значений
		usual_vals = []
		selflink_vals = []
		templ_vals = []
		selflink_templ_vals = []
		id_vals = []
		id_selflink_vals = []
		id_templ_vals = []
		id_selflink_templ_vals = []

		values_to_fill = [
					usual_vals, 
					selflink_vals, 
					templ_vals, 
					selflink_templ_vals, 
					id_vals, 
					id_selflink_vals, 
					id_templ_vals, 
					id_selflink_templ_vals
				]
		
		# проходим по каждому значению и определяем его тип
		for i, one_value in enumerate(values):
			# проверяем, что значение имеет правильный формат 
			# (должно быть словарем с ключами "type" и "value")
			try:
				user_value_type = one_value.get('type')
				value_str = one_value.get('value')
			except AttributeError:
				self.notifications.add_error_with_stack_nodes(f"Invalid format of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				continue
			else:
				if not self.if_type_from_user_is_rigth(user_value_type, value_str, values_to_fill):
					self.if_type_from_user_is_wrong(value_str, values_to_fill)

		
		# формируем и возвращаем валидированные значения
		# (Важно: возврат должен быть здесь, после завершения цикла)
		validated_values = [
			usual_vals, 
			selflink_vals, 
			templ_vals, 
			selflink_templ_vals, 
			id_vals, 
			id_selflink_vals, 
			id_templ_vals, 
			id_selflink_templ_vals
		]
		
		return validated_values

	def create_card(self, name: str, values: list):
		# ловим ошибку типа параметра name и values
		
		got_error = False
		if not isinstance(name, str):
			self.notifications.add_error_with_stack_nodes(f"Invalid format of card name:\n{name}")
			got_error = True
		self.name = name

		if not isinstance(values, list):
			self.notifications.add_error_with_stack_nodes(f"Invalid format of card values:\n{json.dumps(values, indent=4)}")
			got_error = True

		if got_error:
			return

		# использует value_validate
		# подтягивает из него валидированные значения
		validated_usual_vals, selflink_vals, templ_vals, \
			selflink_templ_vals, id_vals, id_selflink_vals, id_templ_vals, \
			id_selflink_templ_vals= self.values_validate(values)

		# ...и передает их в объект карточки
		Card_object = Card(name, validated_usual_vals, selflink_vals, templ_vals, \
			selflink_templ_vals, id_vals, id_selflink_vals, id_templ_vals, \
			id_selflink_templ_vals)
		
		Card_notifications = Card_object.get_notifications()
		self.notifications.add_notifications(Card_notifications)
		
		# печатаем карточку для проверки
		# print(Card_object.get_card()) # печатаем карточку

		# кладем карточку в библиотеку
		self.libruary.append(Card_object) 

		# определять все типы значений - позже, id - через Парсер
		# передавать их в объект карточки
		# и класть карточку в библиотеку
		pass

	# Сигнатура is_функций одинаковая, даже если не все аргументы нужны,
	# потому что мы передаем is_функцию в value_validate_type как аргумент
	def is_selflink_value(self, name: str, value: str):
		return name in value

	def is_template_value(self, name: str, value: str):
		pass

	def is_selflink_template_value(self, name: str, value: str):
		return self.is_selflink_value(name, value) and self.is_template_value(name, value)

	def is_id_value(self, name: str, value: str):
		# Uses Parser to determine if the value is an ID
		pass

	def is_id_template_value(self, name: str, value: str):
		return self.is_id_value(name, value) and self.is_template_value(name, value)

	def is_id_selflink_value(self, name: str, value: str):
		return self.is_id_value(name, value) and self.is_selflink_value(name, value)

	def is_id_selflink_template_value(self, name: str, value: str):
		return self.is_id_value(name, value) and self.is_selflink_value(name, value) and self.is_template_value(name, value)

	def is_usual_value(self, name: str, value: str):
		# использует 
		# is_self_link_value
		# is_template_value
		# is_id_value
		pass

	# def parse(self):
	#	parser_object = Parser()
	#	parser_object.forward_usual_swaps()

	def get_libruary(self):
		res_text = []
		for one_card in self.libruary:
			res_text += [one_card.get_card()]
		return res_text

	def get_notifications_as_json(self):
		return self.notifications.get_all_notifications()

	def get_notifications_as_str(self):
		res_text = ''
		for i, one_notification in enumerate(self.notifications.get_all_notifications()):
			res_text += f"#{i+1}: {one_notification}\n"
		return res_text