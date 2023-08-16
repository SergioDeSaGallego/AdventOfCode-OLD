
alfabeto							= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priori								= {char: index+1 for index, char in enumerate(alfabeto)}
									#changed the anterior way in which we used the variable counter over a loop
									#to assign each value to each letter, with 'enumerate' is more easy!
def comparat (str_1, str_2):
	resultado = set(str_1) & set(str_2)
	return resultado.pop()


def common_val_from_three_strings (str_1:str, str_2:str, str_3:str):
	resultado = set(str_1) & set(str_2) & set(str_3)
	try:
		return priori[(resultado.pop())]
									#now we call the dictionary priori while the same function to save time
									#the function now retrieves the value
	except KeyError:
		print('no common character between the')
		return None
									#added exception handlings
