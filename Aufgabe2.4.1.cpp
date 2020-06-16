<<<<<<< HEAD
//Aufgabe 2.4.1
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct datum{int Tag,Monat,Jahr;};
struct person{char Name[35], Vorname[15];int Nummer;datum geboren;struct person*next;};
void printListe(struct person*Lkopf);
void addliste(struct person*Lkopf,struct person*neuePerson);
int zaehlElemente (struct person*Lkopf);
void addLelementAnf(struct person**Z_LKopf,struct person*neuePerson);


int main (){
	struct person*Lkopf;
	struct person*neuePerson;
	struct person*neuePerson2;
	int summeElemente;
	Lkopf =(struct person*) malloc (sizeof(struct person));
	neuePerson=(struct person*) malloc (sizeof(struct person));
	neuePerson2=(struct person*) malloc (sizeof(struct person));
	
	
	strcpy(Lkopf->Name,"Larch");
	strcpy(Lkopf->Vorname,"Thomas");
	Lkopf->Nummer= 1;
	(*Lkopf).geboren.Tag=26;
	(*Lkopf).geboren.Monat=7;
	(*Lkopf).geboren.Jahr=1987;
	Lkopf->next=NULL;
	
	strcpy(neuePerson->Name,"Larch2");
	strcpy(neuePerson->Vorname,"Thomas2");
	neuePerson->Nummer= 2;
	(*neuePerson).geboren.Tag=27;
	(*neuePerson).geboren.Monat=8;
	(*neuePerson).geboren.Jahr=1980;
	neuePerson->next=NULL;
	
	addliste(Lkopf,neuePerson);
	
	
	
	strcpy(neuePerson2->Name,"Larch3");
	strcpy(neuePerson2->Vorname,"Thomas3");
	neuePerson2->Nummer= 3;
	(*neuePerson2).geboren.Tag=28;
	(*neuePerson2).geboren.Monat=9;
	(*neuePerson2).geboren.Jahr=1981;
	neuePerson2->next=NULL;
	//addliste(Lkopf,neuePerson2);
	addLelementAnf(&Lkopf,neuePerson2);
	printListe(Lkopf);
	summeElemente=zaehlElemente(Lkopf);
	printf("\nAnzahl Listenelemente: %d\n",zaehlElemente(Lkopf));
	
	
	return 0;
	
}
void printListe(struct person*Lkopf){
	struct person *aktPerson;
	aktPerson=Lkopf;
	while(aktPerson != NULL){
		printf("Ausgabe Kopf: %s\n",aktPerson->Name);
		printf("Ausgabe Kopf: %s\n",aktPerson->Vorname);
		printf("Ausgabe Kopf: %i\n",aktPerson->Nummer);
		printf("Ausgabe Kopf: %i\n",(*aktPerson).geboren.Tag);
		printf("Ausgabe Kopf: %i\n",(*aktPerson).geboren.Monat);
		printf("Ausgabe Kopf: %i\n\n",(*aktPerson).geboren.Jahr);
		aktPerson=aktPerson->next;
	}
	
	
}
void addliste(struct person*Lkopf,struct person*neuePerson){
	struct person *aktPerson;
	aktPerson=Lkopf;
	while(aktPerson != NULL){
		if(aktPerson->next == NULL){
			aktPerson->next =neuePerson;
			break;
		}else
			aktPerson=aktPerson->next;
	}
	

}
int zaehlElemente (struct person*Lkopf){
	struct person*aktuellesElement;
	int summeElemente=0;
	aktuellesElement=Lkopf;
	while(aktuellesElement != NULL){
		summeElemente=summeElemente+1;
		aktuellesElement=aktuellesElement->next;
		
	}
	return summeElemente;
	
}
void addLelementAnf(struct person**Z_LKopf,struct person*neuePerson){
	neuePerson->next=*Z_LKopf;
	*Z_LKopf=neuePerson;
}
=======
//Aufgabe 2.4.1
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct datum{int Tag,Monat,Jahr;};
struct person{char Name[35], Vorname[15];int Nummer;datum geboren;struct person*next;};
void printListe(struct person*Lkopf);
void addliste(struct person*Lkopf,struct person*neuePerson);
int zaehlElemente (struct person*Lkopf);
void addLelementAnf(struct person**Z_LKopf,struct person*neuePerson);


