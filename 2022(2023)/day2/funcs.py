#def whowin(en,mc):
#	if en == "A" and mc == "X":
#		return "draw"
#	if en == "A" and mc == "Y":
#		return "win" 
#	if en == "A" and mc == "Z":
#		return "lose"
#	if en == "B" and mc == "Y":
#		return "draw"
#	if en == "B" and mc == "X":
#		return "lose"
#	if en == "B" and mc == "Z":
#		return "win"
#	if en == "C" and mc == "X":
#		return "win"
#	if en == "C" and mc == "Y":
#		return "lose"
#	if en == "C" and mc == "Z":
#		return "draw"

 #		comentado, es mejor usar un lookup de diccionario para esto


def whowin(en,mc):
	resultado = {
		('A','X'):'draw',
		('A','Y'):'win',
		('A','Z'):'lose',
		('B','Y'):'draw',
		('B','X'):'lose',
		('B','Z'):'win',
		('C','X'):'win',
		('C','Y'):'lose',
		('C','Z'):'draw'
	}
	return resultado[(en,mc)]

"""x=lose, y=draw, z=win
"""

def whatchoos(en,res):
	choos = {
		('A','X'):'R',
	}



