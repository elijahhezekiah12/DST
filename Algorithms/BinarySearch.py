import math

def binsrc(list, x, p, r):
	if p == r:
		if x == list[p]:
			return "Found! Index is", p
		else:
			return "Failed!"
	else:
		mid = (p + r) // 2
		if x <= list[mid]:
			return binsrc(list, x, p, mid)
		else:
			return binsrc(list, x, mid + 1, r)

if __name__ == "__main__":
	list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	print binsrc(list, 9, 0, len(list) - 1)
