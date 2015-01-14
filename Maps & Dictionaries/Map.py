class KeyValue():
	def __init__(self, k, v):
		self.key = k
		self.value = v
		
	def getKey(self):
		return self.key
			
	def getValue(self):
		return self.value
		
	def setKey(self, k):
		self.key = k
		
	def setValue(self, v):
		self.value = v
		
class Map():
	def __init__(self):
		self.list = list()
		
	def size(self):
		return len(self.list)
		
	def isEmpty(self):
		return len(self.list) == 0
		
	def get(self, k):
		index = self.find_position(k)
		if index == None:
			return "null"
		else:
			return self.list[index].getValue()
	
	def put(self, k, v):
		index = self.find_position(k)
		if index == None:
			# key not found
			self.list.append(KeyValue(k, v))
		else:
			self.list[index].setValue(k)
			# key exists
	def remove(self, k):
		index = self.find_position(k)
		if index == None:
			print "key does not exist!"
		else:
			self.list.pop(index)
	
	def keys(self):
			s = "["
			for x in range(0, len(self.list)):
				if x == len(self.list) - 1:
					s += `self.list[x].getKey()`
				else:
					s += `self.list[x].getKey()` + ", "
			return s + "]"
	
	def values(self):
			s = "["
			for x in range(0, len(self.list)):
				if x == len(self.list) - 1:
					s += `self.list[x].getValue()`
				else:
					s += `self.list[x].getValue()` + ", "
			return s + "]"
	
	def entries(self):
			s = "["
			for x in range(0, len(self.list)):
				if x == len(self.list) - 1:
					s += "(" + `self.list[x].getKey()` + "," + self.list[x].getValue() + ")"
				else:
					s += "(" + `self.list[x].getKey()` + "," + self.list[x].getValue() + "),"
			return s + "]"

	
	def find_position(self, k):
		for x in range(len(self.list)):
			if self.list[x].getKey() == k:
				return x
		return None
	
if __name__ == "__main__":
	list = Map()
	print list.isEmpty()
	list.put(1, "Tanzim")
	list.put(2, "Hello")
	list.put(3, "World")
	list.remove(3)
	print list.entries()
