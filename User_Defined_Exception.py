class my_exception(Exception):
	def __init__(self,message):
		self.m = message
	def __str__(self):
		return self.m

try:
	a = 100
	b = 65
	if a<b :
		raise my_exception("a can't be less than b")
except my_exception as x:
	print(x)

finally:
	print("Done")