from DLL import DLL

class LRUCache(object):
    
    def __init__(self, size=10):
        self.list = DLL()
        self.store = {}
        self.size = size
        print "Cache set with size ", self.size
        print "\nCache Store is \n" 
        print self.store

    def find(self,value):
    	if self.list.find(hash(value)):
    		print "Cache hit..fetching value from Cache"
    		self.setToRecent(value)
    		print "Cache List is"
    		self.list.printList()
    		print "\n"
    		return self.store[hash(value)]
    	else :
    		print "Cache miss.."
    		print "Cache List is"
    		self.list.printList()
    		print "\n"
    		print "adding to the Cache \n"

    		self.addToCache(value)

    		print "\nValue available in the Store is\n"
    		return self.store[hash(value)]

    def removeFromCache(self,value):
    	if value in self.store:
    		del self.store[value]

		print "Cache Store is \n",self.store,"\n"

    def addToCache(self,value):

    	if(self.size==self.list.size):
    		print "Cache size exceeded.removing the last item from cache list"

    		self.removeFromCache(self.list.getLast().value)
    		#if self.list.getLast().value in self.store:
			#	del self.store[self.list.getLast().value]
			#	print "Cache Store is \n",self.store,"\n"
    		self.list.removeLast()


    	if(self.list.size<self.size):
    		self.list.setFirst(hash(value))
    		print "\nNew Cache List is \n"
    		self.list.printList()
    		print "setting the search Value in store with key " + str(hash(value))
    		self.store[hash(value)] = value
    		print "Cache Store is \n",self.store

    def setToRecent(self,value):

    	self.list.remove(hash(value))
    	print "setting the value to most recent in Cache List"
    	self.list.setFirst(hash(value))

    def flush(self):

    	self.list = DLL()
    	self.store = {}
    	print "\nCache List is\n"
    	self.list.printList()
    	print "Cache Store is \n",self.store

    def getStore(self):
    	return self.store

    def getListSize(self):
    	return self.list.getSize()