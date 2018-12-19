import math

res=[]
def recurse(putar,stack,popar):
    if len(putar)==0 and len(stack)==0:
        res.append(popar)
    if len(putar)>0:
        recurse(putar[1:],stack[:]+[putar[0]],popar[:])
    if len(stack)>0:
        recurse(putar[:],stack[:-1],popar[:]+[stack[-1]])


def find(putar,stack,popar):
    if len(putar)==0 and len(stack)==0:
        print popar == out, popar, out
        return popar == out
    if len(putar)>0:
        if find(putar[1:],stack[:]+[putar[0]],popar[:]):
            return True
    if len(stack)>0:
        if find(putar[:],stack[:-1],popar[:]+[stack[-1]]):
            return True
    return False

# n=5
# recurse(range(n),[],[])
# for ii in res:
#     print ii
# print len(res),math.factorial(n)

src=[1,2,3,4,5]
out=[4,3,5,1,2]
res=find(src,[],[])
print res
