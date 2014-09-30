alfabeto = ["c","a","s","a"]
P        = ["","","",""]
tam      = 4

def combcomrep(L):
	if len(L)==0:
		print ''.join(P)
	else:
		T = distintos(L)
		for x in xrange(0,len(T)):
			s = T[x]
			P[tam - len(L)] = s
			combcomrep(diferenca(L,s))

def diferenca(alfabet,gg):
	t = []
	s = alfabet[:]
	s.remove(gg)
	if len(s)==0:
		return t
	for a in xrange(0,len(s)):
		t.append(s[a])
	return t

def distintos(alfabet):
	t = []
	for a in xrange(0,len(alfabet)):
		if alfabet[a] not in t:
			t.append(alfabet[a])
	return t

combcomrep(alfabeto)
