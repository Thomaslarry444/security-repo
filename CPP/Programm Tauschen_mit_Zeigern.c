//Programm Tauschen_mit_Zeigern.c
//Parameterübergabe mit call by reference
#include <stdio.h>
void swap (int *a,int *b);

int main(){
	int zahl1,zahl2;
	zahl1=10;
	zahl2=20;
	printf("\nAusganswerte: %2i\t%2i",zahl1,zahl2);
	swap (&zahl1,&zahl2);
	printf("\nErgeniswerte: %2i\t%2i",zahl1,zahl2);
	return 0;
	
}
void swap (int *a,int *b){
	int vhilf;
	vhilf=*a;
	*a=*b;
	*b=vhilf;
}	
