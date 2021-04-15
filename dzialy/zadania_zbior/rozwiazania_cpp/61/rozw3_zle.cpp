// Bledne rozwiazanie zadania 3 - nie uwzglednia mozliwego bledu na pierwszym i drugim wyrazie ciagu.

#include <fstream>
#include <algorithm>

using namespace std;

const int N = 20;

int main()
{
    ifstream in("bledne.txt");
    ofstream out("wynik3_zle.txt");
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
        
        for(int i = 0; i+1 < dlugosc; i++)
            if (roznice[i] != roznice[0])
            {
                out << ciag[i+1] << endl;
                break;
            }
    }
}
