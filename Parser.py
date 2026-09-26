from Logger import Logger

class Parser():
	# на вход библиотека в следующем виде:
	# "cards": [
    #     {
    #         "status": "successful",
    #         "name": "Пиво",
    #         "usual_vals": [
    #             {
    #                 "val": "Деньги"
    #             }
    #         ],
    #         "selflink_vals": [],}]
	
	def __init__(self, _logger: Logger):
		self.__logger = _logger
		self.inp_str = self.__logger.inp_str
		self.cards = self.__logger.cards

		# print("получены карточки", self.__logger.cards)
		# print("Введенная строка:")
		# print(self.__logger.inp_str)
	
	def __replase_all_1_pass(string, valtype):
		pos = 0
		was_swaps = False
		#for
		return was_swaps
	
	def forward_usual_swaps(self):
		# Принимает входную строку
		
		# цикл итерации по типам значений
		#	цикл проходов пока были замены
		#
		#		(цикл до конца
		#			строка, смещение = найти что заменять
		#			заменяем на месте
		#			возврат длина замены
		#			позиция += смещение)
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

