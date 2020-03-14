class RobotMaker:
	"""Represents a robot, with a name."""
	############## Class Variable ##############
	population = 0   #This class variable is counting the number of robots.
	############## Class Method ################
	@classmethod
	def how_many(cls):
		"""Prints the current population."""
		print("The RobotMaker says: We have", cls.population, "robots.")
	def __init__(self, name):
		"""Initializes the data."""
		self.name = name
		# 'self.name' is a object variable.
		print("Initializing ",self.name)
		# When created, the robot adds to the population
		RobotMaker.population += 1
	def die(self):
		"""I am dying."""
		print(self.name,"is being dismantled!")
		RobotMaker.population -= 1
		if RobotMaker.population == 0:
			print(self.name, "was the last one.")
		else:
			print("The RobotMaker says: There are still", RobotMaker.population, "robots working.")
	def say_hi(self):
		"""Greeting by the robot."""
		print("Greetings, my masters call me ",self.name)



droid1 = RobotMaker("Sonny")
droid1.say_hi()
RobotMaker.how_many()

droid2 = RobotMaker("Wall-E")
droid2.say_hi()
RobotMaker.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's dismantle them.")
droid1.die()
droid2.die()
RobotMaker.how_many()
