"""
Problem statement: 

* death row prisoners are given a chance to go free if they guess their hat
* they can talk to each other
* they can only see the hats in front of them, not behind them
* they can say a color but nobody knows if it was right or not
* expected: save all but one and the last has a 50%% chance

Approach:

* blue - 0
* red - 1
* everyone counts the number of transitions flipping the bit starting with blue == no transitions
* last person gives the number of transitions = 50%
* everyone else counts transtions 

"""

import random

num_prisoners = 10


def calc_xor(src):
	# We are counting right to left. Init with last prisoner
	xor = src[len(src)-1]

	# XOR all remaining values
	for ii in range(len(src)-2,-1,-1):
			xor=xor^src[ii]

	return xor



# Create a random list of hat assignments
src = [random.randrange(2) for x in range(num_prisoners)]

# Initialize temporary data arrays
crc = [False for x in range(num_prisoners)]
ans = [-1 for x in range(num_prisoners)]

# First prisoner answers with the XOR checksum
ans[0] = calc_xor(src[1:])

# All other prisoners answer with xor(hats they see)^xor(what prisoners have said)
for ii in range(1,num_prisoners):
	# Calculate the XOR checksum - note that the checksum is already in ans[0]
	ans[ii] = calc_xor(ans[:ii] + src[ii+1:])

# Output
print "Hats (looking right):",src
print "Prisoner says:       ",ans
print "Is it true?          ",[ans[ii]==src[ii] for ii in range(len(src))]


