#include <stdio.h>
#include <stdlib.h>

#define ENERO 1
#define DICIEMBRE 12

int main()
{
    int mes;
    int mesValido;
    printf("dame un numero de mes:");
    scanf("%d",&mes);
    mesValido=(ENERO<=mes)&&(mes<=DICIEMBRE);
    if (mesValido){
        printf("es un mes valido\n");
    }
    else{
        printf("mes no valido\n");
    }
    return 0;
}
