class ArrayList():
	def __init__(self):
		self.capacity = 10
		self.size = 0
		self.s = [None] * self.capacity 
		
	def size(self):
		return self.size
	
	def isEmpty(self):
		return self.size == 0
	
	def get(self, i):
		return self.s[i]
	
	def replace(self, i, e):
		self.s[i] = e
	
	def add(self, e):
		if self.capacity == self.size:
			self.checkCap()
		self.s[self.size] = e
		self.size += 1
	
	def remove(self, i):
		self.s[i] = None
		for x in range(i, self.size):
			self.s[x] = self.s[x + 1]
		self.size -= 1
		
		
	def checkCap(self):
		self.capacity = self.capacity * 2
		t = [None] * self.capacity
		## This could possibly be improved?
		for x in range(0, self.size):
			t[x] = self.s[x]
		self.s = t	
		
	def toString(self):
		if self.size == 0:
			return "[]"
		else:
			s = "["
			for x in range(0, self.size):
				if x == (self.size - 1):
					s += self.s[x]
				else:
					s += self.s[x] + ", "
			return s + "]"
			
			
if __name__ == "__main__":
	list = ArrayList()
	print list.isEmpty()
	list.add("Hello")
	list.add("World")
	list.add("My")
	list.add("Name")
	list.add("Is")
	list.add("Tanzim")
	list.remove(1)
	print list.toString()
