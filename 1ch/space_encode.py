#coding=utf-8

def space_encode(str, true_length):
	spaces = []
	for i in range(true_length):
		if str[i] == ' ':
			spaces.append(i)
	# is there any python pointer can use ?
