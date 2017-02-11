

def is_anagram(s1,s2):
	if ''.join(sorted(s1)) == ''.join(sorted(s2)):
		print "is anagram:  %s / %s" % (s1,s2)
		return True
	else:
		print "is not anagram:  %s / %s" % (s1,s2)
		return False

is_anagram("tuba","abut")
is_anagram("yes", "no")

