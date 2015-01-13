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
		
		
class SLinkedList():
	
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
		
	def addFirst(self, n):
		n.setNext(self.head)
		self.head = n
		self.size += 1
		
		if self.tail == None:
			self.tail = self.head
		
	def addLast(self, n):
		n.setNext(None)
		self.tail.setNext(n)
		self.tail  = n
		self.size += 1
		
	def removeFirst(self):
		if self.head == None:
			print "list is empty"
		else:
			temp = self.head
			self.head = self.head.getNext()
			temp.setNext(None)
			self.size -= 1
		
	def getHead(self):
		return self.head
		
	def getTail(self):
		return self.tail
		
if __name__ == "__main__":
	slist = SLinkedList()
	
	n1 = Node("Hello", None)
	slist.addFirst(n1)
	print slist.getHead().getElement() + " - " +  slist.getTail().getElement()
	
	n1 = Node("World", None)
	slist.addFirst(n1)
	print slist.getHead().getElement() + " - " +  slist.getTail().getElement()
	
	n1 = Node("Singly", None)
	slist.addFirst(n1)
	print slist.getHead().getElement() + " - " +  slist.getTail().getElement()
	
	n1 = Node("LinkedList", None)
	slist.addLast(n1)
	print slist.getHead().getElement() + " - " +  slist.getTail().getElement()
	

