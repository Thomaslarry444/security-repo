//Aufgabe2.3 
#include <stdio.h>
void sign (int *zeiger_zahl,int*zeiger_rueckgabe);

int main(){
	int zahl;
	int *zeiger_zahl,*zeiger_rueckgabe;
	zeiger_zahl=&zahl;
	int rueckgabe;
	zeiger_rueckgabe=&rueckgabe;
	int was1=0,wasminus1=0;
	do{
	printf("Geben Sie eine Zahl ein: \t");
	scanf("%i",zeiger_zahl);
	sign(zeiger_zahl,zeiger_rueckgabe);
	printf("der Rueckgabewert lautet: \t%i",*zeiger_rueckgabe);
	if (rueckgabe==-1)
		wasminus1=1;
	if (rueckgabe==1)
		was1=1;
}while(wasminus1!=1||was1!=1);
	
	return 0;
	
}

void sign (int *zeiger_zahl,int*zeiger_rueckgabe){
	int rueckgabewert;
	if (*zeiger_zahl<0)
		*zeiger_rueckgabe=-1;
	if (*zeiger_zahl>0)
		*zeiger_rueckgabe=1;
	
}

