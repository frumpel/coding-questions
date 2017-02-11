mystring = bytearray("abcdabcdaa")

def remove_duplicates(string):
	ba = bytearray(string)
	ml = len(ba)
	ii = 0
	while ii < ml:
		jj = ii+1
		while jj < ml:
			if ba[jj] == ba[ii]:
				kk = jj + 1
				while kk < ml - 1:
					ba[kk]=ba[kk+1]
					kk += 1
				ml -= 1
			else:
				jj += 1
		ii += 1
	return str(ba[0:ml])

def test_remove_duplicates(string,expected):
	result  = remove_duplicates(string)
	success = result == expected
	if success:
		print "test succeeded: %s -> %s == %s" % (string,result,expected)
	else:
		print "test failed:    %s -> %s != %s" % (string,result,expected)
	return success

print "Function run"
print remove_duplicates(mystring)

print "Test runs"
test_remove_duplicates("ok",      "fail")
test_remove_duplicates("abcd",    "abcd")
test_remove_duplicates("abcdaaaa","abcd")
test_remove_duplicates("abcdabab","abcd")
test_remove_duplicates("",        "")