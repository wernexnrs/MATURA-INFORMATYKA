#include <fstream>
#include <string>

using namespace std;

const int N = 200;


int koncowka(string A, string B)
{
    int dl_A = A.length();
    int dl_B = B.length();
    int k = 0;
    while(k<dl_A && k<dl_B && A[dl_A-1-k]==B[dl_B-1-k])
        k++;
    return k;
}

int main()
{
    ifstream in("napisy.txt");
    ofstream out("wyniki.txt",fstream::app);
    int dlugosc = 0;
    string pierwszy[N],drugi[N];
    int wspolna[N];
    for(int i=0; i<N; i++)
    {
        in >> pierwszy[i] >> drugi[i];
        wspolna[i] = koncowka(pierwszy[i],drugi[i]);
        if (wspolna[i] > dlugosc)
            dlugosc = wspolna[i];
    }
    out << "Maksymalna koncowka: " << dlugosc << endl;
    for(int i=0; i<N; i++)
        if (wspolna[i]==dlugosc)
            out << pierwszy[i] << " " << drugi[i] << endl;
}
