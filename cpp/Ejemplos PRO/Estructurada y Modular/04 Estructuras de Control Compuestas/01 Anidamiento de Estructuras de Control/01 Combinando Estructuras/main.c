#include <stdio.h>
#include <stdlib.h>

#define SOFTWARE_DE_SISTEMAS 1
#define SISTEMAS_COMPUTACIONALES 2
#define SISTEMAS_DIGITALES 3
#define CALIFICACION_MINIMA 60

int main()
{
    char estudiarIngQuimica,descansarSemestre;
    int calificacion,opcion;
    printf("1 Cursar la Primaria\n");
    printf("2 Cursar la Secundaria\n");
    printf("3 Cursar la Preparatoria\n");
    printf("4 Cursar la Licenciatura\n");
    printf("  4.1 Cursar la carrera\n");
    printf("    4.1.1 Seleccionar las 2 carreras que me más me gusten\n");
    printf("    4.1.2 Elegir una carrera (Ing. Quimica o Ing. en Computacion)\n");
    printf("--->¿Estudiar Ingeneria Quimica (S/N)?");
    scanf("%c",&estudiarIngQuimica);  //antes de verificar se obtiene con qué evaluar
    printf("    4.1.3 Verificar si estudiar Ingenieria Quimica\n");
    if (estudiarIngQuimica=='S' || estudiarIngQuimica=='s'){
        printf("      4.1.3.1 Estudiar Ingenieria Quimica\n");
        printf("        4.1.3.1.1 Cursar las materias más fáciles\n");
        printf("        4.1.3.1.2 Cursar la materia mas dificil\n");
        do{
            printf("          4.1.3.1.2.1 Iniciar\n");
            printf("          4.1.3.1.2.2 Evaluar mi desempeño en el curso\n");
            printf("--------->¿Cuanto obtuviste de calificacion? ");
            scanf("%d",&calificacion);  //antes de verificar se obtiene con qué evaluar
            printf("          4.1.3.1.2.3 Verificar si cursar de nuevo\n");
        }while(calificacion<CALIFICACION_MINIMA);
        printf("        4.1.3.1.3 Cursar las materias optativas\n");
    }
    else{
        printf("      4.1.3.2 Estudiar Ingenieria en Computacion\n");
        printf("        4.1.3.2.1 Cursar las materias mas faciles\n");
        printf("        4.1.3.2.2 Evaluar un posible descanso de la carrera\n");
        printf("------->¿Descansar un semestre (S/N)?");
        getchar();
        scanf("%c",&descansarSemestre);  //antes de verificar se obtiene con qué evaluar
        while(descansarSemestre=='S' || descansarSemestre=='s'){
            printf("          4.1.3.2.2.1 Verificar si falto un semestre\n");
            printf("          4.1.3.2.2.2 Trabajar un tiempo\n");
            printf("          4.1.3.2.2.3 Regularizarme en conocimientos necesarios\n");
            printf("--------->¿Descansar otro semestre (S/N)?");
            getchar();
            scanf("%c",&descansarSemestre);  //antes de verificar se obtiene con qué evaluar
        }
        printf("        4.1.3.2.3 Cursar la especialidad de la carrera\n");
        printf("          4.1.3.2.3.1 Elegir una de las especialidades\n");
        printf("--------->1) Software de Sistemas\n");
        printf("--------->2) Sistemas Computacionales\n");
        printf("--------->3) Sistemas Digitales\n");
        printf("--------->4) Sistemas de Informacion\n");
        printf("--------->Elige una opción: ");
        scanf("%d",&opcion);  //antes de verificar se obtiene con qué evaluar
        printf("          4.1.3.2.3.2 Verificar por la opcion a seguir\n");
        switch(opcion){
            case SOFTWARE_DE_SISTEMAS:
                printf("            4.1.3.2.3.2.1 Cursar por Software de Sistemas\n");
                printf("              4.1.3.2.3.2.1.1 Cursar las materias mas faciles\n");
                printf("              4.1.3.2.3.2.1.2 Cursar la materia mas dificil\n");
                break;
            case SISTEMAS_COMPUTACIONALES:
                printf("            4.1.3.2.3.2.2 Cursar por Sistemas Computacionales\n");
                printf("              4.1.3.2.3.2.2.1 Cursar las materias mas faciles\n");
                printf("              4.1.3.2.3.2.2.2 Cursar la materia mas dificil\n");
                break;
            case SISTEMAS_DIGITALES:
                printf("            4.1.3.2.3.2.3 Cursar por Sistemas Digitales\n");
                printf("              4.1.3.2.3.2.3.1 Cursar las materias mas faciles\n");
                printf("              4.1.3.2.3.2.3.2 Cursar la materia mas dificil\n");
                break;
            default:
                printf("            4.1.3.2.3.2.4 Cursar por Sistemas de Informacion\n");
                printf("              4.1.3.2.3.2.4.1 Cursar las materias mas faciles\n");
                printf("              4.1.3.2.3.2.4.2 Cursar la materia mas dificil\n");
        }
        printf("        4.1.3.2.4 Cursar las materias optativas\n");
    }
    printf("  4.2 Graduarme de la carrera\n");
    printf("  4.3 Titularme de la carrera\n");
    printf("5 Cursar la Maestría\n");
    printf("6 Cursar el Doctorado\n");

    return 0;
}
