#include <stdio.h>

int main()
{
    float Monatsertrag=0.0;
    float Pauschale, maxMenge, lieferMenge;
    char wiederholen;

    printf("Bitte die Pauschale eingeben.");
    scanf("%f",&maxMenge);

    do
    {
        do
        {
            printf("Bitte maxMenge einegeben: ");
            scanf("%f",&maxMenge);
            printf("Bitte lieferMenge eingeben: ");
            scanf("%f",&lieferMenge);

            if(lieferMenge > maxMenge)
            {
                lieferMenge = maxMenge;
            }
            else
            {
                if (lieferMenge < 0)
                {
                    printf("Unsinnige Eingabe.");
                }
            }
        } while (lieferMenge < 0);

        Monatsertrag = Monatsertrag+lieferMenge*Pauschale;

        printf("Eingabe wiederholen ? (J/N)");
        scanf("%c",&wiederholen);

    } while (wiederholen == 'J');
    
    printf("Der Monatsertrag beträgt: %f",Monatsertrag);
}
