#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c;
    float d;
    char letra;
    a=10;
    printf("primero a=%d\n",a);
    b=a++;
    printf("luego a=%d y b=%d\n",a,b);
    c=++a;
    printf("ahora a=%d y c=%d\n",a,c);
    c--; //tambien le aplica notacion prefija y sufija
    printf("ahora a=%d y c=%d\n",a,c);
    d=0.5;
    d++;
    letra=65;
    letra++;
    printf("d=%f\n",d);
    printf("letra=%c\n",letra);
    return 0;
}
