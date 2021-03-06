class Node():

	def __init__(self, e, n):
		self.element = e
		self.next = n
		
	def getElement(self):
		return self.element
		
	def getNext(self):
		return self.next
		
	def setElement(self, e):
		self.element = e
		
	def setNext(self, n):
		self.next = n
		
class CircularList():
	
	def __init__(self):
		self.cursor = None
		self.size = 0
		
	def size(self):
		return self.size
		
	def getCursor(self):
		return self.cursor
		
	def advance(self):
		self.cursor = self.cursor.getNext();
		
	def add(self, e):
		if self.cursor == None:
			e.setNext(e)
			self.cursor = e
		else:
			e.setNext(self.cursor.getNext())
			self.cursor.setNext(e)
		self.size+= 1
		
	def remove(self):
		n = self.cursor.getNext()
		if n == self.cursor:
			self.cursor = None
		else:
			self.cursor.setNext(n.getNext())
			n.setNext(None)
		self.size -= 1
		return n
		
	def toString(self):
		if self.cursor == None:
			return "[]"
		else:
			s = "[.." + self.cursor.getElement()
			n = self.cursor
			self.advance()
			while n != self.cursor:
				s += ", " + self.cursor.getElement()
				self.advance()
			return s + "...]"
			
if __name__ == "__main__":
	cl = CircularList()
	cl.add(Node("Tanzim", None))
	cl.add(Node("Bob", None))
	cl.advance()
	print cl.getCursor().getElement()
	cl.add(Node("Jen", None))
	print cl.toString()
