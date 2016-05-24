
The LRU Cache is implemented with a Double linked List as a Queue.
The values to be searched in the Cache are hashed and the hashes are stored in the linked list
the Values along with their hashes are stored in a python dictionary

DLL.py class holds the implementation of the Doubley Linked List
the DLL can be tested individually with the following commands in python interpreter

"
from DLL import DLL 
x = DLL()
"
the various methods n the DLL class are as follows
setFirst(value) : creates a node in the DLL and and adds it as the front Node
setLast(value) : creates a node in the DLL and and adds it as the last Node
removeFirst() : removes the first node in the DLL
removeLast() : removes the last node in the DLL
remove(value) : remoes a Node with the given value 
find(value) : searches for the value in the nodes and returns true if found else returns false

LRU class holds the implementation of the Least Recently Used Cache

the LRU can be tested individually with the following commands in python interpreter

"
from LRU import LRUCache
x = LRUCache()
"

will create an LRUCache object with no of items in caache set to 10

in order to specify the number of items in the cache as a size the followiing command can be alternatively used
"
x= LRUCache(5)
"
if you need five items to be stored in the Cache

The main method in the Cache is 

find(value) : searches for a value in the cahce. If found updates the most recent value in Queue. If not found adds the value to the store and updates the most recent value in Queue. Both Nubers and Strings can be used as values.

ex: find(2),find('2'),find('Harry Potter')

setToRecent(value) : updates the most recent value in Queue with the given Hash Value
removeFromCache(value) : removes the given entry stored in Cache store with key given

flush() : flushes the given Cache. both the store and Queue are reset

