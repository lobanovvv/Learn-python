class Person:

	def __init__(self, name):
		self.name = name

	def talk(self):
		print("Talk") 

	def hello(self):
		print(f"Hello {self.name}!")


anton = Person("Anton")

anton.hello()
