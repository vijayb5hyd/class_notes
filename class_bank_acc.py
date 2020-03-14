class BankAccount:
	def __init__(self, firstn, lastn):
		self.firstn=firstn
		self.lastn=lastn
	def account_details(self, acc_no, acc_type, ifsc_code, mobile, email):
		self.acc_no = acc_no
		self.acc_type = acc_type
		self.ifsc_code = ifsc_code
		self.mobile = mobile
		self.email = email
	def full_name(self):
		print("FullName :", self.firstn, self.lastn)


customer1=BankAccount('Naveen','B')
customer1.account_details('987654321','sb account','ifsc0008','9848121212','naveen@msnz.com')
customer1.full_name()

customer1_details=[customer1.acc_no,customer1.acc_type,customer1.ifsc_code,customer1.mobile,customer1.email]
customer1_details

print(customer1.acc_no)
print(customer1.acc_type)
print(customer1.ifsc_code)
print(customer1.mobile)
print(customer1.email)

customer2=BankAccount('Praveen','G')
customer2.account_details('987654361','sb account','ifsc0008','9848121223','praveen@msnz.com')
customer2.full_name()

customer2_details=[customer2.acc_no,customer2.acc_type,customer2.ifsc_code,customer2.mobile,customer2.email]
customer2_details

print(customer2.acc_no)
print(customer2.acc_type)
print(customer2.ifsc_code)
print(customer2.mobile)
print(customer2.email)