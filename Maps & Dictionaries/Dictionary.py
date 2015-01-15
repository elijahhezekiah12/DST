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
		
class Dictionary():
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

	def getAll(self, k):
		s = "["
		for x in range(0, len(self.list)):
			if self.list[x].getKey() == k:
					s += "(" + `self.list[x].getKey()` + "," + `self.list[x].getValue()` + ")"
		return s + "]"
	
	def put(self, k, v):
		if self.find_match(k,v) is not True:
			self.list.append(KeyValue(k, v))
		else:
			print "already exists!"

	def remove(self, k):
		index = self.find_position(k)
		if index == None:
			print "entry does not exist!"
		else:
			self.list.pop(index)
	
	
	def entrySet(self):
			s = "["
			for x in range(0, len(self.list)):
				if x == len(self.list) - 1:
					s += "(" + `self.list[x].getKey()` + "," + `self.list[x].getValue()` + ")"
				else:
					s += "(" + `self.list[x].getKey()` + "," + `self.list[x].getValue()` + "),"
			return s + "]"
			
	def find_match(self, k, v):
		for x in range(len(self.list)):
			if self.list[x].getKey() == k and self.list[x].getValue() == v:
				return True
			else:
				return False
	
	def find_position(self, k):
		for x in range(len(self.list)):
			if self.list[x].getKey() == k:
				return x
		return None
	
if __name__ == "__main__":
	list = Dictionary()
	print list.isEmpty()
	list.put("Hello", "Used to express a greeting, answer a telephone, or attract attention")
	list.put("Hello", "Not Available")
	list.put("World", "The earth or globe, considered as a planet")
	list.put("Tanzim", "It is my name!!!")
	list.remove("Tanzim")
	print list.entrySet()
	print list.getAll("Hello")
