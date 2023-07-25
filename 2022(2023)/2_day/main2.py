#
#Your puzzle answer was 8890.
#
#The first half of this puzzle is complete! It provides one gold star: *
#--- Part Two ---
#
#The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#
#The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:
#
#    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
#    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
#
#Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
#
#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


from funcs import whatchoos
import sys
import os



#test="""A Y
#B X
#C Z"""

with open(os.path.join(sys.path[0], 'input'), 'r' ) as inputF:
	guide=inputF.read()

guide = guide.split('\n')

print(guide)

punts=0

points_chos = {('r'):1,('p'):2,('t'):3}
points_resh = {('X'):0,('Y'):3,('Z'):6}

for x in guide:
	if x != '':
		chos=whatchoos(x[0], x[2])
		punts += points_chos[(chos)]
		punts += points_resh.get(x[2],0)
		#no diferencia entre usar "points_chos[(chos)] y usar points_chos.get(chos,0)
		# la unica diferencia podría ser, la posibilidad de elegir un valor por defecto (el "0" al final en la funcion "get")
		# esto del 0 puede ser util cuando queramos llamar a un diccionario usando valores en una lista que PODRIA tener valores vacíos, como puede ser nuestra lista de "input"
		# el caso es (como demuestro aqui al hacer las llamadas a los dos ciccionarios de diferente manera) que ambas hacen la llamada al diccionario con exito, por lo que dependera
		# de cual se necesite, dada la ocasion
print(punts)
