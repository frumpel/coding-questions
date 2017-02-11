from sll import singly_linked_list

print "Test 2a: deleting duplicates with the help of a hash"

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


print "Test 2b: deleting duplicates with the help of a runner"

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
