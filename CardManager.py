import json
from notification_classes import common_notification
from Card import Card

class CardManager():
	def __init__(self):
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

	def validate_value_type(self, value_type, value_str: str, func, values_list, inner): # какого типа func, inner?
		# Сделать замыканием?
		if value_type == value_str and func(<параметры>):
			informated_val_value = self.gen_value_links_info(value_str)
			values_list.append(informated_val_value)
		else:
			value_type = ''
			inner(<value_type?>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
			  
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

		# проходим по каждому значению и определяем его тип
		for i, one_value in enumerate(values):
			# проверяем, что значение имеет правильный формат 
			# (должно быть словарем с ключами "type" и "value")
			try:
				value_type = one_value.get('type')
				value_str = one_value.get('value')
			except AttributeError:
				self.notifications.add_error_with_stack_nodes(f"Invalid format of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				continue

			# Внутренняя функция (замыкание). 
			# Она имеет доступ ко всем переменным, объявленным выше, и в цикле ниже.
			def __inner():
				if value_type is None:
						self.notifications.add_error_with_stack_nodes(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				elif value_type == '' or value_type == 'selflink':
					self.validate_value_type(value_type, 'selflink', self.is_selflink_value, selflink_vals, __inner)
			  
			  	elif value_type == '' or value_type == 'usual':
					self.validate_value_type(value_type, 'usual', self.is_usual_value, usual_vals, __inner)

				elif value_type == '' or value_type == 'template':
					self.validate_value_type(value_type, 'template', self.is_template_value, template_vals, __inner)

				elif value_type == '' or value_type == 'selflink-template':
					self.validate_value_type(value_type, 'selflink-template', self.is_selflink-template_value, selflink-template_vals, __inner)
				
				elif value_type == '' or value_type == 'id':
					self.validate_value_type(value_type, 'id', self.is_id_value, id_vals, __inner)
				
				elif value_type == '' or value_type == 'id-selflink':
					self.validate_value_type(value_type, 'id-selflink', self.is_id_selflink_value, id_selflink_vals, __inner)
				
				elif value_type == '' or value_type == 'id-template':
					self.validate_value_type(value_type, 'id-template', self.is_id_template_value, id_template_vals, __inner)
				
				elif value_type == '' or value_type == 'id-selflink-template':
					self.validate_value_type(value_type, 'id-selflink-template', self.is_id_selflink_template_value, id_selflink_template_vals, __inner)
				
				else:
					self.notifications.add_error_with_stack_nodes(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")

'''
			def __inner():
				if value_type is None:
						self.notifications.add_error_with_stack_nodes(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				elif value_type == '' or value_type == 'selflink':
					if value_type == 'selflink' and self.is_selflink_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						selflink_vals.append(informated_val_value)
					else:
						value_type = ''
						__inner(<value_type?>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
			  
			  	elif value_type == '' or value_type == 'usual':
					if value_type == 'usual' and self.is_usual_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						usual_vals.append(informated_val_value)
					else:
						value_type = ''
						__inner(<value_type?>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
			  
				elif value_type == '' or value_type == 'usual':
					# if is_usual_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						usual_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
					#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				elif value_type == '' or value_type == 'template':
					# if is_template_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						templ_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
					#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				elif value_type == '' or value_type == 'selflink-template':
					# if is_selflink_template_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						selflink_templ_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
						#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				elif value_type == '' or value_type == 'id':
					# if is_id_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						id_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
					#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				elif value_type == '' or value_type == 'id-selflink':
					# if is_id_selflink_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						id_selflink_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
					#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				elif value_type == '' or value_type == 'id-template':
					# if is_id_template_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						id_templ_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
					#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				elif value_type == '' or value_type == 'id-selflink-template':
					# if is_id_selflink_template_value(<параметры>):
						informated_val_value = self.gen_value_links_info(value_str)
						id_selflink_templ_vals.append(informated_val_value)
					# elif <глубина рекурсии < 3>:
					#	__inner(<параметр глубины>) # рекурсивно вызываем замыкание, чтобы проверить другие типы значений
				else:
					self.notifications.add_error_with_stack_nodes(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
'''
			# вызываем замыкание для добавления значения в нужный список
			__inner()
		
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

	def is_selflink_value(self, name: str, value: str):
		return name in value

	def is_template_value(self):
		pass

	def is_selflink_template_value(self):
		return self.is_selflink_value() and self.is_template_value()

	def is_id_value(self):
		# Uses Parser to determine if the value is an ID
		pass

	def is_id_template_value(self):
		return self.is_id_value() and self.is_template_value()

	def is_id_selflink_value(self):
		return self.is_id_value() and self.is_selflink_value()

	def is_id_selflink_template_value(self):
		return self.is_id_value() and self.is_selflink_value() and self.is_template_value()

	def is_usual_value(self):
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