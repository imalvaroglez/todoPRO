#include <iostream>
#include <string.h>

using namespace std;

#define TAMANO_NOMBRE 50
#define TAMANO_RFC 13

struct Persona{
    int codigo;
    char nombre[TAMANO_NOMBRE+1];
    char rfc[TAMANO_RFC+1];//13 caracteres más el caracter '\0'
    float salario;
};

int main()
{
    Persona profe,inge;

    profe.codigo=2233517;
    strcpy(profe.nombre,"Luis Alberto Munoz Gomez");
    strcpy(profe.rfc,"MUGL790912IC7");
    profe.salario=5000;
    inge=profe;
    inge.salario+=20000;

    cout << "Imprimiendo variable registro profe:" << endl;
    cout << "Codigo=" << profe.codigo << endl;
    cout << "Nombre="  << profe.nombre << endl;
    cout << "RFC=" << profe.rfc << endl;
    cout << "Salario=" << profe.salario << endl;

    cout << "\nImprimiendo variable registro inge:" << endl;
    cout << "Codigo=" << inge.codigo << endl;
    cout << "Nombre=\n" << inge.nombre << endl;
    cout << "RFC=" << inge.rfc << endl;
    cout << "Salario=" << inge.salario << endl;

    return 0;
}
