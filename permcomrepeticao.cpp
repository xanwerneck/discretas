#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printPermutacaoComRepeticaoRecursao(const char alf[], char *alfUsed,
    char *word, int wordSize) {
  if (wordSize == strlen(alf)) {
    printf("%s\n", word);
  } else {
    for(int i=0; i < strlen(alf); i++) {
      if (!alfUsed[i]) {
        int nextLetterI = strlen(word);
        alfUsed[i] = 1;
        word[nextLetterI] = alf[i];
        printPermutacaoComRepeticaoRecursao(alf, alfUsed, word, wordSize+1);
        word[nextLetterI] = 0;
        alfUsed[i] = 0;
      }
    }
  }
}

void alfWithoutRepetitions(const char alf[], char *newAlf) {
  char alreadyInNewAlf[256];
  memset(alreadyInNewAlf, 0, 256);
  int originalLength = strlen(alf);
  int newLength = 0;
  for(int i=0; i<originalLength; i++) {
    if (!alreadyInNewAlf[alf[i]]) {
      newAlf[newLength++] = alf[i];
      alreadyInNewAlf[alf[i]] = 1;
    }
  }
}

void printPermutacaoComRepeticao(const char alf[]) {
  char *word = (char*) malloc(strlen(alf)+1);
  char *alfUsed = (char*) malloc(strlen(alf)+1);
  memset(word, 0, strlen(alf)+1);
  memset(alfUsed, 0, strlen(alf)+1);
  printPermutacaoComRepeticaoRecursao(alf, alfUsed, word, 0);
  free(word);
  free(alfUsed);
}

int main()
{
  printf("Permutação com Repetição\n");
  printPermutacaoComRepeticao("aabc");
  return 0;
}

