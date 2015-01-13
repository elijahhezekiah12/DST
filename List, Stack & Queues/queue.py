class Queue():

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	
	def isEmpty(self):
		return self.items == []
		
	def size(self):
		return len(self.items)
	
if __name__ == "__main__":
	queue = Queue()
	print queue.isEmpty()
	queue.enqueue("Hello")
	queue.enqueue("World")
	print queue.size()
	print queue.isEmpty()
	print queue.dequeue()
	print queue.dequeue()
