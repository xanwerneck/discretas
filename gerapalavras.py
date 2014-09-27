alfabeto = ["a","b","c"]
p = ["","",""]
t = 3;

def gerapalavras(n):
	if n==0:
		print ''.join(p)
	else:
		for i in xrange(0,len(alfabeto)):
			p[t-n] = alfabeto[i]
			gerapalavras(n-1)

S = []
def gerapermutacoes(alfa):
	if len(alfa)==0:
		print ''.join(S)
	else:
		for x in xrange(0,len(alfa)):
			s = alfa[x]
			S.append(s)
			gerapermutacoes(diferenca(alfa, S))
			S.remove(s)

def gerapermutacoesultimo(alfa):
	if len(alfa)==0:
		print ''.join(S)
	else:
		for x in xrange(0,len(alfa)):
			s = alfa[len(alfa)- (x+1)]
			S.append(s)
			gerapermutacoesultimo(diferenca(alfa, S))
			S.remove(s)


pa = ["",""]
tam = 2;
def gerapermutacoescomtamanho(alfa,tt):
	if tt==0:
		print ''.join(pa)
	else:
		for x in xrange(0,len(alfa)):
			pa[tam-tt] = alfa[x]
			gerapermutacoescomtamanho(diferenca(alfa, pa),tt-1)
			pa[tam-tt] = ""

def diferenca(alfabet,gg):
	t = []
	for a in xrange(0,len(alfabet)):
		if alfabet[a] not in gg:
			t.append(alfabet[a])
	return t

gerapalavras(t)

print "---aqui eu termino essa geracao de palavras----"

gerapermutacoes(alfabeto)

print "---aqui eu termino as permutacoes em ordem crescente----"

gerapermutacoesultimo(alfabeto)

print "---aqui eu termino as permutacoes em ordem decrescente----"

gerapermutacoescomtamanho(alfabeto,tam)

print "---aqui eu termino as permutacoes com tamanho----"