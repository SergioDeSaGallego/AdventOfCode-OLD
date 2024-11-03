
# Adding the result to its own class
# Game_number[[red[round1,round2,round3],blue[round1,round2,round3],green[round1,round2,round3]]

class GameIterations:
    def __init__(self,stage,red,blue,green):
        self.stage=stage
        self.red=red
        self.blue=blue
        self.green=green


# Parsing lines of each game to by color, round and game

def LineIngest(L_Stage,line):
    Fix_Line=line.split(';')
    L_Red=[]
    L_Blue=[]
    L_Green=[]
    for round in Fix_Line:
        Fix_round = round.strip().split(',')
        for i in Fix_round:
            # print(i)
            if 'red' in i:
                L_Red.append(i.strip().split(' ')[0])
            elif 'blue' in i:
                L_Blue.append(i.strip().split(' ')[0])
            elif 'green' in i:
                L_Green.append(i.strip().split(' ')[0])


    return GameIterations(L_Stage,L_Red,L_Blue,L_Green)



