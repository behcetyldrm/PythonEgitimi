class Fruits():

	def __init__(self, name, calories):

		self.name = name
		self.calories = calories

	def __str__(self):  #özel method

	#__str__ methodu ile bu sınıfın içine attığımız instance'mızı ekrana yazdırabildik.

		return f"{self.name} has {self.calories} calories"

	def __len__(self): #özel method

		return self.calories


my_fruit = Fruits("banana", 200)
print(my_fruit)

print(len(my_fruit))