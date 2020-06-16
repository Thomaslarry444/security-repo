//Aufgabe 2.3.4
#include <stdio.h>

void zeik_verbind(const char*,const char*,char*);

int main(){
	char Ergebnis[10];
	char Programm[]={'t','h','c','\0'};
	char Entwicklung[]={'X','T','C','\0'};
	zeik_verbind(Programm,Entwicklung,Ergebnis);
	printf("Programm und Entwicklung ");
	for (int x=0;Ergebnis[x]!='\0';x++)
		printf(" %c",Ergebnis[x]);
	return 0;
	
	
}

void zeik_verbind(const char*P,const char*E,char*ergebnis){
	int lauf=0;
	for (int x=0;P[x]!='\0';x++){
		ergebnis[x]=P[x];
		lauf++;
	}
		
	for (int x=0;E[x]!='\0';x++){
		ergebnis[lauf]=E[x];
		lauf++;
	}
	
	
		
		
		
	
}
