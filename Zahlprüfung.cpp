//Aufgabe2.3 
#include <stdio.h>
int sign (int zahl);

int main(){
	int zahl;
	int rueckgabe;
	int was1=0,wasminus1=0;
	do{
	printf("Geben Sie eine Zahl ein: \t");
	scanf("%i",&zahl);
	rueckgabe=sign(zahl);
	printf("der Rueckgabewert lautet: \t%i",rueckgabe);
	if (rueckgabe==-1)
		wasminus1=1;
	if (rueckgabe==1)
		was1=1;
}while(wasminus1!=1||was1!=1);
	
	return 0;
	
}

int sign (int zahl){
	int rueckgabewert;
	if (zahl<0)
		rueckgabewert=-1;
	if (zahl>0)
		rueckgabewert=1;
	return rueckgabewert;
}

