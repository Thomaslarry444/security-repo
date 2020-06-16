//Programm Zeiger.c
#include<stdio.h>

int main(){
	int var;
	int *ptr;
	var=121;
	ptr=&var;
	printf("%i\n",*ptr);
	printf("%i\n",ptr);
	return 0;
}
