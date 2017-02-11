"""
Building a linked likst based on an array class is a terrible idea :)
Note that this makes it really hard to kill off the head node
"""

class single_link_list_array:
	# Head of our data
	Nodes = []

	def hello_world(self):
		print "hello_world"

	def add_node(self,data):
		tl = len(self.Nodes)
		self.Nodes += [[data,0]]
		if tl > 0:
			self.Nodes[tl-1][1] = tl 
		print self.Nodes

	def get_node_by_seq_base1(self,n):
		if len(self.Nodes) <= 0:
			return []
		index=0
		count=1
		while True:
			if count == n:
				return self.Nodes[index]
			if self.Nodes[index][1] == 0:
				return []
			index=self.Nodes[index][1]
			count+=1

	def remove_node_by_seq_base1(self,n):
		if len(self.Nodes) <= 0:
			return []
		index=0
		count=1
		while True:
			if count == n-1:
				print "Deleting node at count ",count," index ",index
				self.Nodes[index][1] = self.Nodes[self.Nodes[index][1]][1]
				print "Deletion done: ",self.Nodes
				return
			if self.Nodes[index][1] == 0:
				return
			index=self.Nodes[index][1]
			count+=1


	# def remove_node_duplicate_nodes(self):
	# 	if len(self.Nodes):
	# 		return
	# 	index = 0
	# 	while True:
	# 		data = self.Nodes[index][0]
	# 		index2 = self.Nodes[index][1]
	# 		if index2 == 0:
	# 			print "End of list! ", self.Nodes
	# 			return
	# 		if self.Nodes[index][0] == self.Nodes[index2][0]:
	# 			self





sl = single_link_list_array()
sl.hello_world()
sl.add_node("one")
sl.add_node("two")
sl.add_node("three")
sl.add_node("four")
print sl.get_node_by_seq_base1(2)
print sl.get_node_by_seq_base1(4)
print sl.get_node_by_seq_base1(5)
sl.remove_node_by_seq_base1(1)