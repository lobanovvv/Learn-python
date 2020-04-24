import random

for i in range(3):
	print(random.random())

for i in range(3):
	print(random.randint(10,20))

#Random from list
members = [ "Anton", "Vasya", "Kolya" ]
leader = random.choice(members)
print(leader)
