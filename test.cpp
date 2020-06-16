//Programm Funktionszeiger.c
#include <stdio.h>

 int berech(int wert,int(*fzeiger)(int wert));
 int funk1(int x);
 int funk2(int x);

int main (){
int i=2;
 printf("\nFunktion1 benutzt: %i",berech(i,funk1));
 printf("\nFunktion2 benutzt: %i",berech(i,funk2));
 }

 int berech(int wert, int(*fzeiger)(int wert)){
 return(2*wert+(*fzeiger)(wert));
 }

 int funk1(int x){
 return(x*x+10);
}

int funk2(int x){
	return (5*x+50);
}

