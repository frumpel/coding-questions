

def prettyprint(matrix):
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)

def rotate_nxn_image_with_carry(data):
	dim1 = len(data)
	if dim1 < 2:
		return
	dim2 = len(data[0])
	if dim2 != dim1:
		return

	for jj in range(dim1/2):
		# print
		for ii in range(jj,dim1-1-jj):
			# print "(%d,%d) (%d,%d) (%d,%d) (%d,%d)" % (
			# 	ii,jj,
			# 	dim1-1-jj,ii,
			# 	dim1-1-ii,dim1-1-jj,
			# 	jj,dim1-1-ii)
			carry = data[ii       ][jj       ]
			data[ii       ][jj       ] = data[dim1-1-jj][ii       ]
			data[dim1-1-jj][ii       ] = data[dim1-1-ii][dim1-1-jj]
			data[dim1-1-ii][dim1-1-jj] = data[jj       ][dim1-1-ii]
			data[jj       ][dim1-1-ii] = carry
	return data

def point_recalc_matrix_90(sx,sy,sw,sh):
	"""
	This is an attempt at using a rotation matrix. The problem is, though,
	that the resulting coordinates will be negative!

	90deg counterclockwise matrix
	|  cos  sin | = |  0  -1 | | x |
	| -sin  cos |   |  1   0 | | y |

	90deg clockwise matrix
	|  cos  sin | = |  0   1 | | x |
	| -sin  cos |   | -1   0 | | y |
	"""
	# # for 90deg counter? clockwise y will become negative so add width
	# ox =  0
	# oy = sw-1
	# nx = ox +  0 * sx +  1 * sy
	# ny = oy + -1 * sx +  0 * sy
	# return (nx,ny)

	# for 90deg clockwise? y will become negative so add width
	ox = sh-1
	oy = 0
	nx = ox +  0 * sx + -1 * sy
	ny = oy +  1 * sx +  0 * sy
	return (nx,ny)


def rotate_mxn_image_with_matrix(src_data):
	"""
	Prealloc from here: http://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
	Rotation matrix: http://www.datagenetics.com/blog/august32013/index.html
	"""
	dim_h=len(src_data)
	if dim_h < 2:
		return
	dim_w=len(src_data[0])
	if dim_w < 2:
		return
	dst_data = [x[:] for x in [[0]*dim_h]*dim_w]

	for yy in range(dim_h):
		for xx in range(dim_w):
			(nx,ny) = point_recalc_matrix_90(xx,yy,dim_w,dim_h)
			# dst_data[xx][yy]
			# print "(%d,%d) -> (%d,%d)" % (xx,yy,nx,ny)
			dst_data[ny][nx] = src_data[yy][xx]

	return dst_data

image_odd=[
  [ 1, 2, 3, 4, 5],
  [ 6, 7, 8, 9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25]
]

image_even=[
  [ 1, 2, 3, 4],
  [ 5, 6, 7, 8],
  [ 9,10,11,12],
  [13,14,15,16],
]

print "Swapping rotation"
print "Image with odd dimensions:"
print "Before:"
prettyprint(image_odd)
print "After:"
prettyprint(rotate_nxn_image_with_carry(image_odd))

print "Image with even dimensions:"
print "Before:"
prettyprint(image_even)
print "After:"
prettyprint(rotate_nxn_image_with_carry(image_even))


image_odd=[
  [ 1, 2, 3, 4, 5],
  [ 6, 7, 8, 9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25]
]

image_even=[
  [ 1, 2, 3, 4],
  [ 5, 6, 7, 8],
  [ 9,10,11,12],
  [13,14,15,16],
]

print
print "Matrix rotation"
print "Image with odd dimensions:"
print "Before:"
prettyprint(image_odd)
print "After:"
prettyprint(rotate_mxn_image_with_matrix(image_odd))

print "Image with even dimensions:"
print "Before:"
prettyprint(image_even)
print "After:"
prettyprint(rotate_mxn_image_with_matrix(image_even))

