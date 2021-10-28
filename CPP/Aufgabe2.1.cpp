//Ermitteln_Prozentwert
#include <stdio.h>
//test
float prozent(float ,float);
void ausgabe (float zahl);

int main (){
	float wert, pwert, psatz;
	
	printf("\nProzentwert eingeben: ");
	scanf("%f",&pwert);
	printf("\nGrundwert eingeben: ");
	scanf("%f,&wert");
	psatz=prozent(pwert,wert);
	printf("\n");
	
	ausgabe(psatz);
	
	return 0;

}
float prozent (float Prozentwert,float Grundwert){
	return Prozentwert/Grundwert*100;
}
void ausgabe(float prozentsatz){
	printf("\nProzentsatz: %.2f %%",prozentsatz);
}

