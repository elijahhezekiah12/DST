def quicksort(list):
	if len(list) > 1:
		l, e, g = partition(list)	
		return quicksort(l) + e + quicksort(g)	
	else:
		return list

def partition(list):
		pivot = list[len(list) - 1]
		l = []
		e = []
		g = []
		
		for i in range(len(list)):
			if list[i] > pivot:
				g.append(list[i])
			elif list[i] < pivot:
				l.append(list[i])
			else:
				e.append(list[i])
				
		return l, e, g
		
if __name__ == "__main__":
	list = [1,5,7,8,3,6,8,0,9]
	print quicksort(list)
