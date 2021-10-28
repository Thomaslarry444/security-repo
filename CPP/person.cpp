#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct person* neue_node(struct person *anfang,char Vorname [],char Nachname [],int Punkte);
void ausgabe (struct person* anfang);
int anzahl_Person(struct person* anfang);
struct person* neuer_anfang(struct person* anfang,char* Vorname,char* Nachname,int Punkte);

struct person{
	char Vorname [20];
	char Nachname [20];
	int Punkte;
	struct person *next;
};

int main (){
	//printf("Geben Sie den Vornamen ein");
	//scanf()
	struct person *anfang=NULL;
	
	anfang=neue_node(anfang,"Harri","Hanel",200);
	neue_node(anfang,"Thomas","Larch",100);
	ausgabe(anfang);
	printf("Anzahl\t%i\n",anzahl_Person(anfang));
	
	neue_node(anfang,"Thito","Jh",500);
	ausgabe(anfang);
	printf("Anzahl\t%i\n",anzahl_Person(anfang));
	
	anfang=neuer_anfang(anfang,"peter","peters",350);
	ausgabe(anfang);
	printf("Anzahl\t%i\n",anzahl_Person(anfang));
	
	return 0;
}



struct person* neue_node(struct person* anfang,char* Vorname,char* Nachname,int Punkte){
	if(anfang==NULL){
		anfang=(struct person*)malloc(sizeof(struct person));
		strcpy(anfang->Vorname, Vorname );
		strcpy(anfang->Nachname, Nachname);
		anfang->Punkte= Punkte;
		anfang->next=NULL;	
		
	}
	else{
		while(anfang->next!=NULL){
			anfang=anfang->next;	
		}
		anfang->next=(struct person*)malloc(sizeof(struct person));
		strcpy(anfang->next->Vorname, Vorname );
		strcpy(anfang->next->Nachname, Nachname);
		anfang->next->Punkte= Punkte;
		anfang->next->next=NULL;	
	}	
	return anfang;
}

void ausgabe (struct person* anfang){
	if(anfang==NULL){
		printf("Fehler keine Liste");
	}else{
		while (anfang !=NULL){
			printf("%s\t%s\t%i\n",anfang->Vorname,anfang->Nachname,anfang->Punkte);
			anfang=anfang->next;
		}
	}
}

int anzahl_Person(struct person* anfang){
	int anzahl;
	for(anzahl=0;anfang!=NULL;anzahl++){
		anfang=anfang->next;
	}
	return anzahl;
}

struct person* neuer_anfang(struct person* anfang,char* Vorname,char* Nachname,int Punkte){
	if(anfang=NULL){
		anfang=(struct person*)malloc(sizeof(struct person));
		strcpy(anfang->Vorname, Vorname );
		strcpy(anfang->Nachname, Nachname);
		anfang->Punkte= Punkte;
		anfang->next=NULL;	
		
	}
	else{
		struct person* neuer_anfang = (struct person*)malloc(sizeof(struct person));
		neuer_anfang->next = anfang;
		strcpy(neuer_anfang->Vorname, Vorname );
		strcpy(neuer_anfang->Nachname, Nachname);
		return neuer_anfang;
	}
}

