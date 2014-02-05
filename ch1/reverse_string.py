#coding=utf-8

def reverse(str):
	# for reverse in place
	str_list = list(str)
	n = len(str_list)
	for i in range(n/2):
		str_list[i], str_list[n-1-i] = str_list[n-1-i], str_list[i]
	return "".join(str_list)


if __name__ == '__main__':
	rever = reverse("test reverse function")
	print reverse(rever)
