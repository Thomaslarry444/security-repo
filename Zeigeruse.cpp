//Programm Zeigernutzung.c
#include <stdio.h>
int main (){
	int int_z1, int_z2, *zeig_int;
	char bu_1, bu_2, *zeig_bu;
	int_z1=1;
	int_z2=-2;
	bu_1='c';
	
	zeig_int=&int_z2;
	int_z2+=*zeig_int+1;
	printf("%i\n",zeig_int);
	zeig_bu=&bu_1;
	bu_2=*zeig_bu;
	printf("%c\n",bu_2);
	
	*zeig_int=*zeig_int+int_z1;
	printf("%i\n",*zeig_int);
	int_z2=int_z1* *zeig_int;
	printf("&i\n", int_z2);
	 (*zeig_int)++;
	 printf("%i\n",zeig_int);
	 
	 return 0;
}
