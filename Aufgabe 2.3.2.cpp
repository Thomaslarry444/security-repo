//Aufgabe 2.3.2
#include <stdio.h>
#define ANZ 6 

float vsumme (float *,int);

int main (){
	float ergebnis;
   	float Allezahlen [6]={1.1f,1.6f,4.5f,4.6f,7.8f,9.2f};
   	ergebnis=vsumme(Allezahlen,ANZ);
	printf("Das ist das Ergebnis  %f",ergebnis);
	
	return 0;
	
}



float vsumme (float  *elemente,int Anzahl){
	float ergebnis=0;
	for (int x=0;x<Anzahl;x++){
		ergebnis+=elemente[x];
}
	return ergebnis;
	
	

}

