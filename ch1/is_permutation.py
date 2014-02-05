#coding=utf-8

def is_permutation(str1, str2):
	tmp_dict = {}
	for i in str1:
		if i in tmp_dict:
			tmp_dict[i] += 1
		else:
			tmp_dict[i] = 1

	for i in str2:
		if i in tmp_dict:
			tmp_dict[i] -= 1
		else:
			return False

	for v in tmp_dict.values():
		if not v == 0:
			return False

	return True

if __name__ == '__main__':
	print is_permutation("test", "stet")
	print is_permutation("test", "ttet")


