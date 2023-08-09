from funcs_pr import priori, comparat
import os, sys

script_dirname								= os.path.dirname(__file__)
input_full_path								= os.path.join(script_dirname, 'input')



with open(input_full_path, 'r') as file_input:
	list_from_input							= file_input.readlines()
										#readlines is better for this! itearate over each line


total									= 0

for line in list_from_input:
	if line:
		mit 							= len(line) // 2
		split_1, split_2						= line[mit:], line[:mit]

		same_L							= comparat(split_1, split_2)
	#	print(same_L)
		t_value							= priori[same_L]


	total								+= t_value

print(total)
