class Person:

	def __init__(self, name):
		self.name = name

	def talk(self):
		print("Talk")

sandy = Person("Sandy")

print(sandy.name)
sandy.talk()

sandy.name = "Sandy Tayler"
print(sandy.name)

