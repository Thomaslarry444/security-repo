//Programm Fakultaet_2.c
#include <stdio.h>
long fakul (int zahl);

int main(){
	int wert;
	printf("\nFakultaetsrechnung fuer den Wert");
	scanf("%d",&wert);
	printf("\nErgebnis: %d! = %d",wert,fakul(wert));
return 0;
}
long fakul(int zahl){
	long ergeb;
	if (zahl>0)printf("zahl=d%:\t%d*fakul (%d)\n,zahl,zahl,zahl-1");
	if (zahl>0){
		ergeb=zahl*fakul(zahl-1);
	}
	else 
      ergeb=1;
      printf("Ergebnisrueckgabe fuer zahl=%d: %d\n",zahl,ergeb);
    return(ergeb);
}
