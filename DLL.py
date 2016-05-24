class Node(object):
	
	def __init__(self,value=None):
		self.value = value
		self.prev = None
		self.next = None

#DoublyLinkedList
class DLL(object):

	def __init__(self,value=None):
		if value == None:
			self.first = None
			self.last = None
			self.size = 0
		else:
			self.first = Node(value)
			self.last = self.first
			self.size = 1

	def getFirst(self):
		return self.first

	def getLast(self):
		return self.last

	def getSize(self):
		return self.size

	def setFirst(self,value):
		newNode = Node(value)

		if(self.size == 0):
			self.first = newNode
			self.last = newNode
		else:
			newNode.next = self.first
			newNode.prev = self.first.prev

			self.first.prev = newNode

			self.first = newNode

		self.size+=1

	def setLast(self,value):
		newNode = Node(value)

		if(self.size == 0):
			self.first = newNode
			self.last = newNode
		else:
			newNode.next = self.last.next
			newNode.prev = self.last

			self.last.next = newNode

			self.last = newNode

		self.size+=1

	def removeFirst(self):

		if(self.size >1):
			tempNode = self.first.next

			tempNode.prev = self.first.prev
			self.first.next = None

			self.first = tempNode

			self.size-=1

		else:
			self.first = None
			self.last = None
			self.size = 0

	def removeLast(self):

		if(self.size >1):
			tempNode = self.last.prev

			tempNode.next = self.last.next
			self.last.prev = None

			self.last = tempNode

			self.size-=1

		else:
			self.first = None
			self.last = None
			self.size = 0

	def remove(self,value):

		tempNode = self.first


		if self.first.value == value:
			self.removeFirst()

		elif self.last.value == value:
			self.removeLast()

		else:
			found = True
			while tempNode.value != value:
				if(tempNode.next is None):
					print "value not found"
					found = False
					break
				else:
					tempNode = tempNode.next

			if(found):
				tempNode.prev.next = tempNode.next
				tempNode.next.prev = tempNode.prev

				tempNode.prev = None
				tempNode.next = None

				self.size-=1

	def find(self,value):
		found = False

		tempNode = self.first

		if(self.size>0):
			if self.first.value == value:
				found = True

			elif self.last.value == value:
				found = True

			else:
				while tempNode.next is not None:
					if tempNode.value == value:
						found = True
					tempNode = tempNode.next

		return found
	
	def printList(self):

		tempNode = self.first
		
		if(self.size>0):
			while tempNode.next is not None:
				print tempNode.value
				tempNode = tempNode.next
			print tempNode.value






