import json
from notification_classes import common_notification
from Card import Card

class CardManager():
	def __init__(self):
		self.libruary = [] # хранит объекты класс Card
		self.notifications = common_notification.common_notification() # хранит ошибки, которые произошли при создании карточек
	
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
				self.notifications.add_error_with_stack_nodes(f"Invalid format of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
				continue

			# Внутренняя функция (замыкание). 
			# Она имеет доступ ко всем переменным, объявленным выше, и в цикле ниже.
			def __inner():
				if val_type is None:
					self.notifications.add_error_with_stack_nodes(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")
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
					self.notifications.add_error_with_stack_nodes(f"Unknown type of value #{i+1}:\n{json.dumps(one_value, indent=4)}")

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
		
		Card_inner_notifications = Card_object.get_notifications()
		Card_notifications = Card_inner_notifications.get_all_notifications()

		for one_error in Card_notifications.get("errors", []):
			if "Error_text" not in one_error:
				self.notifications.add_error_with_stack_nodes(f"Missing 'Error_text' in Card notifications['Errors']:\n{Card_notifications.get('Errors', [])}")
			else:
				self.notifications.add_error_with_stack_nodes(one_error["Error_text"])
		
		for one_warning in Card_notifications.get("warnings", []):
			if "Warning_text" not in one_warning:
				self.notifications.add_warning_with_stack_nodes(f"Missing 'Warning_text' in Card notifications['Warnings']:\n{Card_notifications.get('Warnings', [])}")
			else:
				self.notifications.add_warning_with_stack_nodes(one_warning["Warning_text"])
		
		for one_note in Card_notifications.get("notes", []):
			if "Note_text" not in one_note:
				self.notifications.add_note_with_stack_nodes(f"Missing 'Note_text' in Card notifications['Notes']:\n{Card_notifications.get('Notes', [])}")
			else:
				self.notifications.add_note_with_stack_nodes(one_note["Note_text"])
		
		for one_messages in Card_notifications.get("messages", []):
			if "Message_text" not in one_messages:
				self.notifications.add_message_with_stack_nodes(f"Missing 'Message_text' in Card notifications['Messages']:\n{Card_notifications.get('Messages', [])}")
			else:
				self.notifications.add_message_with_stack_nodes(one_messages["Message_text"])
		
		
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

	def get_notifications_as_list(self):
		return self.notifications.get_all_notifications()

	def get_notifications_as_str(self):
		res_text = ''
		for i, one_notification in enumerate(self.notifications.get_all_notifications()):
			res_text += f"#{i+1}: {one_notification}\n"
		return res_text