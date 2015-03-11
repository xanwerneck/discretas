#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char alfGlob[] = "abc";
int *used;
char *p;

void permutePrint(char alf[]) {
	if (strlen(alfGlob) == strlen(p)) {
		printf("%s\n", p);
		return;
	}

	for(int i=0; i < strlen(alf); i++) {
		if (used[i]) continue;
		char l = alf[i];
		used[i] = 1;
		char cp[2];
		cp[0] = l;
		cp[1] = 0;
		strcat(p, cp);
		permutePrint(alf);
		p[strlen(p)-1] = 0;
		used[i] = 0;
	}
}

int main()
{
	used = (int*) malloc(4*(strlen(alfGlob)+1));
	p = (char*) malloc(strlen(alfGlob)+1);
	memset(p, 0, strlen(alfGlob)+1);
	memset(used, 0, 4*(strlen(alfGlob)+1));
	printf("Permute Print\n");
	permutePrint(alfGlob);
	free(p);
	free(used);
  return 0;
}
