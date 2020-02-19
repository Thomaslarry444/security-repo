//Aufgabe 2.3.3
#include <stdio.h>
#define Zeichen 5
void ersetze_zeichen(char*s,char zei_alt, char zei_neu);

int main (){
	char zeichenkette[]={'f','g','d','e','\0'};
	for (int x=0;zeichenkette[x]!='\0';x++)
		printf("Zeichen der Zeichenkette %c\n",zeichenkette[x]);
	
	ersetze_zeichen(zeichenkette,'f','a');
	
	for (int x=0;zeichenkette[x]!='\0';x++)
		printf("Zeichen der Zeichenkette %c\n",zeichenkette[x]);
		
		printf("getauschter Buchstabe %c",*zeichenkette);
	return 0;
	
}

void ersetze_zeichen(char*s,char zei_alt, char zei_neu){
	for (int x=0;s[x]!='\0';x++){
		if (s[x]==zei_alt){
			s[x]=zei_neu;
			
		}
			
		}
		
		
		
	}
