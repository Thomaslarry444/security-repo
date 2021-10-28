#include <stdio.h >

int main ()
{
	int zahl_1;
	int zahl_2;
	
	
	scanf("%d + %d", &zahl_1, &zahl_2);
	int ergebnis=zahl_1+zahl_2;
		if (ergebnis>=12)
	{
		printf("Super es ist größer");
	}
	else
	{
		printf("schlecht es ist kleiner");
	}
	return 0;	
}
