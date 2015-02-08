import math

def selectionsort(list):
	for x in range(0, len(list)):	
		index = x
		lowest = list[x]
		for i in range(x, len(list)):
			if list[i] < lowest:
				index = i
				lowest = list[i]
		# can be improved by checking if list[x] is index, so no change needed
		temp = list[x]
		list[x] = list[index]
		list[index] = temp
	
	return list
		
	return "hi"
if __name__ == "__main__":
	list = [55,51,74,86,36,67,88,0,49]
	print selectionsort(list)
