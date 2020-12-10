# include <stdio.h>
# include <cstdlib>
# include <time.h>
# include <stdlib.h>


int main (){
	srand (time(NULL));
	int position;
	int kartenspiel[52];
	char eingabe;
	int kartensumme=0;
	for(int i=0;i<52;i++){
		kartenspiel[i]=0;
	}
	
	
	for (int farbe=0; farbe<4 ; farbe++){
		for(int kartenwert=0; kartenwert<13; kartenwert++){
			do{
				position = rand() % 52;	
			}
			while(kartenspiel[position]!=0);
			
			if (kartenwert<=8){
				kartenspiel[position]=kartenwert+2;
			}
			if(kartenwert>8 && kartenwert<12){
				kartenspiel[position]=10;
			}
			if(kartenwert==12){
				kartenspiel[position]=11;
			}	
		}
	}
	//for(int i=0;i<52;i++){
		//printf("%d\n", kartenspiel[i]);
	//}

int spielerkarte=0;
int Spieler[12];
for(int kartenzug=0; kartenzug<2; kartenzug++){
	Spieler[spielerkarte] = kartenspiel[position];
	kartenspiel[position]=0;
	printf("Spielerkarten %d\n", Spieler[spielerkarte]);
		// kartensumme=kartensumme+Spieler[spielerkarte];
	//printf("Momentane Kartenhoehe:  %d\n",kartensumme);
	position++;
	spielerkarte++;
;
}
	//for (int spielersumme=0; spielersumme<2;spielersumme++){
		//kartensumme+=Spieler[spielerkarte];
		//printf("Momentane Kartenhoehe:  %i\n",kartensumme);
//	}

	

int bankkarte=0;
int Bank[12];
for(int kartenzug=0; kartenzug<2; kartenzug++){
	Bank[bankkarte]= kartenspiel[position];
	kartenspiel[position]=0;
	printf("Bankkarten %d\n ", Bank[bankkarte]);
	position++;
	bankkarte++;
}
}
//printf("Wollen Sie noch eine Karte Spieler (y/n)\n");
//scanf("%c",&eingabe);
//if('y'==eingabe){
	//Spieler[spielerkarte]=kartenspiel[position];
	//kartensumme=kartensumme+Spieler[spielerkarte];
	//for(int zaehlen=0; zaehlen<3; zaehlen++){
		//kartensumme+=Spieler[spielerkarte];
	//printf("Die momentane Summe der Karten betraegt: %d\n",kartensumme);

	
	


