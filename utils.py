# Modules for maxNumber.py
def find_max(arr):
	max_number = 0
	for number in arr:
		if number > max_number:
			max_number = number
	return max_number	
