//Schulnoten 
# include <stdio.h>
# define MAX 10
# define best 1
# define worst 6

int main (){
	float Schulnoten[MAX];
	float Durchschnitt;
	bool feunf_gefunden=false;
	bool drei_gefunden=false;
	float ergbnis=0;
	printf("Gib 10 Schulnoten ein , Kommazahlen. \n");
	for (int i=0;i<MAX;i++){
		do{
			scanf("%f", &Schulnoten[i]);
			if (Schulnoten[i]>worst ||Schulnoten[i]<best){
				printf("falsche Eingabe \n");
				
			}
		}while (Schulnoten[i]>worst ||Schulnoten[i]<best); 
		
	}
	for (int i=0;i<MAX;i++){
	ergbnis=ergbnis+Schulnoten[i];
	}
	Durchschnitt=ergbnis/MAX;
	printf("Durschnittswert Schulnoten: %f", Durchschnitt);
	
	for (int i=0;i<MAX;i++){
		if (Schulnoten[i]==6.0){
			printf("Sitzen geblieben \n");
			break;
		}
	}
	for (int i=0;i<MAX;i++){
		if (Schulnoten[i]==5){
			feunf_gefunden=true;
			//printf 1x5 gefunden
			
		}
		if(Schulnoten[i]==5 && feunf_gefunden==true){
			for (int j=0;i<MAX;i++){
				//printf 2x5 gefunden
				if (Schulnoten[i]==3){
					drei_gefunden=true;
					
				}
				if(Schulnoten[j]==3 && drei_gefunden==true){
					printf("2x Ausgeglichen mit 2x3 ergo super geschafft");
					break;
				
				}
				if (j==MAX-1){
					printf("Dann auch sitzen geblieben");
					break;
				}	
			}
		}
	}
	
	return 0;
}


