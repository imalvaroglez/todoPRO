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
    Empleado(string nombre,int edad):
        Empleado(nombre,edad,SALARIO_BASE){
    }
    Empleado(string nombre,double salario):
        Empleado(nombre,EDAD_MINIMA,salario){
    }
    Empleado(string nombre):
        Empleado(nombre,SALARIO_BASE){
    }
    void fijaDatos(string nombre){
        this->nombre=nombre;
    }
    void fijaDatos(string nombre,int edad){
        fijaDatos(nombre);
        if (edad>=EDAD_MINIMA){
            this->edad=edad;
        }
        //else no cambio la edad por no permitir menores de edad
    }
    void fijaDatos(string nombre,int edad,float salario){
        fijaDatos(nombre,edad);
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
