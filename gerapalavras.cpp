#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char alfGlob[] = "abc";
char *p;

void brutalPrint(char alf[]) {
	if (strlen(alfGlob) == strlen(p)) {
		printf("%s\n", p);
		return;
	}

	for(int i=0; i < strlen(alf); i++) {
		char l = alf[i];
		char cp[2];
		cp[0] = l;
		cp[1] = 0;
		strcat(p, cp);
		brutalPrint(alf);
		p[strlen(p)-1] = 0;
	}
}

int main()
{
	p = (char*) malloc(strlen(alfGlob)+1);
	memset(p, 0, strlen(alfGlob)+1);

	printf("Brutal Print\n");
	brutalPrint(alfGlob);

	free(p);
  return 0;
}
