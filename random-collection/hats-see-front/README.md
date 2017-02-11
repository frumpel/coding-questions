# Hats problem - single file

## Problem statement: 

* death row prisoners are given a chance to go free if they guess their hat
* they can talk to each other
* they can only see the hats in front of them, not behind them
* they can say a color but nobody knows if it was right or not
* expected: save all but one and the last has a 50% chance

## Approach 1

NOTE: Although I like the concept I don't think this solution works as implemented. Basically it approaches this as a form of "Forward Error Correction" coding where the last person (who can see all hats except his own) provides a checksum. 

* blue - 0
* red - 1
* everyone counts the number of transitions flipping the bit starting with blue == no transitions
* last person gives the number of transitions = 50%
* everyone else counts transtions 

## Approach 2

This uses the same logic with the added observation that the simplest checksum coding is XOR. 

* The first prisoner (who can see all hats except his own) calculates XOR as follows: start with the color number of the farthest prisoner he can see and then XORs it with each hat color until he reaches the prisoner closest to him. Since he has no information about his own hat he has a 50% chance of surviving
* Each subsequent prisoner calculates XOR starting with the the color number of the farthest prisoner he can see and then XORs it with each hat color until he reaches the prisoner closest to him. He then continues to XOR this with the colors mentioned by all prisoners who came before.