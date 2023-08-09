#--- Day 2: Rock Paper Scissors ---
#The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.
#
#Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.
#
#Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
#
#The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
#
#The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#
#Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.
#
#For example, suppose you were given the following strategy guide:
#
#A Y
#B X
#C Z
#This strategy guide predicts and recommends the following:
#
#In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
#In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
#
#What would your total score be if everything goes exactly according to your strategy guide?
#

from funcs import whowin
import os
import sys

with open(os.path.join(sys.path[0], 'input'), 'r') as inputF:
	strategy_guide=inputF.read().split("\n")



test="""A Y
B X
C Z"""

#rock(A/X)     = 1
#paper(B/Y)    = 2
#Scissors(C/z) = 3

#lost          = 0
#draw          = 3
#win           = 6



z							= {'X':1, 'Y':2, 'Z':3}i
#se convirtio esto en un diccionario, conteniendo las tres posibilidades (X,Y,Z) para evadir los 3 if's de la primera versioni

punts							= 0
for x in (strategy_guide):


	if x 						== '':	break 	

	##
	#	break puesto para la ultima iteracion, input nos da una cadena vacia al final debido al split().
	##

	ronda						= {"enemy":x[0], "mc":x[2]}
	resultadovronda					= whowin(ronda['enemy'], ronda['mc'])

	##
	#	eliminados puntos_temporal y ronda_tempo, no hacen falta ya, se hace a lo largo del bucle simplemente llamando a x[0] y x[2] enlugar de hacer un split basado en el espacio intermedio :D
	##

	if resultadovronda				== "draw":
		punts					+= 3
	if resultadovronda				== "win":
		punts					+= 6


	punts += z.get(ronda['mc'],0)

	print(punts)



