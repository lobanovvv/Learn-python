class Mammol():
	def walk(self):
		print("I am walking")
	
class Dog(Mammol):
	def bark(self):
		print("BARK, BARK")

class Cat(Mammol):
	pass


cat1 = Cat()
cat1.walk()

dog1 = Dog()
dog1.bark()
