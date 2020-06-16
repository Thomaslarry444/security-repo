//4 gewinnt
# include <stdio.h>
void print_Spielfeldline (int Feld[][7],int reihe);
void print_Spielfeld (int Spielfeld[][7]);

int main(){
	int Spielfeld [7][7];
	int counter=0;
	int hoehe;
	bool gewonnen=false; 
	
	
	int Einwurfmoeglichkeit=1;
	for (int x=0;x!=7;x++){
		for (int y=0;y!=7;y++){
			Spielfeld[x][y]=0;
		}
	}

	while (gewonnen==false){
	print_Spielfeld(Spielfeld);
	printf ("Spieler1 Bitte einen Stein einwerfen");
	printf ("An welcher Postion willst du einwerfen"); 
	scanf("%i",&Einwurfmoeglichkeit);
	while (Einwurfmoeglichkeit>7 || Einwurfmoeglichkeit<=0){
		printf ("An welcher Postion willst du einwerfen"); 
		scanf("%i",&Einwurfmoeglichkeit);
		if (Einwurfmoeglichkeit>7 || Einwurfmoeglichkeit<=0)
				printf ("Eingabe nicht moeglich");
	}
	for (int z=0;z!=7;z++){
		if (Spielfeld[Einwurfmoeglichkeit][z]==0){
			Spielfeld[Einwurfmoeglichkeit][z]=1;
			hoehe=z;
			break;
		}
	}
	for (int reihe=0;reihe!=7;reihe++){
		if (Spielfeld[Einwurfmoeglichkeit][reihe]==1){
			counter++;
			if (counter==4){
				printf("Spieler 1 gewonnen");
				gewonnen=true;
				return 0;
			
			}
		}else{
			counter=0;
		} 
	}	
	for (int zsp=0;zsp!=7;zsp++){
		if (Spielfeld[zsp][hoehe]==1){
			counter++;
			if (counter==4){
				printf("Spieler 1 gewonnen");
				gewonnen=true;
				return 0;
			}
		}else{
			counter=0;
		} 
	}	
	
	
	print_Spielfeld(Spielfeld);	
	printf ("Spieler2 Bitte einen Stein einwerfen");
	printf ("An welcher Postion willst du einwerfen"); 
	scanf("%i",&Einwurfmoeglichkeit);
	while (Einwurfmoeglichkeit>7 || Einwurfmoeglichkeit<=0){
		printf ("An welcher Postion willst du einwerfen"); 
		scanf("%i",&Einwurfmoeglichkeit);
		if (Einwurfmoeglichkeit>7 || Einwurfmoeglichkeit<=0)
				printf ("Eingabe nicht moeglich");
	}
	for (int z=0;z!=7;z++){
		if (Spielfeld[Einwurfmoeglichkeit][z]==0){
			Spielfeld[Einwurfmoeglichkeit][z]=2;
			hoehe=z;
			break;
		}
	}	
		
	for (int reihe=0;reihe!=7;reihe++){
		if (Spielfeld[Einwurfmoeglichkeit][reihe]==2){
			counter++;
			if (counter==4){
				printf("Spieler 2 gewonnen");
				gewonnen=true;
				return 0;
			}
		}else{
			counter=0;
		} 
	}	
	for (int zsp=0;zsp!=7;zsp++){
		if (Spielfeld[zsp][hoehe]==2){
			counter++;
			if (counter==4){
				printf("Spieler 2 gewonnen");
				gewonnen=true;
				return 0;
			}
		}else{
			counter=0;
		} 
	}
	}
}
void print_Spielfeldline (int Feld[][7],int reihe){
	char hline=179;
	for(int counter=0; counter!=7;counter++){
		printf("counter:  %d",counter);
		if (Feld[counter][reihe]==0){
			printf("  ");
		}
		else if (Feld[counter][reihe]==1){
			printf("X ");	
		}
		else if (Feld[counter][reihe]==2){
			printf("O ");
		}	
		if (counter==6){
			printf("%c",hline);
		}
	}
	printf("\n");
}	
void print_Spielfeld (int Spielfeld[][7]){
	char hline=179, vline=196, kreuz=197,anfli=195, leer=' ', Spieler1='X',Spieler2='O';
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	print_Spielfeldline(Spielfeld, 6);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
    print_Spielfeldline(Spielfeld, 5);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	print_Spielfeldline(Spielfeld, 4);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	print_Spielfeldline(Spielfeld, 3);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	print_Spielfeldline(Spielfeld, 2);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	print_Spielfeldline(Spielfeld, 1);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	print_Spielfeldline(Spielfeld, 0);
	printf ("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n",anfli,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz,vline,vline,vline,kreuz);
	printf ("\n");	
}

