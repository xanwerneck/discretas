# Parte 1 - Montagem de anagramas
# Trabalho - Estruturas Discretas - 26/10/2014
# Desenvolvido por:
# Alexandre Werneck
# Hugo Roque 

# Funcao anagrama      - Recebe uma variavel como parametro para escrita de cada palavra gerada
#                        Recebe um array para montagem dos anagramas
#                        Monta todas as palavras
#                        Escreve cada uma na variavel recebida
# Entrada              - O variavel global para escrita - arRetorno
# Saida                - A variavel acrescida das palavras geradas

def anagrama(retorno, alf):
	if len(alf)==0:
		pal = ''.join(p)
		retorno.append(pal)
	else:
		T = distintos(alf)
		for x in xrange(0,len(T)):
			s = T[x]
			p[n - len(alf)] = s
			if (n - len(alf)) == 0:
				anagrama(retorno, diferenca(alf,s))
			else:
				if p[n-len(alf)] != p[(n-len(alf))-1]:
					anagrama(retorno, diferenca(alf,s))


# Funcao distintos      - Funcao que seleciona os elementos distintos
#						Ex: ["a","b","a"] = Retorna novo array com ["a","b"]
# Entrada              - O array contendo todos os alementos
# Saida                - Novo array eliminando as repeticoes

def distintos(alf):
	a = []
	for x in xrange(0,len(alf)):
		if alf[x] not in a:
			a.append(alf[x])
	return a

# Funcao diferenca     - Funcao elimina o elemento ja utilizado
#						Ex: ["a","b","c"] = Retorna novo array com ["b","c"]
# Entrada              - O array contendo todos os alementos
# Saida                - Novo array eliminando o ja utilizado

def diferenca(alfabet,gg):
	t = []
	s = alfabet[:]
	s.remove(gg)
	if len(s)==0:
		return t
	for a in xrange(0,len(s)):
		t.append(s[a])
	return t

# MAIN - Aqui acontece a leitura do arquivo e montagem do array para execucao do programa
f = open("anagramas.txt","r")
anagramas = []
for line in f:
	linha = list(line.strip())
	anagramas.append(linha)
f.close();

# Array para montagem do arquivo de retorno
arRetorno = []

# Chamada do programa para cada ocorrencia do array
for x in xrange(0,len(anagramas)):
	n = len(anagramas[x])
	p = []
	for y in xrange(0,n):
		p.append("")
	anagrama(arRetorno, anagramas[x])	

# Escreve o resultado do array montado no arquivo de retorno
f = open('saida.txt', 'w+')
for x in xrange(0,len(arRetorno)):
	f.write(arRetorno[x] + '\n')
f.close()

