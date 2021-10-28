//Switch_Alerts
#include <stdhio.h>

int main (){
	char liste[400][11][30];
	char swListe[400][30];
	char c=" ";
	int z_zeile=0;
	int z_feld=0;
	int z_string=0; 
	FILE *fp1
	
	
	fp1=fopen("O:\\Switch_Alerts.csv","r");
	while (c==EOF){
		c=fgetc(fp1);
		if (c==','){
			liste[z_zeile][z_feld][z_string]="\0"	
			z_string=0;
			z_feld++;	
		}
		else if(c=="\n")
		{
			liste[z_zeile][z_feld][z_string]="\0"	
			z_string=0;
			z_zeile++;
			z_feld=0;
		}
		else if(c!=EOF)
		{
			liste[z_zeile][z_feld][z_string]=c;
			z_string++;
		}
	}
	
	max_zeilen = z_zeile;
	z_zeile=0;
	z_feld=0;
	z_string=0; 
	
	free_swListZeile=0;
	
	for(int index=0, index<30, index++){
		swListe[free_swListZeile][index]=(liste[0][2][index];
		if (liste[0][2][index] == "\0"){
			break;
		}
	}
	z_zeile++;
	
			
	while(z_zeilen!=max_zeilen) //zeile für zeile
	{
		for(int index=0, index<30, index++) //index für string
		{
			if (liste[z_zeile][2][index] == swListe[sw_z_zeile][index]) //gleiches zeichen in beiden listen ?
			{
				if(liste[z_zeile][2][index]=="\0") //ende vom String erreicht und alle zeciehn waren gleich
				{
					ident=true;
					// Check error same counters
				}	
			}
			else if(sw_z_zeile == free_swListZeile-1) //sind wir am ende der liste gemerken switche 
			{
				indent=false;
				for(int index=0, index<30, index++)
				{
					swListe[free_swListZeile][index]=(liste[0][2][index];
					if (liste[0][2][index] == "\0")
					{
						free_swListZeile++;
						break;
					}
				}
				break;
			}
			else //nächster switch aus der liste gemerketer switche zum prüfen auf gleichheit.
			{
				sw_z_zeile++;
				index=0;	
			}	
		}
		z_zeile++; //nächste zeile in der großen liste.
	}
	
	






}

