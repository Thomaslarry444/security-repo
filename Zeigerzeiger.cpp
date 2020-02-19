//Programm Zeiger_auf_Zeiger_Zeiger.c
#include<stdio.h>

int main(){
	int var;
	int *ptr;
	int **pptr;
	var=121;
	ptr=&var;
	pptr=&ptr;
	printf("%i\n, **pptr");
	return 0;
}
