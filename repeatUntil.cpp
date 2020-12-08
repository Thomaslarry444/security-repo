//Test
# include <stdio.h>

int main (){
	int i=1;
	int b=1;
	do{
		i=i+1;
		b=b+2;
		//printf("i= %i\nb= %i\n",i,b);	
	}
	while ((b+2*i)<20);
	return 0;
}
