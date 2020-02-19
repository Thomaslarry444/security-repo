//Aufgabe 2.2
#include <stdio.h>
float v_berech(float durchem, float hoehe);

int main(){
	float durchmesser,hoehe,volumen;
	printf("bitte durchmesser eingeben:\t");
	scanf("%f",&durchmesser);
	printf("bitte hoehe eingeben:\t");
	scanf("%f",&hoehe);
	if (durchmesser<0||hoehe<0){
		printf("Werte ist minus du null");
		return -1;
	}
	volumen=v_berech(durchmesser,hoehe);
	printf("Das Volumen beträgt \n %f",volumen);
	
	
	return 0;
}

float v_berech(float durchem, float hoehe){
	float volumen;
	float pi;
	pi=3.14;
	volumen=pi*0.5*durchem*0.5*durchem*hoehe;
	
	return volumen;
}
