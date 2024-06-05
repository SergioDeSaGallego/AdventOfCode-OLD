from funcs import first_numlet,last_numlet

#sample="""two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteeni"""

#splines=sample.splitlines()


with open('input', 'r') as inputFile:
    splites=inputFile.read().splitlines()

sum=0
for lin in splites:
    le_numlet=first_numlet(lin)
    ri_numlet=last_numlet(lin)

    leftnum=le_numlet[1]
    rightnum=ri_numlet[1]

    leftplace=le_numlet[0]
    rightplace=ri_numlet[0]


    for chara in lin:
        if chara.isdecimal() and lin.rindex(chara)>rightplace:
            rightplace=lin.rindex(chara)
            rightnum=chara
#aqui necesitamos usar rindex para sacar el numero mas a la derecha, evitando casos duplicados.
        if chara.isdecimal() and lin.index(chara)<leftplace:
            leftplace=lin.index(chara)
            leftnum=chara

    print(lin, "\nleft", leftnum, "\nright", rightnum)

    result=(str(leftnum)+str(rightnum))
    print(result)

    sum=sum+int(result)

print(sum)
