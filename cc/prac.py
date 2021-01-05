from collections import defaultdict
import re
import itertools

"""
~ comprehension form ~
[expr for x in list if condition]
{key_expr: val_expr for key, value in enumerate(list) if condition}
{expr for x in set if condition]
"""

words = ['apple', 'bat', 'bar', 'atom', 'book']
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
outer_list = []
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south carolina##', 'West virginia?']


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
	
	# set a default values for dictionaries
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
			if letter not in by_letter:
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
	
	get_default()
	setdefault_default()
	pass


def comprehension_practice_1():
	# list
	lc = [x.upper() for x in strings if len(x) > 2]
	# dictionary
	dc = {k: v for k, v in enumerate(strings) if len(v) > 2}
	# set
	sc = {len(x) for x in strings if len(x) > 2}
	# nested comprehension
	# 1st
	names_of_interest = []
	for names in all_data:
		e_names = [name for name in names if name.count('e') >= 2]
		names_of_interest.extend(e_names)
	# 2nd
	e_names = [name for names in all_data for name in names if name.count('e') >= 2]
	# flattening a list of tuples
	# 1st
	flatten1 = []
	for tup in some_tuples:
		for x in tup:
			flatten1.append(x)
	# 2nd
	flatten2 = [x for tup in some_tuples for x in tup]
	# create a list of lists
	lol = [[x for x in tup] for tup in some_tuples]
	pass


def comprehension_practice_2():
	a = 5
	b = 10
	c = 20
	result = []
	for i in range(5):
		outer_list.append(i)
	for value in strings:
		value = value.strip()
		value = re.sub('[!#?]', '', value)
		value = value.title()
		result.append(value)
	return a, b, c, result


def remove_punctuation(value):
	return re.sub('[!#?]', '', value)


remove_ops = [str.strip, remove_punctuation, str.title]


def clean_states():
	result = []
	for state in states:
		for op in remove_ops:
			state = op(state)
		result.append(state)
	for x in map(remove_punctuation, states):
		print(x)
	return result


def lambda_sort():
	strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
	strings2 = strings[:]
	# sort by strings with the most unique letters
	strings.sort(key=lambda x: len(set(list(x))))
	strings2.sort(key=lambda x: len(set(x)))
	pass


def comprehension_practice_3():
	pass


def comprehension_practice_4():
	pass


def itertools_module_practice():
	first_letter = lambda x: x[0]
	names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
	for letter, names in itertools.groupby(names, first_letter):
		print(letter, list(names))
	pass

# dictionary_from_sequence()
# default_values()
# comprehension_practice_2()
# clean_states()
# lambda_sort()
itertools_module_practice()

debug = 1


# end of file
