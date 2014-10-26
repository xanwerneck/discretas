import sys

n = 4

festa = [
	[1,2],
	[0,2,3],
	[0,1],
	[1]
]


n2 = 7

festa2 = [
	[1,2,3],
	[0],
	[0],
	[0],
	[5,6],
	[4,6],
	[4,5]
]

def comunidade(q,fest):
	if q!=0:
		for x in xrange(0,len(fest)):
			if len(fest[x]) == q:
				p = montaVetor(fest[x],x)
				est = checaRelacoes(fest[x])
				if est == 1:
					print p
					sys.exit(0)
			else:
				comunidade(q-1,fest)

def checaRelacoes(festai):
	for x in xrange(0,len(festai)):
		f = festa[festai[x]]
		for y in xrange(0,len(festai)):
			if (x!=y) and (festai[y] not in f):
				return 0
	return 1

def montaVetor(fest,x):
	t = []
	t.append(x)
	for x in xrange(0,len(fest)):
		t.append(fest[x])
	return t

comunidade(n2-1,festa2)
