#include <iostream>
#include <string>
#include <stdio.h>

#define TAMANO_CADENA 50

using namespace std;

int main()
{
    string cadenaSinEspacios;
    char cadenaConEspacios[TAMANO_CADENA];

    cout << "Dame una cadena sin espacios: ";
    cin >> cadenaSinEspacios;
    cout << "La cadena leida es ***" << cadenaSinEspacios << "***" << endl << endl;
    getchar();

    cout << "Dame una cadena con espacios: ";
    cin.getline(cadenaConEspacios,TAMANO_CADENA);
    cout << "La segunda cadena leida es " << cadenaConEspacios << endl << endl;


    cout << "Ambas cadenas son: " << cadenaSinEspacios << "-" << cadenaConEspacios << endl << endl;
    cout << "presione entrar para continuar" << endl;
    getchar();
    return 0;
}
