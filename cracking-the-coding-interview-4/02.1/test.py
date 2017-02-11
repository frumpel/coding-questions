from collections import defaultdict

class singly_linked_list_node:
	data = None;
	next = None;

	def __init__(self,data):
		# print "SLN: Init with ", data
		self.set_data(data)

	def set_data(self,data):
		# print "SLN: Set data with ", data
		self.data = data

	def set_next(self,next):
		# print "SLN: Set next with ", next
		self.next = next

	def append_data(self,data):
		# print "SLN: Append data with ", data
		self.next = singly_linked_list_node(data)

	def get_data(self):
		# print "SLN: get data", self.data
		return self.data

	def get_next(self):
		# print "SLN: returning next",self.next
		return self.next

class singly_linked_list:
	head = None

	def print_list(self):
		ptr = self.head
		while ptr:
			print "Entry:",ptr.get_data()
			ptr = ptr.get_next()

	def append_datac(self,data):
		if not self.head:
			# print "inserting head"
			self.head = singly_linked_list_node(data)
		else:
			ptr = self.head
			while ptr.get_next():
				# print "PTR: ", ptr.get_next()
				ptr = ptr.get_next()
			# print "inserting child"
			ptr.append_data(data)

	def delete_first_node_matching_data(self,data):
		if not self.head:
			return
		if self.head.get_data() == data:
			print "deleting/resetting head"
			self.head = self.head.next
			return
		ptr=self.head
		while ptr.get_next():
			if ptr.get_next().get_data() == data:
				print "deleting/resetting child"
				ptr.set_next(ptr.get_next().get_next())
				return
			ptr=ptr.get_next()

	def remove_duplicates_with_hash(self):
		if not self.head:
			# print "RDH: exit on empty list"
			return
		ptr = self.head
		dup = defaultdict(int)
		dup[ptr.get_data()]+=1
		while ptr.get_next():
			if dup[ptr.get_next().get_data()]:
				# print "RDH: found",ptr.get_next().get_data(),"in hash"
				ptr.set_next(ptr.get_next().get_next())
			else:
				# print "RDH:",ptr.get_next().get_data(),"not found in hash. Amending hash"
				dup[ptr.get_next().get_data()]+=1
				ptr=ptr.get_next()

	def remove_duplicates_with_runner(self):
		if not self.head:
			# print "RDH: exit on empty list"
			return
		ptr1 = self.head
		while ptr1 and ptr1.get_next():
			# Immediate followers are handled as a special case ?
			# while ptr1 and ptr1.get_next().get_data() == ptr1.get_data():
			# 	ptr1.set_next(ptr1.get_next().get_next())
			run_prv=ptr1
			run_cur=ptr1.get_next()
			while run_cur:
				if run_cur.get_data() == ptr1.get_data():
					run_prv.set_next(run_cur.get_next())
					run_cur = run_prv.get_next()
				else: 
					run_prv = run_prv.get_next()
					run_cur = run_cur.get_next()
			# Note: this can assign a NULL pointer thus the existence check above
			ptr1 = ptr1.get_next()



print "Test 0: basic linked list functions: create / print / delete"

sl = singly_linked_list()

sl.append_datac("zero")
sl.append_datac("two")
sl.append_datac("one")
sl.append_datac("two")
sl.print_list()

sl.delete_first_node_matching_data("two")
sl.print_list()

print "2.1: Test 2a: deleting duplicates with the help of a hash"

sl = singly_linked_list()

sl.append_datac("zero")
sl.append_datac("zero")
sl.append_datac("one")
sl.append_datac("two")
sl.append_datac("two")
sl.append_datac("three")
sl.append_datac("two")
sl.append_datac("two")
sl.append_datac("four")
sl.append_datac("four")

print "Before deletion"
sl.print_list()

sl.remove_duplicates_with_hash()

print "After deletion"
sl.print_list()


print "2.1: Test 2b: deleting duplicates with the help of a runner"

sl = singly_linked_list()

sl.append_datac("zero")
sl.append_datac("zero")
sl.append_datac("one")
sl.append_datac("two")
sl.append_datac("two")
sl.append_datac("three")
sl.append_datac("two")
sl.append_datac("two")
sl.append_datac("four")
sl.append_datac("four")

print "Before deletion"
sl.print_list()

sl.remove_duplicates_with_runner()

print "After deletion"
sl.print_list()
