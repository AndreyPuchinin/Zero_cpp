from notification_classes import error
err1 = error.error()
err1.create_notification('error bad')
err1.create_notification('error good')
err1.get_all_notifications()

print("Zero first version!")

class CardManager():
	def __init__(self):
		self.library = [] # хранит объекты класс Card
	
	def value_validate(self):
		# Если тип и selflink  и template то кладет в selflink-template
		pass

	def create_card(self):
		# Должен использовать value_validate
		# создавать объект карточки
		# определять все типы значений
		# и передавать их в объект карточки
		# и класть карточку в нужную библиотеку
		pass

	def is_self_link_value(self):
		pass

	def is_template_value(self):
		pass

	def is_id_value(self):
		pass

	def is_usual_value(self):
		# использует is_self_link_value
		# is_template_value
		# is_id_value
		pass

	def parse(self):
		parser_object = Parser()
		parser_object.forward_usual_swaps()


class Parser():
	def forward_usual_swaps(self):
		# Принимает входную строку
		pass

	def temple_swaps(self):
		# Принимает входную строку
		pass
	
	def backward_swaps(self):
		# Принимает входную строку
		pass
	
	# def id_swaps() ???
	

class Logger():
	pass
	# создает объект CardManager и Parser


class Zero():
	def run_warp_drive(self):
		pass