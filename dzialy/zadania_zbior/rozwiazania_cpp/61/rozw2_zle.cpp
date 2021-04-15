// Bledne rozwiazania zadania 2 - wypisuje wszystkie szesciany, nie tylko najwiekszy w kazdym ciagu.

#include <fstream>
#include <algorithm>

using namespace std;

const int N = 100;

bool szescian(int liczba)
{
    for(int x = 1; x <= 100; x++)
        if (x*x*x == liczba)
            return true;
    return false;
}

int main()
{
    ifstream in("ciagi.txt");
    ofstream out("wynik2_zle.txt");
    int koniec7 = 0;
    int calk7 = 0;
    for(int q = 0; q < N; q++)
    {
        int dlugosc;
        in >> dlugosc;
        for(int i = 0; i < dlugosc; i++)
        {
            int liczba;
            in >> liczba;
            if (szescian(liczba))
                out << liczba << endl;
        }
    }
}
