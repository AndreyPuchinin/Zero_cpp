from Logger import Logger
class TrieNode:
    """Узел префиксного дерева."""
    def __init__(self):
        self.children = {}
        self.name = None
        self.is_end = False

class Trie:
    """Префиксное дерево (Trie) для строк с любыми юникод-символами."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key: str, value: str) -> None:
        """
        Вставляет пару (ключ, значение) в дерево.
        Если ключ уже существует — значение перезаписывается.
        """
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Дошли до конца ключа — сохраняем значение
        node.name = value
        node.is_end = True
    
    def search_prefix(self, prefix: str) -> list:
        """
        !!!Когда e, elf добавлено, а el нет!!!
        входная строка elf будет без замен. А должно быть замена по имени для значения 'e'.
        Возвращает имя 
        самого длинного найденного значения и его длину
        поиск name=Вася [а] в ббббб: 
                        prefix[0], 1
        поиск [а] в ббааа: 
                        prefix[0], 1
        поиск name=Дима [аб] в абббб: 
                        аб, 2
        поиск [бббббаф] в ббббб:
                        prefix[0], 1
        поиск [бб] в бб:
                        
        поиск name=И [а] в абббб:
                        И, 1
        """
        last_correct_name = prefix[0]
        last_correct_step = 1
        node = self.root
        for i, char in enumerate(prefix):
            if char not in node.children:
                if node.name == None:
                    return last_correct_name, last_correct_step
                return node.name, i  # имя и сколько символов нужно заменить на это имя
            if node.name is not None:
                last_correct_name = node.name
                last_correct_step = i+1
            node = node.children[char]

        if node.name == None:
            return last_correct_name, last_correct_step
        return node.name, i+1
    
    def _collect_all(self, node: TrieNode, current_key: str, results: list) -> None:
        """Рекурсивно собирает все пары (ключ, значение) из поддерева."""
        if node.is_end:
            results.append((current_key, node.name))
        
        for char, child_node in node.children.items():
            self._collect_all(child_node, current_key + char, results)

def test_example(data_list: list) -> Trie:
    trie = Trie()
    for key, value in data_list:
        trie.insert(key, value)
    return trie

Trie_usual_vals = test_example([["Деньги","Пиво"],["Пиво","Деньги"]]) #["Рубли","Киндеров"]])
# Trie_selflink_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])
# Trie_templ_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])
# Trie_selflink_templ_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])
# Trie_id_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])
# Trie_id_selflink_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])
# Trie_id_templ_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])
# Trie_id_selflink_templ_vals = test_example([["Деньги","Пиво"],["Рубли","Киндеры"]])

result=[]
Trie_usual_vals._collect_all(Trie_usual_vals.root,'',result)

hardcode_self_cards={"usual_vals": Trie_usual_vals}#,
		# "selflink_vals": Trie_selflink_vals,
		# "templ_vals": Trie_templ_vals,
		# "selflink_templ_vals": Trie_selflink_templ_vals,
		# "id_vals": Trie_id_vals,
		# "id_selflink_vals": Trie_id_selflink_vals,
		# "id_templ_vals": Trie_id_templ_vals,
		#"id_selflink_templ_vals": Trie_id_selflink_templ_vals}

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
		self.swaps = []
	# def search_for_replace(valtype: str, string):
	# 	for i in range(len(string)):
			
	def __replase_all_1_pass(self, text, valtype):
		pos = 0
		step = 0
		were_swaps = False
		while pos<len(text):
			name, step = hardcode_self_cards[valtype].search_prefix(text[pos::])
			if pos+step >len(text):
				return False, text
			if name != text[pos:pos+step]:
				self.swaps += [{'position': pos, 'replaced': text[pos:pos+step], 'replacing': name}]
				were_swaps = True
			text = text.replace(text[pos:pos+step], name)
			
			pos += len(name)
		return were_swaps, text

	def forward_swaps(self, STOPCOUNT):
        # Работает со входной строкой

        # Типы значений = всё кроме ID-шников
        # Работает со входной строкой

        # Типы значений = всё кроме ID-шников
		val_types = [
           'usual_vals']
        # [
        #     'usual_vals',
        #     'selflink_vals',
        #     'templ_vals',
        #     'selflink_templ_vals',
        #     'id_vals',
        #     'id_selflink_vals',
        #     'id_templ_vals',
        #     'id_selflink_templ_vals',
        # ]

		for val_type in val_types:
			i = 0
			were_changes = True
			while (STOPCOUNT>=0 and i<STOPCOUNT or STOPCOUNT<0) and were_changes:
				were_changes, self.inp_str = self.__replase_all_1_pass(self.inp_str, val_type)
				i += 1

		# self.inp_str = self.inp_str.replace(
        #     self.cards[0]['usual_vals'][0]["val"],
        #     self.cards[0]['name'],
        # )

		return {'final_str':self.inp_str, 'swaps': self.swaps}

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

