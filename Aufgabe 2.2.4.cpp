//Aufgabe 2.4
#include <stdio.h>
#include <math.h>

float arctan(int x);
float potenz (int x, int hochx);

int main(){
	int x;
	float ergebnis;
	printf("x= ");
	scanf("%i",&x);
	ergebnis=arctan(x);
	printf("ergebnis %f",ergebnis);
	ergebnis=atan(x);
	printf("ergebnis der Mathefunktion: %f",ergebnis);
	
	return 0; 
	
}

float arctan(int x){
	int hochx=3;
	int plus=1;
	float ergebnis;
	ergebnis=x-potenz(x, hochx)/hochx;
	hochx=hochx+2;
	for (int i=0;i<10000;i++){
		if (plus==1){
			ergebnis=ergebnis+potenz(x,hochx)/hochx;
			plus=0;
		}
		else {
		   ergebnis=ergebnis-potenz(x,hochx)/hochx;
		   plus=1;
		}	
		hochx=hochx+2;
	
	
		
	}
	
	return ergebnis;
}

float potenz (int x, int hochx){
	while (hochx!=1){
		x=x*x;
		hochx=hochx-1;
	}
	return x; 
}

