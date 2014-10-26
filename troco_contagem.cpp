#include <stdio.h>

int trocoContagem(int moedas[], int moedasSize, int valor) {
  if (valor == 0) {
    return 1;
  } else if (moedasSize == 0){
    return 0;
  } else {
    int moeda = moedas[moedasSize-1];
    int soma = 0;
    for(int i = 0; i <= valor/moeda; i++) {
      soma += trocoContagem(moedas, moedasSize-1, valor-moeda*i);
    }
    return soma;
  }
}

int main()
{
  int moedas[] = {9, 1};
  int troco = trocoContagem(moedas, 2, 10);
  printf("%d\n", troco);
  return 0;
}

