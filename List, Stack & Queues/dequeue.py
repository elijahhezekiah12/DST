class Dequeue():
	
	def __init__(self):
		self.items = []
		
	def addHead(self, item):
		self.items.append(item)
		
	def addTail(self, item):
		self.items.insert(0, item)
		
	def removeHead(self):
		return self.items.pop()
		
	def removeTail(self):
		return self.items.pop(0)
		
	def isEmpty(self):
		return self.items == []
		
	def size(self):
		return len(self.items)
	
if __name__ == "__main__":
	dequeue = Dequeue()
	dequeue.addHead("Hello")
	dequeue.addTail("World")
	print dequeue.removeHead()
	print dequeue.removeHead()
