//Aufgabe 1.1
# include <stdio.h>
int main (){
	float zahl1, zahl2, *z_zeiger1, *z_zeiger2;
	zahl1=3;
	zahl2=4;
	z_zeiger1=&zahl1;
	z_zeiger2=&zahl2;
	printf("%f", (*z_zeiger1+*z_zeiger2));

return 0;
}
