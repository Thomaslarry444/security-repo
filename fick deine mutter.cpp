//mehr mathe 
#include <stdio.h>
#include <math.h>
int main(){
	float a,ergebnis,eps;
	eps=0.0000005;
	printf("Bitte einen Wert eingeben\t");
	scanf("%f",&a);
	
	ergebnis=(a+1)/2;
	
	//printf("Genau: %f", fabs(ergebnis*ergebnis-a));
	//printf("Ergebnis: %f", ergebnis);
	
	while( fabs(ergebnis*ergebnis-a) > eps ){
		ergebnis=0.5*(ergebnis+a/ergebnis);
		printf("Wurzel aus %f ist %f \n",a,ergebnis);
	}
	return 0;
}
