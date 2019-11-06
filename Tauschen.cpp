//Programm Tauschen.c
#include<stdio.h>
void swap (int x, int y);

int main(){
	int zahl1=10,zahl2=20;
	printf("Werte vor Aufruf von swap:\n");
	printf("zahl1: %d, zahl2: %d\n,zahl1,zahl2");
	swap (zahl1,zahl2);
	printf("Werte nach Aufruf von swap:\n");
	printf("zahl1: %d, zahl2: %d\n",zahl1,zahl2);
	
	return 0;
}

void swap (int x,int y){
	int hilf;
	hilf=x;
	x=y;
	y=hilf;
}	
