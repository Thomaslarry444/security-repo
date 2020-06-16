//Programm Zeigervergleich.c
#include <stdio.h>
int main (){
	int index;
	int *zeig_index=&index;
	int *zeig_wert=NULL;
	if (zeig_index != zeig_wert)zeig_wert=zeig_index;
	*zeig_index=15;
}
