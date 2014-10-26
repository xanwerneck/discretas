conj = ["a","b","c","d"]
r  = 2
p  = ["","","",""]
p2 = ["",""]

def perm1(cj):
	if len(cj)==0:
		print ''.join(p)
	else:			
		for x in xrange(0,len(cj)):
			p[r - len(cj)] = cj[x]
			perm1(df(cj, cj[x]))


def perm2(cj,n):
	if n==0:
		print ''.join(p2)
	else:			
		for x in xrange(0,len(cj)):
			p2[r-n] = cj[x]
			perm2(df(cj, cj[x]),n-1)

def df(cj,y):
	b = []
	for x in xrange(0,len(cj)):
		if cj[x] != y:
			b.append(cj[x])
	return b

perm1(conj)
#perm2(conj,r)


