// Alternatywne rozwiazanie zadania 2 (z uzyciem funkcji matematycznych)

#include <fstream>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int N = 100;

bool czy_szescian(int liczba)
{
    double pierwiastek = pow(liczba,1.0/3.0);
    int pz = (int)round(pierwiastek);
    if (pz*pz*pz==liczba)
        return true;
    else
        return false;
}

int main()
{
    ifstream in("ciagi.txt");
    ofstream out("wynik2a.txt");
    out << "Najwieksze szesciany: " << endl;
    for(int q = 0; q < N; q++)
    {
        int dlugosc;
        in >> dlugosc;
        int m = 0;
        for(int i = 0; i < dlugosc; i++)
        {
            int liczba;
            in >> liczba;
            if (czy_szescian(liczba))
                m = liczba;
        }
        if (m>0)
            out << m << endl;
    }
}
