#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printGroupsRec(char alf[], int r, char *w, int alfIni, int wSize) {
	if (r == 0) {
		printf("%s\n", w);
	} else {
		int n = strlen(alf);
		for(int i=alfIni; i <= (n-r); i++) {
			w[wSize - r] = alf[i];
			printGroupsRec(alf, r-1, w, 1+i, wSize);
		}
	}
}

void printGroups(char alf[], int r) {
	char *w = (char*) malloc(r+1);
	memset(w, 0, r+1);
	printGroupsRec(alf, r, w, 0, r);
	free(w);
}

int main()
{
	printGroups("abcde", 3);
}
