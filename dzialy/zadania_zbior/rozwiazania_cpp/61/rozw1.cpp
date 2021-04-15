#include <fstream>
#include <algorithm>

using namespace std;

const int N = 100;

int main()
{
    ifstream in("ciagi.txt");
    ofstream out("wynik1.txt");
    int ciag[1000];
    int ilearytm = 0;
    int maxroznica = 0;
    for(int q = 0; q < N; q++)
    {
        int dlugosc;
        in >> dlugosc;
        for(int i = 0; i < dlugosc; i++)
            in >> ciag[i];
        int roznica = ciag[1] - ciag[0];
        bool arytm = true;
        for(int i = 0; i+1 < dlugosc; i++)
            if (ciag[i+1] - ciag[i] != roznica)
            {
                arytm = false;
                break;
            }
        if (arytm)
        {
            ilearytm++;
            if (roznica>maxroznica)
                maxroznica = roznica;
        }
    }
    out << "Ciagow arytmetycznych: " << ilearytm << endl;
    out << "Najwieksza roznica: " << maxroznica << endl;
}
