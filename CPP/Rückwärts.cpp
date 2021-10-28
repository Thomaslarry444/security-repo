//Rückwärts 
# include <stdio.h>
# include <stdlib.h>
void Textrueck (char Text[], int charzaehler);
void Wortrueck (char Text[], int charzaehler, int WortAnf);

int main (void){
	char Text [50];
	int wortAnf;
	printf ("Geben Sie einen Text ein, der nicht mehr als 50 Zeichen enthaelt: \n");
	fgets(Text, 50, stdin);
	printf("%s", Text);
	
	for (int charzaehler=0;charzaehler<=49;charzaehler++){
		printf("%c",Text[charzaehler]);
		if(Text[charzaehler]=='\0')
		{
			Textrueck(Text,charzaehler);
			break;
		}
	}
	
	wortAnf=0;
	for (int charzaehler=0;charzaehler<=49;charzaehler++){
		if(Text[charzaehler]==' '){
			Wortrueck(Text,charzaehler,wortAnf);
			 if (wortAnf==0){
			 	printf(" ");
			 }
			wortAnf=charzaehler;
		}
		if (Text[charzaehler]=='\0'){
				Wortrueck(Text,charzaehler-1,wortAnf);
				//	printf("\n");
				break;	
			;		
		}
	
	}
	return 0;
	
}

void Textrueck (char Text[50], int charzaehler){
	for (int rueckzaehler=charzaehler-1;rueckzaehler>=0;rueckzaehler--){
		printf("%c", Text[rueckzaehler]);
	}
	printf("\n");
}

void Wortrueck (char Text[50], int charzaehler, int WortAnf){
	for (int rueckzaehler=charzaehler-1;rueckzaehler>=WortAnf;rueckzaehler--){
		printf("%c", Text[rueckzaehler]);
	}

}
