class queue_ll_node:
	data = None
	prev = None

	def __init__(self,data,prev):
		self.data = data
		self.prev = prev

	def get_data(self):
		return self.data

	def get_prev(self):
		return self.prev

	def set_prev(self,prev):
		self.prev = prev

class queue_ll_basic:
	head = None
	tail = None

	def enqueue(self,data):
		if self.tail:			
			oldtail = self.tail
			self.tail = queue_ll_node(data,None)
			oldtail.set_prev(self.tail)
		else:
			self.head = self.tail = queue_ll_node(data,None)

	def dequeue(self):
		if not self.head:
			return None
		else:
			ret = self.head.get_data()
			if self.head.get_prev():
				self.head = self.head.get_prev()
			else:
				self.tail = self.head = None
		return ret

	def print_stack(self):		
		ptr=self.head
		while ptr:
			print ptr.get_data()
			ptr = ptr.get_prev()

print "Enqueueing"
sls = queue_ll_basic()
sls.enqueue("one")
sls.enqueue("two")
sls.enqueue("three")
sls.enqueue("four")
sls.enqueue("five")
print "Printing"
sls.print_stack()

print "Dequeueing"
print sls.dequeue()
print sls.dequeue()
print sls.dequeue()
print sls.dequeue()
print sls.dequeue()
print sls.dequeue()
print sls.dequeue()
