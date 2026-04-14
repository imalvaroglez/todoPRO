#include <iostream>
#include <string.h>
#include "AdminCirculos.h"
#include "Circulo.h"

using namespace std;

AdminCirculos* adminCirculos;

int main()
{
    //AdminCirculos* adminCirculos=new AdminCirculos;//diferencia de local a global?
    int veces=0,tamanioAdmin;
    try
    {
        while(1)
        {
            veces++;
            //cout << veces << endl;
            adminCirculos=new AdminCirculos;//el constructor podria imprimir pero tarda mas
        }
    }catch(bad_alloc& e){
    //}catch(exception& e){//excepcion generica
        cout << "Excepcion bad_alloc: " << e.what() << endl;
        cout << "Ya no se pudo crear mas objetos" << endl;
        adminCirculos=NULL;
    }
    cout << "veces que itero: " << veces << endl;
    cout << "tamanio en RAM de AdminCirculos: " <<
        (tamanioAdmin=sizeof(AdminCirculos)) << endl;
    cout << "memoria RAM usada y no liberada: " << tamanioAdmin*veces<< endl;
    veces=2000000000;
    cout << "capacidad de int supera las:     " << veces << endl;
    cout << "Presiona entrar para terminar..." << endl;
    cin.get();
    return 0;
}
