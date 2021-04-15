#include <fstream>
#include <algorithm>

using namespace std;

const int N = 100;

bool czy_szescian(int liczba)
{
    for(int x = 1; x <= 100; x++)
        if (x*x*x == liczba)
            return true;
    return false;
}

int main()
{
    ifstream in("ciagi.txt");
    ofstream out("wynik2.txt");
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
