# Parte 2 - Montagem de festas
# Trabalho - Estruturas Discretas - 26/10/2014
# Desenvolvido por:
# Alexandre Werneck
# Hugo Roque 

# Funcao comunidade    - chamada apos a leitura do arquivo
# Entrada              - O arquivo 'festa.txt' contendo as combinacoes possiveis
# Saida                - O conjunto encontrado

def comunidade(fest):
	combinacoes = montaCombinacoes(fest);

	#tamanho - recebido no primeiro parametro do array da festa
	tamanho = fest[0];

    #conjgenerico - neste loop e montado um conjunto contendo as chaves de cada elemento: Ex:[1,2,3]
	conjgenerico = []
	for x in xrange(0,tamanho):
		conjgenerico.append(x+1)

	for x in xrange(0, tamanho):
		subconjuntos   = []
		montaSubConjuntos(subconjuntos, conjgenerico, tamanho - x);
		for y in xrange(0,len(subconjuntos)):
			tpRet = verificaCombinacoes(combinacoes, subconjuntos[y])
			if tpRet != 0:
				retornoConjunto = montaResultado(tpRet)
				return retornoConjunto

# Funcao montaCombinacoes - Esta funcao monta todas combinacoes 2 a 2 possiveis a partir dos relacionamento #                           existentes.
#							Ex: [3,[2],[1,3],[1]] - Saida: [[1,2],[2,1],[2,3],[3,1]]
# Entrada                 - O array ja montado
# Saida                   - O conjunto de combinacoes
def montaCombinacoes(fest):
	b = []
	for x in xrange(1,len(fest)):		
		for y in xrange(0,len(fest[x])):
			a = [x,fest[x][y]]		
			b.append(a)
	return b

# Funcao montaCombSimples - Esta funcao cria novas combinacoes a partir de um subconjunto fornecido
#							Ex: [2,3,4] - Saida: [[2,3],[2,4],[3,2],[3,4],[4,2],[4,3]]
# Entrada                 - O array ja montado
# Saida                   - O conjunto de combinacoes
def montaCombSimples(fest):
	b = []
	for x in xrange(0,len(fest)):		
		for y in xrange(0,len(fest)):
			if x != y:
				a = [fest[x],fest[y]]	
				b.append(a)
	return b

# Funcao montaSubConjuntos - Esta funcao monta todos os subconjuntos de tamanho n
#							Ex: Tamanho 3 com [1,2,3,4] - Saida: [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
#							Ex: Tamanho 4 com [1,2,3,4] - Saida: [[1,2,3,4]]
def montaSubConjuntos(c, conjgenerico, tamanho):
	if len(conjgenerico) == tamanho:
		if conjgenerico not in c:
			c.append(conjgenerico)		
	else:
		for x in xrange(0, len(conjgenerico)):
			tmp = conjgenerico[:]
			tmp.remove(conjgenerico[x])
			montaSubConjuntos(c, tmp, tamanho)

# Funcao verificaCombinacoes - Esta funcao cria novas combinacoes a partir do conjunto fornecido em subc
#							   e verifica se algum destes conjuntos possui em todas as combinacoes uma 
#                              ocorrencia no parametro comb, se sim OK, foi encontrado o conjunto buscado, do #                              contrario continua procurando
# Entrada                 - comb = contem todas combinacoes + subc = combinacoes dado tamanho especifico
# Saida                   - 0 = nao encontrado | combLocal = array contendo os elementos a serem selecionados
def verificaCombinacoes(comb, subc):
	combLocal = montaCombSimples(subc)	
	for y in xrange(0,len(combLocal)):
		if combLocal[y] not in comb:
			return 0
	return combLocal

# Funcao montaResultado  - Esta funcao monta o conjunto solucao a partir do conjunto das solucoes encontradas
#							Ex: [[1,2],[2,1]] = [1,2]
# Entrada                 - comb = contem as combinacoes que contem o conjunto que sera resposta
# Saida                   - [1,2] = conjunto solucao

def montaResultado(comb):
	ret = []
	for x in xrange(0,len(comb)):
		for y in xrange(0,len(comb[x])):
			if comb[x][y] not in ret:
				ret.append(comb[x][y])
	return ret


# MAIN - Aqui acontece a leitura do arquivo e montagem do array para execucao do programa

f = open("festa.txt","r")
festa = []
festa.append(int(f.readline()))
for line in f:
	linha = line.split(',')
	a = []
	for x in xrange(0,len(linha)):
		a.append(int(linha[x]))
	festa.append(a)
f.close();


# Chamada para o programa principal 
result = comunidade(festa)

# Escreve o resultado do array montado no arquivo de retorno
f = open('saida2.txt', 'w+')
conjResposta = '{'
divider      = ','
for x in xrange(0,len(result)):
	if x == (len(result) - 1):
		divider = ''
	conjResposta += str(result[x]) + divider
conjResposta += '}'
f.write(conjResposta)
f.close()
