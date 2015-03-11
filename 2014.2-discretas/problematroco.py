
moedas = [5,3,1]
soma = 0
valorfinal = 13
n = 3

def probtroco(inic, valortotal):
	if inic == n:
		if (valortotal % moedas[n-1]) == 0:
			return 1
		else:
			return 0
	else:
		soma = 0
		for x in xrange(0,valortotal / moedas[inic-1]):
			soma = soma + probtroco(inic + 1, valortotal - (x * moedas[inic]))
		return soma

total = probtroco(1,valorfinal)
print total