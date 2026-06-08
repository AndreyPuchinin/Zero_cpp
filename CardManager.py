import json
from notification_classes import error
from Card import Card

class CardManager():
	def __init__(self):
		self.libruary = [] # хранит объекты класс Card
		self.errors = error.error() # хранит ошибки, которые произошли при создании карточек
	
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
				val_type = one_value.get('type')
				val_value = one_value.get('value')
			except AttributeError:
				self.errors.create_notification(f"Invalid format of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				continue

			# Внутренняя функция (замыкание). 
			# Она имеет доступ ко всем переменным, объявленным выше, и в цикле ниже.
			def __inner():
				if val_type is None:
					self.errors.create_notification(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				elif val_type == 'selflink':
					selflink_vals.append(val_value)
				elif val_type == 'usual':
					usual_vals.append(val_value)
				elif val_type == 'template':
					templ_vals.append(val_value)
				elif val_type == 'selflink-template':
					selflink_templ_vals.append(val_value)
				elif val_type == 'id':
					id_vals.append(val_value)
				elif val_type == 'id-selflink':
					id_selflink_vals.append(val_value)
				elif val_type == 'id-template':
					id_templ_vals.append(val_value)
				elif val_type == 'id-selflink-template':
					id_selflink_templ_vals.append(val_value)
				else:
					self.errors.create_notification(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")

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
			self.errors.create_notification(f"Invalid format of card name:\n{name}")
			got_error = True
	
		if not isinstance(values, list):
			self.errors.create_notification(f"Invalid format of card values:\n{json.dumps(values, indent=4)}")
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
		pass

	def is_id_template_value(self):
		return self.is_id_value() and self.is_template_value()

	def is_id_selflink_value(self):
		return self.is_id_value() and self.is_selflink_value()

	def is_id_selflink_template_value(self):
		return self.is_id_value() and self.is_selflink_value() and self.is_template_value()

	def is_usual_value(self):
		# использует is_self_link_value
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

	def get_errors_as_list(self):
		return self.errors.get_all_notifications()

	def get_errors_as_str(self):
		res_text = ''
		for i, one_error in enumerate(self.errors.get_all_notifications()):
			res_text += f"#{i+1}: {one_error}\n"
		return res_text