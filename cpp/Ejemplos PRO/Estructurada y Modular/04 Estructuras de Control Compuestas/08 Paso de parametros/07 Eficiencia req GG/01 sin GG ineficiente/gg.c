#include <stdio.h>
#include <stdlib.h>

int potencia(int base,int exponente);

int main()
{
    int base,exponente,resultado,sumable;
    printf("Dame la base: ");
    scanf("%d",&base);
    printf("Dame el exponente: ");
    scanf("%d",&exponente);
    printf("Dime con cual lo sumo: ");
    scanf("%d",&sumable);
    resultado=potencia(base,exponente);
    resultado=sumable+potencia(base,exponente);//evitar llamar 2 veces si se obtiene lo mismo
    printf("%d a la %d es %d\n",base,exponente,resultado);
    printf("tras la suma es %d\n",resultado);
    return 0;
}

int potencia(int base,int exponente){
    int i,resultado;
    resultado=1;
    for(i=0;i<exponente;i++){
        resultado*=base;
    }
    return resultado;
}

