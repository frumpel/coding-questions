
class stack_ar_multi:
	size=0
	count=0
	storage = None
	pointers = None

	def __init__(self,stack_size=20,stack_count=1):
		self.size=stack_size
		self.count=stack_count
		self.pointers = [x*stack_size-1 for x in range(stack_count)]
		self.storage  = [0 for x in range(stack_count*stack_size)]

	def push(self,data,stack_base_zero=0):
		if stack_base_zero < 0 or stack_base_zero >= self.count:
			return "Error: Illegal stack"
		if self.pointers[stack_base_zero] >= self.size * (stack_base_zero + 1) - 1:
			return "Error: Stack full"
		self.pointers[stack_base_zero]+=1
		self.storage[self.pointers[stack_base_zero]] = data
		return "OK: pushed %s onto stack %d in location (%d,%d)" % (
			data,
			stack_base_zero,
			self.pointers[stack_base_zero] - stack_base_zero*self.size,
			self.pointers[stack_base_zero])

	def pop(self,stack_base_zero=0):
		if stack_base_zero < 0 or stack_base_zero >= self.count:
			print "Error: Illegal stack"
			return None
		if self.pointers[stack_base_zero] < self.size * stack_base_zero:
			print "Warning: Stack empty"
			return None
		retval = self.storage[self.pointers[stack_base_zero]]
		self.pointers[stack_base_zero] -= 1
		print "OK: popped %s from stack %d. Ponter now in location (%d,%d)" % (
			retval,
			stack_base_zero,
			self.pointers[stack_base_zero] - stack_base_zero*self.size,
			self.pointers[stack_base_zero])
		return retval


print "Pushing"
sar = stack_ar_multi(5,3)
print sar.push("one")
print sar.push("one",1)
print sar.push("one",2)
print sar.push("one",3)
print sar.push("two")
print sar.push("three")
print sar.push("four")
print sar.push("five")
print sar.push("six")
print sar.push("six")

print "Popping"
print sar.pop()
print sar.pop(1)
print sar.pop(1)
print sar.pop(1)
print sar.pop(2)
print sar.pop(3)
