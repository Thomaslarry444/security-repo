//Einsendeaufgabe 2.3
#include <stdio.h>
int berechne (double *f, int n);

int main (){
	int n=8;
	double f [8]={1.1,1.3,1.7,10.9,11.6,4.9,2.3,1.54};
	int ergebnis;
	ergebnis=berechne(f,n);
	return 0;
	
}

int berechne (double *f, int n){
	double endergebnis,ergebnis1;
	ergebnis1=0;
	for (int i=0;i<n;i++){
		ergebnis1+=f[i];
		

	}
	endergebnis=ergebnis1/n;
	printf("Mittelwert\t%f",endergebnis);
	printf("Alle Zahlen >Mittelwert\n");
	for (int i=0;i<n;i++){
		if (f[i]>endergebnis){
			printf("%f\n",f[i]);
		}
	
		}
		return 0;
}

