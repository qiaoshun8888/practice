#coding=utf-8


class Matrix(object):
	_data_ = []
	width = 0
	height = 0

	def __init__(self, nested_array):
		self.width = len(nested_array[0])
		for i in nested_array:
			if len(i) == self.width:
				self.height += 1
				self._data_.extend(i)
			else:
				raise "Cannot init"

	
	def printout(self):
		if self._data_ and self.width and self.height:
			for i in range(self.height):
				for j in range(self.width):
					print self._data_[i*self.height+j],
				print ""
	
	def transpose(self):
		"""
		0 <- (self.height-1) * self.width
		(self.height-1) * self.width <- (self.height-1)*self.width
		0,0 <ddd- (self.height-1) * self.widtho


		0(0r 0c) <- (3r 1c) 8
		8(2r 1c) <- (1r 3c) 2
		2(0r 2c) <- (1r 1c) 0
		
		1(0r 1c) <- (2r 1c) 4
		4(1r 1c) <- (2r 2c) 5
		5(1r 2c) <- (1r 2c) 1

		3(2r 1c) <- (3r 2c) 9
		9(4r 1c) <- (3e 4c) 11
		11(4r 3c) <-(1r 4c) 3

		6(3r 1c) <- (3r 3c) 10
		10(4r 2c)<- (2r 4c) 7
		7(3r 2c) <- (2r 3c) 6
				

		0,1 <- (self.height-1) * self.width + 1
		0,self.width <- self.height * self.width
		
		self.
		"""


if __name__ == '__main__':
	m = Matrix([[1,3,4],[2,1,3],[4,5,6]])
	m.printout()
