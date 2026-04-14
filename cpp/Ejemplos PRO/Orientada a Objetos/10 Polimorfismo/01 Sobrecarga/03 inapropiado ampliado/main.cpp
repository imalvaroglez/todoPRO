#include <iostream>
#include <sstream>
#include "util.h"

using namespace std;

class Empleado{
    static constexpr float SALARIO_BASE=10000;
    static constexpr int EDAD_MINIMA=18;
    string nombre;
    int edad;
    double salario;
public:
    Empleado(string nombre, int edad,double salario){
        this->nombre = nombre;
        this->edad = edad;
        this->salario=salario;
    }
    Empleado(string nombre,int edad){
        this->nombre = nombre;
        this->edad = edad;
        this->salario=SALARIO_BASE;
    }
    Empleado(string nombre,double salario){
        this->nombre = nombre;
        this->edad = EDAD_MINIMA;
        this->salario=salario;
    }
    Empleado(string nombre){
        this->nombre = nombre;
        this->edad = EDAD_MINIMA;
        this->salario=SALARIO_BASE;
    }
    void fijaDatos(string nombre){
        this->nombre=nombre;
    }
    void fijaDatos(string nombre,int edad){
        this->nombre=nombre;//inapropiado por futura validacion en atributo nombre
        if (edad>=EDAD_MINIMA){
            this->edad=edad;
        }
        //en este momento tenemos 4 lineas de codigo fuente repetidas
    }
    void fijaDatos(string nombre,int edad,float salario){
        this->nombre=nombre;//inapropiado por futura validacion en atributo nombre
        if (edad>=EDAD_MINIMA){
            this->edad=edad;
        }
        //en este momento tenemos 4 lineas de codigo fuente repetidas
        this->salario=salario;
    }
    string dameInfo(){
        stringstream s;
        s << "---Datos del empleado---" << endl;
        s << "Nombre:" << nombre << endl;
        s << "Edad:" << edad << endl;
        s << "Salario:" << salario << endl;
        return s.str();
    }
};

int main()
{
    cout << "--- Instanciando ---" << endl;
    Empleado luis("Luis");
    Empleado alberto("Alberto",20000.0);
    Empleado alex("Alex",18);
    Empleado luisAlberto("Luis Alberto",29,30000);
    cout << luis.dameInfo();
    cout << alberto.dameInfo();
    cout << alex.dameInfo();
    cout << luisAlberto.dameInfo();
    pausar();
    luisAlberto.fijaDatos("Luis Alberto Munoz");
    cout << luisAlberto.dameInfo();
    pausar();
    luisAlberto.fijaDatos("Luis Alberto Munoz G",30);
    cout << luisAlberto.dameInfo();
    pausar();
    luisAlberto.fijaDatos("Luis Alberto Munoz Gomez",31,40000);
    cout << luisAlberto.dameInfo();
    pausar();
    return 0;
}
