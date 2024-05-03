
#sample="""1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet"""
#
#
#splines=sample.splitlines()


with open('input' ,'r') as inputF:
    inputlines=inputF.read().splitlines()


counter=0

for line in inputlines:
    left  = -1
    right = -1

    for i in line:
        if left > int(-1):
            break
        elif i.isnumeric():
            left = int(i)


    for i in line[slice(None, None, -1)]:
        if right > int(-1):
            break
        elif i.isnumeric():
            right = int(i)

    counter=counter+int(str(left)+str(right))

print(counter)




