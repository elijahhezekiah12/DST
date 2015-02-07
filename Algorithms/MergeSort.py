import math

	
def mergesort(list):
	if len(list) > 1:
		partition = len(list) // 2
		
		first_half = list[:partition]
		second_half = list[partition:]
		a = mergesort(first_half)
		b = mergesort(second_half)
		
		return merge(a, b)
	else:
		return list
		
def merge(a, b):
	list = []
	i = 0
	j = 0
	
	while i < len(a) and j < len(b):
			if a[i] <= b[j]:
				list.append(a[i])
				i += 1
			else:
				list.append(b[j])
				j += 1
	print list
	list += a[i:]
	list += b[j:]
	return list

if __name__ == "__main__":
	list = []
	list.append(1)
	list.append(6)
	list.append(3)
	list.append(5)
	list.append(3)
	list.append(4)

	print(mergesort(list))

