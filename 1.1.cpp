//IM12 Aufgabe 1.2
#include <stdio.h>

int main (){
	float x,  y,  *zeigerx , *zeigery;
	x=3.4;
	y=7.2;
	zeigerx=&x;
	zeigery=&y;
	printf("%f",(*zeigerx+*zeigery));
	return 0;
	
}
