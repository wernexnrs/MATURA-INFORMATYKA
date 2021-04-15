#include <fstream>
#include <algorithm>

using namespace std;

const int N = 20;

int main()
{
    ifstream in("bledne.txt");
    ofstream out("wynik3.txt");
    int ciag[1000];
    int roznice[1000];
    for(int q = 0; q < N; q++)
    {
        int dlugosc;
        in >> dlugosc;
        for(int i = 0; i < dlugosc; i++)
            in >> ciag[i];
        for(int i = 0; i+1 < dlugosc; i++)
            roznice[i] = ciag[i+1] - ciag[i];
        
        // jesli pierwsza roznica jest inna niz pozostale, blad jest w pierwszym wyrazie
        if (roznice[0]!=roznice[1] && roznice[1]==roznice[2])
        {
            out << ciag[0] << endl;
            continue;
        }
        // jesli pierwsze dwie roznice sa inne niz pozostale, blad jest w drugim wyrazie
        if (roznice[0]!=roznice[2] && roznice[1]!=roznice[2] && roznice[3]==roznice[2])
        {
            out << ciag[1] << endl;
            continue;
        }
        // w innym wypadku bledny jest ten wyraz, ktory daje inna roznice niz pozostale (czyli niz roznice[0])
        for(int i = 0; i+1 < dlugosc; i++)
            if (roznice[i] != roznice[0])
            {
                out << ciag[i+1] << endl;
                break;
            }
    }
}
