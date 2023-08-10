
alfabeto							= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priori								= {char: index+1 for index, char in enumerate(alfabeto)}
									#se cambió la forma anterior en la que se usaba una variable counter
									#sobre un bucle for para asignar el numero de prioridad a cada
									#letra, sin embargo, dado que la funcion de python 'enumerate' ya
									#añade un valor basado en la posicion en la lista, se usa un bucle iterando
									#sobre esta misma funcion

									#se deja comentada la anterior forma de hacerlo

def comparat (str_1, str_2):
	resultado = set(str_1) & set(str_2)
	return resultado.pop()

