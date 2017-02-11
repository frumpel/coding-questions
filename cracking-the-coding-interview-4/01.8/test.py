import re

def is_substring(string,fragment):
	if re.search(fragment,string):
		return True
	return False

def is_rotation(origin,rotation):
	if len(origin) != len(rotation):
		return False
	return is_substring(origin + origin,rotation)


print is_rotation("waterbottle", "erbottlewat")