import random

dim_w = 10
dim_h = 6
num_r = 20

src_data = [x[:] for x in [[0]*dim_w]*dim_h]
for ii in range(dim_h):
	src_data[ii] = [random.randrange(num_r) for x in range(dim_w)]

def prettyprint(matrix):
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)

def zero_rows_and_columns(data):
	dim_h = len(data)
	if dim_h < 1:
		return
	dim_w = len(data[0])
	if dim_w < 1:
		return
	skipcol=[]
	for yy in range(dim_h):
		zerocol=[]
		for xx in range(dim_w):
			if xx in skipcol:
				continue
			if data[yy][xx] == 0:
				zerocol += [xx]
		for xx in zerocol:
			for ii in range(dim_h):
				data[ii][xx] = 0
		if zerocol:
			for ii in range(dim_w):
				data[yy][ii] = 0
			skipcol += zerocol

	return data

print "Before"
prettyprint(src_data)
print "After"
prettyprint(zero_rows_and_columns(src_data))