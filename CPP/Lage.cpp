//PunktimQuadranten
#include<stdio.h>
int main () {
	float x, y;
	int Lage;
	printf("Bitte x: "); scanf("%f", &x);
	printf("Bitte y: "); scanf("%f", &y);
	
	if( x==0 ) 
		if (y==0) 
			Lage=0;
		else
			Lage=-1;
			
	else
		if (y==0)
			Lage=-2;
		else 
			if (y>0)
				if (x>0)
					Lage=1;
				else
					Lage=2;
			else 
				if (x<0)
					Lage=3;
				else
					Lage=4;
	
	switch(Lage) {
		case 0: printf("Nullpunkt");break;
		case -1: printf("auf x-Achse");break;
		case -2: printf("auf y-Achse");break;
		case 1: printf ("im 1.Quadranten");break;
		case 2: printf ("im 2.Quadranten");break;
		case 3: printf ("im 3.Quadranten");break;
		case 4: printf ("im 1.Quadranten");break;
	}
}
