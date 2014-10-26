#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void trocoEnumeracaoRecursivo(int moedas[], int moedasSize, int valor, int *quantidadeMoedas, int moedasOriginalSize) {
  if (valor == 0) {
    for(int i = 0; i < moedasOriginalSize; i++) {
      if (quantidadeMoedas[i]) {
        printf("%d moeda(s) de %d, ", quantidadeMoedas[i], moedas[i]);
      }
    }
    printf("\n");
  } else if (moedasSize > 0) {
    int moeda = moedas[moedasSize-1];
    for(int i = 0; i <= valor/moeda; i++) {
      *(quantidadeMoedas+moedasSize-1) += i;
      trocoEnumeracaoRecursivo(moedas, moedasSize-1, valor-moeda*i, quantidadeMoedas, moedasOriginalSize);
      *(quantidadeMoedas+moedasSize-1) -= i;
    }
  }
}

void trocoEnumeracao(int moedas[], int moedasSize, int valor) {
  int *quantidadeMoedas = (int*) malloc(moedasSize*4);
  memset(quantidadeMoedas, 0, moedasSize*4);
  trocoEnumeracaoRecursivo(moedas, moedasSize, valor, quantidadeMoedas, moedasSize);
  free(quantidadeMoedas);
}

int main()
{
  int moedas[] = {9, 1};
  trocoEnumeracao(moedas, 2, 10);
  return 0;
}

