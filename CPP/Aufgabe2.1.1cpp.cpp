<<<<<<< HEAD
//Aufgabe2.1
#include <stdio.h>
float prozent (float wert,float prozentwert);
void ausgabe (float ergebnis);

int main(){
	float wert=1000;
	float prozentwert=1500;
	float ergebnis;
	ergebnis=prozent (wert,prozentwert);
	ausgabe (ergebnis);
	
	return 0;
}

float prozent (float wert,float prozentwert){
	int ergebnis=prozentwert/wert*100;
	return ergebnis;
}
void ausgabe (float ergebnis){
	printf("Prozentsatz: %f",ergebnis);
}
	
=======
//Aufgabe2.1
#include <stdio.h>
float prozent (float wert,float prozentwert);
void ausgabe (float ergebnis);

int main(){
	float wert=1000;
	float prozentwert=1500;
	float ergebnis;
	ergebnis=prozent (wert,prozentwert);
	ausgabe (ergebnis);
	
	return 0;
}

float prozent (float wert,float prozentwert){
	int ergebnis=prozentwert/wert*100;
	return ergebnis;
}
void ausgabe (float ergebnis){
	printf("Prozentsatz: %f",ergebnis);
}
	
>>>>>>> 33a1bf1eb8ce5cf1ea81e18a0ffe1092ed551610
