# include <stdio.h>
# include <cstdlib>
# include <time.h>
# include <stdlib.h>


int main (){
	srand (time(NULL));
	int position;
	int kartenspiel[52];
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
	position++;
	spielerkarte++;
	
}
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
