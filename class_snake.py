class Snake:
	"""This class allows you to create objects of type snake."""
	def __init__(self,name):
		self.name=name
	def change_name(self,new_name):
		self.name=new_name

snake1=Snake("Python")
snake2=Snake("Black Mamba")

print(snake1.name)
print(snake2.name)

snake1.change_name("Anaconda")
print(snake1.name)

print(Snake.__doc__)