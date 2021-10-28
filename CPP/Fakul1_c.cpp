//Programm Fakultaet_1.c
#include <stdio.h>
long fakul (int zahl);

int main(){
	int wert;
	printf("\nFakultaetsrechnung für den Wert");
	scanf("%d",&wert);
	printf("\nErgebnis: %d! = %d",wert,fakul(wert));
return 0;
}

long fakul(int zahl){
	long ergeb;
	if(zahl>0)
	 ergeb=zahl*fakul(zahl-1);
	else
	  ergeb=1;
	return(ergeb);
	
}
