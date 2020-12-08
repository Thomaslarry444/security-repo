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
	for(int i=0;i<52;i++){
		printf("%d\n", kartenspiel[i]);
	}

}
