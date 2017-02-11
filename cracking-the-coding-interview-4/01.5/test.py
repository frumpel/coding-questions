"""
This is a horrible idea because it's probably n^2 on the append. If we 
wanted this faster we could allocate a bytearray that's 3n long
"""

def url_escape_space(input_string):
	output_string = ""
	for ii in input_string:
		if ii == " ":
			output_string += "%20"
		else:
			output_string += ii
	return output_string

ts="a b c  d"
print "'%s', '%s'" % (ts,url_escape_space(ts))