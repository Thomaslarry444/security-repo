//Aufgabe 1.1
# include <stdio.h>
int main(){
int i=7,*z_int;
z_int=&i;
printf("\n\n%i ",*z_int);
printf("\n\n%i ",*z_int+2);
printf("\n\n%i ",*(&i));
printf("\n\n%i ",(*z_int)++);
return 0;
}
