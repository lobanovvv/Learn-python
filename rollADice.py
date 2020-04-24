import random


class Dice:
	def roll(self):
		var1 = random.randint(1,6)
		var2 = random.randint(1,6)
		res = ( var1, var2 )
		return res


chance1 = Dice()
print(chance1.roll())

