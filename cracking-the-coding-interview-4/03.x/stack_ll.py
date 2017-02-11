class stack_ll_node:
	data = None
	prev = None

	def __init__(self,data,prev):
		self.data = data
		self.prev = prev

	def get_data(self):
		return self.data

	def get_prev(self):
		return self.prev

class stack_ll_basic:
	top = None

	def push(self,data):
		if self.top:
			self.top = stack_ll_node(data,self.top)
		else:
			self.top = stack_ll_node(data,None)

	def pop(self):
		if not self.top:
			print "stack is empty"
			return None
		else:
			ret = self.top.get_data()
			if self.top.get_prev():
				self.top = self.top.get_prev()
			else:
				self.top = None
		return ret

	def print_stack(self):		
		ptr=self.top
		while ptr:
			print ptr.get_data()
			ptr = ptr.get_prev()

print "Pushing"
sls = stack_ll_basic()
sls.push("one")
sls.push("two")
sls.push("three")
sls.push("four")
sls.push("five")
print "Printing"
sls.print_stack()

print "Popping"
print sls.pop()
print sls.pop()
print sls.pop()
print sls.pop()
print sls.pop()
print sls.pop()
