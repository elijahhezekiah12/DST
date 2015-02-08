def insertionsort(list):
	for i in range(1, len(list)):
		j = i
		while j > 0 and list[j-1] > list[j]:
			temp = list[j]
			list[j] = list[j-1]
			list[j-1] = temp
			j -= 1

	return list

if __name__ == "__main__":
	list = [55,51,74,86,36,67,88,0,49]
	print insertionsort(list)
