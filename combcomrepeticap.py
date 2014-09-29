alfabeto = ["c","a","s","a"]
P = ["","","",""]
tam = len(P)

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
    t = alfabeto
    for a in xrange(0,len(alfabet)):
        if alfabet[a] == gg:
            t.remove(alfabet[a])
            return t
    return t

def distintos(alfabet):
    t = []
    for a in xrange(0,len(alfabet)):
        if alfabet[a] not in t:
            t.append(alfabet[a])
    return t



combcomrep(alfabeto)