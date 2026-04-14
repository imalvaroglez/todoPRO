#include <stdio.h>
#include <stdlib.h>

int main()
{
    short int enteroCortoNegativo=0x8000;  //notacion hexadecimal
    int enteroNegativo=0x80000000;
    float flotante=-0.1e-2f;
    double doblePrecision=1e-35;
    printf("enteroCortoNegativo=%d\n",enteroCortoNegativo);
    printf("enteroNegativo=%d\n",enteroNegativo);
    printf("flotante=%f\n",flotante);
    printf("doblePrecision=%0.40f\n",doblePrecision);
    return 0;
}
