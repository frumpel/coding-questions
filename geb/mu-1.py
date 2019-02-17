# Rule 1: xI -> xIU
# Rule 2: Mx -> Mxx
# Rule 3: III -> U
# Rule 4: UU -> 0
# Exit 1: MU
# Exit 2: depth
# Exit 3: already seen

from collections import defaultdict
# At 8 this generates 8k results in about 0.3s + 10s for printing
MAX_DEPTH=8
seen = defaultdict(list)

def MU_0001(input,depth,history):
    # print input, depth, history
    if input == "MU":
        print "MU reached via ", history
        return
    if depth>MAX_DEPTH:
        # print "Done at depth ", depth, " with history ", history
        return
    if input in seen:
        # print "Done because already seen ", input
        return

    # Track input in seen
    seen[input].append(history)

    # Rule 1
    if input[-1] == "I":
        ns=input + "U"
        MU_0001(ns,depth+1,history+[ns])
    # Rule 2
    if input[0] == "M":
        ns=input[0]+input[1:]+input[1:]
        MU_0001(ns,depth+1,history+[ns])
    # Rule 3 - could have multiple replacepment options
    for ii in range(len(input)-3):
        if input[ii:ii+3] == "III":
            ns=input[0:ii]+"U"+input[ii+3:]
            MU_0001(ns,depth+1,history+[ns])
    # Rule 4 - could have multiple replacement options
    for ii in range(len(input)-2):
        if input[ii:ii+2] == "UU":
            ns=input[0:ii]+input[ii+2:]
            MU_0001(ns,depth+1,history+[ns])

MU_0001("MI",0,[])
for ii in sorted(seen):
    print ii,seen[ii]
