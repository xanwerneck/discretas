conj = ["a","b","c","d"]
r  = 2
p= ["",""]
p2=["","","",""]
n  = 4

def geraconjuntos(conj,n):
	if len(conj)==0:
		print ''.join(p2)	
	else:
		for x in xrange(0,len(conj)):
			p2[n-len(conj)] = conj[x]
			geraconjuntos(df(conj, conj[x]))

def df(cj,y):
	b = []
	for x in xrange(0,len(cj)):
		if cj[x] != y:
			b.append(cj[x])
	return b

def remove_em_p(alfabet, p):
	T = []
	for x in xrange(0, len(alfabet)):
		if alfabet[x] not in p:
			T.append(alfabet[x])
	return T

geraconjuntos(conj,0)