from sll import singly_linked_list

class ll_number:
	number = None

	def __init__(self,number):
		self.number = singly_linked_list()
		for ii in str(number)[::-1]:
			self.number.append_datac(int(ii))

	def __get_head__(self):
		return self.number.get_head()

	def add_ll_numbers(self,ll_number):
		sle1 = self.number.get_head()
		sle2 = ll_number.__get_head__()
		if not sle1 or not sle2:
			return None
		nsum = 0
		npow = 1
		while sle1 or sle2:
			if sle1:
				nsum += sle1.get_data()*npow
				sle1 =  sle1.get_next()
			if sle2:
				nsum += sle2.get_data()*npow
				sle2 =  sle2.get_next()
			npow *= 10
		return nsum



print "Test 0: Addition without carry"

n1 = 123
n2 = 123
n1l = ll_number(n1)
n2l = ll_number(n2)
print n1,"+",n2,"=",n1l.add_ll_numbers(n2l)

print "Test 1: Addition with carry"

n1 = 513
n2 = 295
n1l = ll_number(n1)
n2l = ll_number(n2)
print n1,"+",n2,"=",n1l.add_ll_numbers(n2l)

print "Test 2: Addition with different lenghts"

n1 = 1513
n2 = 295
n1l = ll_number(n1)
n2l = ll_number(n2)
print n1,"+",n2,"=",n1l.add_ll_numbers(n2l)
