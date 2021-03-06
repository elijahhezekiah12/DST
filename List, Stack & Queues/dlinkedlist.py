class DNode():
	def __init__(self, e, n, p):
		self.element = e
		self.next = n
		self.previous = p
		
	def getElement(self):
		return self.element
		
	def getPrevious(self):
		return self.previous
		
	def getNext(self):
		return self.next
		
	def setElement(self, e):
		self.element = e
		
	def setPrevious(self, e):
		self.previous = e
		
	def setNext(self, e):
		self.next = e
		
class DLinkedList():
	def __init__(self):
		self.size = 0
		self.head = DNode("Head", None, None)
		self.tail = DNode("Tail", None, self.head)
		self.head.setNext(self.tail)
	
	def size(self):
		return self.size()
		
	def isEmpty(self):
		return self.size == 0
		
	def getFirst(self):
		return self.head.getNext()
		
	def getLast(self):
		return self.tail.getPrevious()
		
	def getNext(self, e):
		if self.tail == e:
			print "cannot get next node past the tail of the list"
			return None
		else:
			return e.getNext()	

			
	def removeLast(self):
		if self.size == 0:
			print "list is empty!"
		else:
			v = self.tail.getPrevious()
			u = v.getPrevious()
			self.tail.setPrevious(u)
			u.setNext(self.tail)
			v.setPrevious(None)
			v.setNext(None)
			self.size -= 1
			
	def addAfter(self, n, e):
		# add after node n, new node e to be added
		t = n.getNext()
		e.setPrevious(n)
		e.setNext(t)
		t.setPrevious(e)
		n.setNext(e)
		self.size += 1
		
	def addBefore(self, n, e):
		# add before node n, new node e to be added
		t = n.getPrevious()
		e.setPrevious(t)
		e.setNext(n)
		n.setPrevious(e)
		t.setNext(e)
		self.size += 1
			
	def addFirst(self, e):
		self.addAfter(self.head, e)
		
	def addLast(self, e):
		self.addBefore(self.tail, e)
		
	def remove(self, e):
		u = e.getPrevious()
		v = e.getNext()
		u.setNext(v)
		v.setPrevious(u)
		e.setPrevious(None)
		e.setNext(None)
		self.size -= 1
		
	def hasPrevious(self, e):
		return e != self.head
		
	def hasNext(self, e):
		return e != self.tail
			
	def toString(self):
		s = "["
		e = self.head.getNext()
		while e != self.tail:
			s += e.getElement()
			e = e.getNext()
			if e != self.tail:
				s += ","
		s += "]"
		return s	
		
if __name__ == "__main__":
	dl = DLinkedList()
	dl.addFirst(DNode("Hello", None, None))
	dl.addLast(DNode("World", None, None))
	dl.addBefore(dl.getLast(), DNode("Tanzim", None, None))
	dl.remove(dl.getLast())
	print dl.toString()	
	print dl.isEmpty()
	dl.removeLast()
	print dl.toString()	
