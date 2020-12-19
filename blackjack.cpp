#include <stdio.h>
#include <cstdlib>
#include <time.h>
#include <stdlib.h>

int getKartensumme(int kartenanzahl, int *Karten);
void getKartenzug(int* position, int* spielerkarte,int* Kartenspiel, int* Spieler, int Kartenanzahl);

int main()
{
	srand(time(NULL));
	int position;
	int kartenspiel[52];
	char eingabe;
	int kartensumme = 0;
	int spielerkarte = 0;
	int Spieler[12];
	int bankkarte = 0;
	int Bank[12];
	for (int i = 0; i < 52; i++)
	{
		kartenspiel[i] = 0;
	}

	for (int farbe = 0; farbe < 4; farbe++)
	{
		for (int kartenwert = 0; kartenwert < 13; kartenwert++)
		{
			do
			{
				position = rand() % 52;
			} while (kartenspiel[position] != 0);

			if (kartenwert <= 8)
			{
				kartenspiel[position] = kartenwert + 2;
			}
			if (kartenwert > 8 && kartenwert < 12)
			{
				kartenspiel[position] = 10;
			}
			if (kartenwert == 12)
			{
				kartenspiel[position] = 11;
			}
		}
	}
	//for(int i=0;i<52;i++){
	//printf("%d\n", kartenspiel[i]);
	//}

	printf("Spieler 1 ist am Zug.\n");
	getKartenzug(&position,&spielerkarte,kartenspiel,Spieler,2);
	/*
	for (int kartenzug = 0; kartenzug < 2; kartenzug++) // Kartenzug könnte auch in eine funktion.
	{
		Spieler[spielerkarte] = kartenspiel[position];
		kartenspiel[position] = 0;
		printf("Der Spieler zieht die Karte %d\n", Spieler[spielerkarte]);
		position++;
		spielerkarte++;
	}
	*/
	kartensumme = getKartensumme(spielerkarte, Spieler);
	printf("Kartensumme Spieler:  %i\n\n", kartensumme);

	printf("Die Bank ist am Zug.\n");
	getKartenzug(&position,&bankkarte,kartenspiel,Bank,2);
	/*
	for (int kartenzug = 0; kartenzug < 2; kartenzug++)
	{
		Bank[bankkarte] = kartenspiel[position];
		kartenspiel[position] = 0;
		printf("Die Bank zieht die Karte %d\n", Bank[bankkarte]);
		position++;
		bankkarte++;
	}
	*/
	kartensumme = getKartensumme(bankkarte, Bank);
	printf("Kartensumme Bank:  %i\n", kartensumme);

	printf("Noch eine Karte Spieler? (y/n) ");	// dieser Teil sollte in eine Schleife
	scanf("%c", &eingabe);
	if (eingabe == 'y')
	{
		Spieler[spielerkarte] = kartenspiel[position];
		kartenspiel[position] = 0;
		printf("\nDer Spieler zieht die Karte %d\n", Spieler[spielerkarte]);
		position++;
		spielerkarte++;
		kartensumme = getKartensumme(spielerkarte, Spieler);
		printf("Die momentane Summe der Karten betraegt: %d\n", kartensumme);
	}
	else
	{
		printf("Keine weiteren karten fuer den Spieler\n");
		printf("Die momentane Summe der Karten betraegt: %d\n", kartensumme);
	}
}

int getKartensumme(int kartenanzahl, int *Karten)
{
	int kartensumme = 0;
	for (int kartennummer = 0; kartennummer < kartenanzahl; kartennummer++)
	{
		kartensumme += Karten[kartennummer];
	}
	if (kartensumme == 21)
	{
		printf("Sie haben gewonnen\n");
	}
	else if (kartensumme > 21)
	{
		printf("Sie haben verloren\n");
	}

	return kartensumme;
}
void getKartenzug(int* position, int* spielerkarte,int* Kartenspiel, int* Spieler,int Kartenanzahl)
{
	for (int kartenzug = 0; kartenzug < Kartenanzahl; kartenzug++) // Kartenzug könnte auch in eine funktion.
	{
		Spieler[*spielerkarte] = Kartenspiel[*position];
		Kartenspiel[*position] = 0;
		printf("Der Spieler zieht die Karte %d\n",Spieler[*spielerkarte]);
		*position++;
		*spielerkarte++;
	}
}
