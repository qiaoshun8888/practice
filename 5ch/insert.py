'''
Write a method to insert M into N
such that M starts at bit j and ends at bit i
'''


def insert(n, m, i, j):
	# print bin(n)
	# print (0b1 << j | ~(0b1 << i))
	n = n | (0b1 << j | ~(0b1 << i))
	# print bin(n)
	m = m << i
	# print bin(m)
	return n & m

if __name__ == '__main__':
    r = insert(0b10000000000, 0b10011, 2, 6)
    print bin(r)

