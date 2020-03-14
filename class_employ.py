class Employ:
	def __init__(self,name):
		self.name = name
	def details(self,id,designation,email):
		self.id = id
		self.designation = designation
		self.email = email


record1 = Employ('Praveen')
record1.details(4567,'Admin','praveen@msnz.com')

record2 = Employ('Naveen')
record2.details(1234,'Developer','naveen@msnz.com')

print("Name of the employ: ",record1.name)
print("ID of the employ: ",record1.id)
print("Designation: ",record1.designation)
print("Email: ",record1.email)
#----------------------------------------
#Modify a property of an object/instance.
record1.id = 9876
print(record1.id)
#----------------------------------------
#Delete a property of an object/instance.
del record1.id
print(record1.id)
#----------------------------------------
#Delete an object/instance.
del record1