int main (){
	struct person*Lkopf;
	struct person*neuePerson;
	struct person*neuePerson2;
	int summeElemente;
	Lkopf =(struct person*) malloc (sizeof(struct person));
	neuePerson=(struct person*) malloc (sizeof(struct person));
	neuePerson2=(struct person*) malloc (sizeof(struct person));
	
	
	strcpy(Lkopf->Name,"Larch");
	strcpy(Lkopf->Vorname,"Thomas");
	Lkopf->Nummer= 1;
	(*Lkopf).geboren.Tag=26;
	(*Lkopf).geboren.Monat=7;
	(*Lkopf).geboren.Jahr=1987;
	Lkopf->next=NULL;
	
	strcpy(neuePerson->Name,"Larch2");
	strcpy(neuePerson->Vorname,"Thomas2");
	neuePerson->Nummer= 2;
	(*neuePerson).geboren.Tag=27;
	(*neuePerson).geboren.Monat=8;
	(*neuePerson).geboren.Jahr=1980;
	neuePerson->next=NULL;
	
	addliste(Lkopf,neuePerson);
	
	
	
	strcpy(neuePerson2->Name,"Larch3");
	strcpy(neuePerson2->Vorname,"Thomas3");
	neuePerson2->Nummer= 3;
	(*neuePerson2).geboren.Tag=28;
	(*neuePerson2).geboren.Monat=9;
	(*neuePerson2).geboren.Jahr=1981;
	neuePerson2->next=NULL;
	//addliste(Lkopf,neuePerson2);
	addLelementAnf(&Lkopf,neuePerson2);
	printListe(Lkopf);
	summeElemente=zaehlElemente(Lkopf);
	printf("\nAnzahl Listenelemente: %d\n",zaehlElemente(Lkopf));
	
	
	return 0;
	
}
void printListe(struct person*Lkopf){
	struct person *aktPerson;
	aktPerson=Lkopf;
	while(aktPerson != NULL){
		printf("Ausgabe Kopf: %s\n",aktPerson->Name);
		printf("Ausgabe Kopf: %s\n",aktPerson->Vorname);
		printf("Ausgabe Kopf: %i\n",aktPerson->Nummer);
		printf("Ausgabe Kopf: %i\n",(*aktPerson).geboren.Tag);
		printf("Ausgabe Kopf: %i\n",(*aktPerson).geboren.Monat);
		printf("Ausgabe Kopf: %i\n\n",(*aktPerson).geboren.Jahr);
		aktPerson=aktPerson->next;
	}
	
	
}
void addliste(struct person*Lkopf,struct person*neuePerson){
	struct person *aktPerson;
	aktPerson=Lkopf;
	while(aktPerson != NULL){
		if(aktPerson->next == NULL){
			aktPerson->next =neuePerson;
			break;
		}else
			aktPerson=aktPerson->next;
	}
	

}
int zaehlElemente (struct person*Lkopf){
	struct person*aktuellesElement;
	int summeElemente=0;
	aktuellesElement=Lkopf;
	while(aktuellesElement != NULL){
		summeElemente=summeElemente+1;
		aktuellesElement=aktuellesElement->next;
		
	}
	return summeElemente;
	
}
void addLelementAnf(struct person**Z_LKopf,struct person*neuePerson){
	neuePerson->next=*Z_LKopf;
	*Z_LKopf=neuePerson;
}
>>>>>>> 33a1bf1eb8ce5cf1ea81e18a0ffe1092ed551610
