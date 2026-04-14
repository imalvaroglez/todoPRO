#include <stdio.h>
#include <stdlib.h>

int main()
{
    int valores[]={100,90,95,85,90,95,100};
    int i,j;
    for(i=0,j=7;i<j;i++){
        printf("valores[%d]=%d\n",i,valores[i]);
    }
    return 0;
}
