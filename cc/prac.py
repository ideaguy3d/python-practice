from collections import defaultdict

"""
~ comprehension form ~
[expr for x in list if condition]
{expr for x in set if condition]
"""

words = ['apple', 'bat', 'bar', 'atom', 'book']
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

def dictionary_from_sequence():
	v_list = ['foo', 'bar', 'baz']
	k_list = ['alpha', 'beta', 'gamma']
	kv_map = {}
	# can create dictionaries 2 ways
	# 1st
	for k, v in zip(k_list, v_list):
		kv_map[k] = v
	# 2nd
	kv_map2 = dict(zip(k_list, v_list))
	foo_map = dict(zip(range(5), reversed(range(5))))
	pass


def default_values():
	v_list = ['foo', 'bar', 'baz']
	k_list = ['alpha', 'beta', 'gamma']
	default_value = 'N/A'
	d1 = dict(zip(k_list, v_list))
	key = 'cep'
	by_letter = {}
	by_letter2 = {}
	by_letter3 = defaultdict(list)
	# set a default value
	def get_default():
		# 1st
		if key in d1:
			value = d1[key]
		else:
			value = default_value
		# 2nd
		value = d1.get(key, default_value)
		pass
	
	def setdefault_default():
		# 1st, manual
		for word in words:
			letter = word[0]
			if letter not in words:
				by_letter[letter] = [word]
			else:
				by_letter[letter].append(word)
		# 2nd, uses .setdefault()
		for word in words:
			by_letter2.setdefault(word[0], []).append(word)
		# 3rd, uses defaultdict
		for word in words:
			by_letter3[word[0]].append(word)
		pass
	
	pass # end of "def default_values():"


def comprehension_practice_1():
	# list
	lc = [x.upper() for x in strings if len(x) > 2]
	# dictionary
	# dc = {k: v for k, v in strings if len(v) > 2}
	# set
	sc = {len(x) for x in strings if len(x) > 2}
	pass


def comprehension_practice_2():
	pass


def comprehension_practice_3():
	pass


def comprehension_practice_4():
	pass


dictionary_from_sequence()
comprehension_practice_1()


# end of file
