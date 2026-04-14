#include <iostream>

#define ENERO 1
#define DICIEMBRE 12

using namespace std;

int main()
{
    int mes;
    bool mesValido;
    cout << "dame un numero de mes:";
    cin >> mes;
    mesValido=(ENERO<=mes)&&(mes<=DICIEMBRE);
    if (mesValido){
        cout  << "es un mes valido" << endl;
    }
    else{
        cout << "mes no valido" << endl;
    }
    cout << "mesValido vale " << mesValido << endl;
    mesValido=false;
    cout << "mesValido vale " << mesValido << endl;
    mesValido=true;
    cout << "mesValido vale " << mesValido << endl;
    mesValido=2;
    cout << "mesValido vale " << mesValido << endl;
    return 0;
}
