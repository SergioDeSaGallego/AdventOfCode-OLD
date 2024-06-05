numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

#hacemos un set para encontrar y mapear cada numero con su valor
#(recordar que, set es mejor para estos casos, es una "lista desordenada" pero hace las búsquedas más rapidas que en una lista ordenada normal)



def first_numlet (lin):
    position = 99999
    num=0
    for number in numbers:
        if number in lin:
            if lin.index(number)<position:
                position=lin.index(number)
                num=numbers[number]

    return [position, num]

def last_numlet (lin):
    position = -1
    num=0
    for number in numbers:
        if number in lin:
            if lin.rindex(number)>position:
                position=lin.rindex(number)
                num=numbers[number]
    return [position, num]


eso="4sixfour4nppgsr36one3"

