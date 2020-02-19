//Einsedeaufgabe 3
#include <stdio.h>
#include <string.h>
int zeik_laeng (char*zkette);

int main (){
	char zeichenkette [17];
	int ergebnis;
	strcpy (zeichenkette, "Testzeichenkette");
	ergebnis=zeik_laeng (zeichenkette);
	printf("Anzahl der Zeichen %i",ergebnis);
	return 0;
}

int zeik_laeng (char*zkette){
	int n=0;
	for (int i=0;zkette[i]!='\0';i++){
		n=n+1;
	}
	return n;
	
}
