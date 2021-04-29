class Shape:
	def __init__(self):
		pass
	def area(self):
		return 0

class Square(Shape):
	def __init__(self,l):
		self.l  = l
	def area(self):
		return (self.l**2)

aSquare = Square(3)
print(aSquare.area())
aShape = Shape()
print(aShape.area())