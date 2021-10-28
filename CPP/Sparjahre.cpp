//Programm Spahrjahre.c
#include<stdio.h>
#include<conio.h>
int main() 
{
	float zins, anf, end, guthaben;
	int jahre;
	char input='j';
	while (input!='n')
	{
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
		printf("Moechten Sie die Rechnung wiederholen?(j)a/ (n)ein\n");
		//scanf (" %c",&input);
		input=getch();
	}
return 0;
}

