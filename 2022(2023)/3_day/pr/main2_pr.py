import os, sys
from funcs_pr import common_val_from_three_strings


inp_folder		= os.path.dirname(__file__)
inp_full_path	= os.path.join(inp_folder, 'input')


try:
	with open(inp_full_path, 'r') as inp_fi:
			file_input		= inp_fi.read().split('\n')
except FileNotFoundError:
	print(f"file '{inp_full_path}' not found")
except PermissionError:
	print(f"permission on '{inp_full_path}' denied")
											#added exceptions for file errors
val	=	0
for i in range(0, len(file_input), 3):
	if file_input[i] and file_input[i+1] and file_input[i+2]:
		str_1,str_2,str_3		=	file_input[i],file_input[i+1],file_input[i+2]
		val	+=	common_val_from_three_strings(str_1,str_2,str_3)
											#changed the previous way, with if, counters and appends to temporal lists
											#to one that, first checks the total amount of tuples, jumping from 3 to 3,
											#and iterating the numbers between each three ([i],[i+1],[i+2])
print(val)
