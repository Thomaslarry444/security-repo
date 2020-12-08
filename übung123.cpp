#include <stdio.h >

int main (){
float Schulnoten[10],summe;
int anzahl=10, i;
	
for(int i=0; i<anzahl; i++){
	printf("\nBitte geben sie 10 Schulnoten ein : \n");
	scanf("%f", &Schulnoten[i]);	
} 

	
for(i=0; i<anzahl; i++){
	summe += Schulnoten [i];
}
	
printf("\n die summe ist %.2f\n", summe);
printf("\n der durchschnitt ist %.2f\n", summe /anzahl );
	
}
	
