from sll import singly_linked_list


sl = singly_linked_list()

sl.append_datac("n-9")
sl.append_datac("n-8")
sl.append_datac("n-7")
sl.append_datac("n-6")
sl.append_datac("n-5")
sl.append_datac("n-4")
sl.append_datac("n-3")
sl.append_datac("n-2")
sl.append_datac("n-1")
sl.append_datac("n-0")

print "0-th"
print sl.find_nth_from_last_element(0)

print "5-th"
print sl.find_nth_from_last_element(5)

print "15-th"
print sl.find_nth_from_last_element(15)
