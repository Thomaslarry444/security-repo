//Quadratzahlen_11-25
#include<stdio.h>
int main() {
	int quadra,ergebnis;
	quadra=11;
	
	while (quadra<=25){
		ergebnis=quadra*quadra;
		printf("Das Quadrat von %d ist %d\n",quadra,ergebnis);
		quadra=quadra+1;
		
	}
	return 0;
}
