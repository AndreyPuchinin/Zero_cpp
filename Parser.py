from Logger import Logger

class Parser():
	def __init__(self, _logger: Logger):
		self.__logger = _logger
		self.inp_str = self.__logger.inp_str
		self.cards = self.__logger.cards

		print("получены карточки", self.__logger.cards)
		print(self.__logger.inp_str)

	def forward_usual_swaps(self):
		# Принимает входную строку
		self.inp_str = self.inp_str.replace(self.cards[0]['usual_vals'][0]["val"], self.cards[0]['name'])
		return self.inp_str

	def temple_swaps(self):
		# Принимает входную строку
		pass
	
	def backward_swaps(self):
		# Принимает входную строку
		# Срабатывает, если не было коллизий
		pass
	
	def id_swaps():
        # Принимает входную строку
		# Вызывается, в случае, когда были коллизии
		pass

