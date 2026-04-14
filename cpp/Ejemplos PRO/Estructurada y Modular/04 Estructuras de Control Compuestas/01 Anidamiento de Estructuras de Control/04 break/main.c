#include <stdio.h>
#include <stdlib.h>

#define TOTAL_VALORES 5

int main()
{
    int valores[]={90,95,100,80,85};
    int i,aEncontrar,seEncontro;
    printf("Dime cual valor buscar: ");
    scanf("%d",&aEncontrar);
    for(i=0,seEncontro=0;i<TOTAL_VALORES;i++){
        printf("Buscando en el indice %d\n",i);
        if (valores[i]==aEncontrar){
            seEncontro=1;
            break;
        }
    }
    if (seEncontro){
        printf("Se encontro el valor buscado en el indice %d\n",i);
    }
    else{
        printf("No se encontro el valor buscado\n");
    }
    return 0;
}
