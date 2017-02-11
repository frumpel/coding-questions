from sll import singly_linked_list

print "Test 0: basic linked list functions: create / print / delete"

sl = singly_linked_list()

sl.append_datac("zero")
sl.append_datac("two")
sl.append_datac("one")
sl.append_datac("two")
sl.print_list()

sl.delete_first_node_matching_data("two")
sl.print_list()
