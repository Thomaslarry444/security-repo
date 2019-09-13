//Programm Spahrjahre.c
#include<stdio.h>
int main() 
{
float zins, anf, end, guthaben;
int jahre;
printf("\n");
printf("\n Berechnung der Sparjahre \n");
printf(" Geben Sie das Anfangskapital ein: \t");
scanf ("%f",&anf);
printf(" Geben Sie den aktuellen Zinssatz ein: \t");
scanf ("%f",&zins);
end = 2 * anf;
printf("\n");
guthaben = anf;
jahre = 0;
while(guthaben < end)
{
	guthaben = guthaben + guthaben * zins;
	jahre = jahre + 1;
}
    printf("Nach %d Jahren ist das Sparziel erreicht.", jahre);
    printf("\n");
return 0;
}

