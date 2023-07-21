
#--- Part Two ---
#By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
#
#To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
#
#In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.
#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
#
#EXAMPLE
#
#testCal="""1000
#2000
#3000
#
#4000
#
#5000
#6000
#
#7000
#8000
#9000
#
#10000"""
#



with open('input','r') as inpuF:
	calories=inpuF.read().split('\n')
actualCal = 0
numbers=[]

for x in calories:
	if x != calories[-1] and x != "":
		actualCal = int(actualCal) + int(x)
	elif x == '':
		numbers.append(actualCal)
		actualCal = 0
	else:
		actualCal = int(actualCal) + int(x)
		numbers.append(actualCal)
Cal1=0
Cal2=0
Cal3=0

print(numbers)

for x in numbers:

	if x > Cal3  and x < Cal2:
		Cal3=int(x)

	elif x > Cal2 and x < Cal1:
		Cal3=Cal2
		Cal2=int(x)

	elif x > Cal1:
		Cal2=Cal1	
		Cal1=int(x)
	
print(Cal1,Cal2,Cal3)
print(sum((Cal1,Cal2),Cal3))
