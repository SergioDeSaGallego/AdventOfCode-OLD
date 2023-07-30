




valores							= {}
letras								= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter							= 0
for x in letras:
	counter 						+= 1
	valores.update({x:counter})




def comparat(str_1, str_2):
	eq=''
	for x in str_1:
		if x in str_2:
			eq += x
	return eq[-1]
