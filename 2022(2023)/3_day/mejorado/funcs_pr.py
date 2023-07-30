




#valores							= {}
#letras								= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#counter							= 0
#for x in letras:
#	counter 						+= 1
#	valores.update({x:counter})




#def comparat(str_1, str_2):
#	eq=''
#	for x in str_1:
#		if x in str_2:
#			eq += x
#	return eq[-1]



alfabeto							= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
prioridad							= {char: index+1 for index, char in enumerate(alfabeto)}
									#se cambió la forma anterior en la que se usaba una variable counter
									#sobre un bucle for para asignar el numero de prioridad a cada
									#letra, sin embargo, dado que la funcion de python 'enumerate' ya
									#añade un valor basado en la posicion en la lista, se usa un bucle iterando
									#sobre esta misma funcion

									#se deja comentada la anterior forma de hacerlo

def comparat (str_1, str_2):
	resultado = set(str_1) & set(str_2)
	return resultado
