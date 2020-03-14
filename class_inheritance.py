class Person:
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age
	def Name(self):
		return self.firstname + " " + self.lastname

class Employee(Person):
	def __init__(self, first, last, age, staffnum):
		Person.__init__(self, first, last, age)
		self.staffnumber = staffnum
	def GetEmployee(self):
		return self.Name() + ", " + self.age + ", " + self.staffnumber

x = Person("Praveen", "G", "40")
y = Employee("Naveen", "B", "30", "1007")

print(x.Name())
print(y.GetEmployee())