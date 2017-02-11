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

def assign_hats(num_prisoners):
	"""
	Generate a list of random hat assignments
	"""
	return [random.randrange(2) for x in range(num_prisoners)]

def transition_list(hats):
	"""
	Given a list of hat assignments determine the number of color changes
	at each position. Note that this includes the hat that the prisoner
	can't see!
	"""
	tlist = [0]
	for ii in range(1,len(hats)):
		if hats[ii] != hats[ii-1]:
			tlist += [int(not tlist[ii-1])]
		else:
			tlist += [tlist[ii-1]]
	return tlist

def guess_hats(hats,transitions):
	# checksum=[0 for x in range(len(transitions))]
	guesses=[0 for x in range(len(transitions))]

	# Last prisoner is sacrificial and provides the checksum - the number of
	# Transitions he can see
	#checksum[len(transitions)-1] = transitions[len(transitions)-2]
	guesses[ len(transitions)-1] = transitions[len(transitions)-2]

	# for ii in range(len(transitions)-2,-1,-1):
	# 	checksum = 
	# 	if guesses[ii+1] == transitions[ii-1]:

	# print "checksum:    ", checksum

	# # Every other prisoner looks at ...
	# for ii in range(len(transitions)-2,-1,-1):
	# 	if guesses[ii+1] == transitions[ii-1]:
	# 		if transitions[ii-1] == 0:
	# 			guesses[ii] = hats[0]
	# 		else:
	# 			guesses[ii] = int(not hats[0])
	# 	else:
	# 		if transitions[ii-1] != 0:
	# 			guesses[ii] = hats[0]
	# 		else:
	# 			guesses[ii] = int(not hats[0])
	# for ii in range(len(transitions)-3,-1,-1):
	# 	guesses[ii] = 9

	return guesses

hats = assign_hats(20)
transitions = transition_list(hats)

print "hats:        ", hats
print "transitions: ", transitions
print "guesses:     ", guess_hats(hats,transitions)


