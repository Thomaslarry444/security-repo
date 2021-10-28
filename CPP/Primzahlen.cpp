// Programm Primzahlen.c
#include <stdio.h>
#define N 100
int main(){
	int i, j, a[N+1];
	
	a[1] = 0;
	for (i = 2; i<= N; i++) a[i] = 1;
	
	for (i = 1; i <= N; i++)
    	if (a[i]) printf ("%d ", i);
	
	for (i = 2; i <= N/2; i++)
		for (j = 2; j <= N/i; j++)
			a[i*j] = 0;
			
	printf("\n\nBerechn. der Primzahlen < 100:\n");
	for (i = 1; i <= N; i++)
		if (a[i]) printf ("\n%d", i);
	printf ("\nEnde des Programms\n");

	return 0;
}
