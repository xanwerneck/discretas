	
alfabeto = [
	[1,2,3,4]
]

p = [0,0,0,0]
n = 4

def anagrama(alf):
	if len(alf)==0:
		print p
	else:
		T = distintos(alf)
		for x in xrange(0,len(T)):
			s = T[x]
			p[n - len(alf)] = s
			if (n - len(alf)) == 0:
				anagrama(diferenca(alf,s))
			else:
				if p[n-len(alf)] != p[(n-len(alf))-1]:
					anagrama(diferenca(alf,s))

def distintos(alf):
	a = []
	for x in xrange(0,len(alf)):
		if alf[x] not in a:
			a.append(alf[x])
	return a

def diferenca(alfabet,gg):
	t = []
	s = alfabet[:]
	s.remove(gg)
	if len(s)==0:
		return t
	for a in xrange(0,len(s)):
		t.append(s[a])
	return t

anagrama(alfabeto[0])
