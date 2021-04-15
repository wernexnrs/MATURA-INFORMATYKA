#include <fstream>
#include <string>

using namespace std;

const int dlugosc = 1876;

int spolgloski(string A)
{
    int s = 0;
    int ciag = 0;
    for(int i=0; i<A.length(); i++)
    {
        if (A[i]=='A' || A[i]=='E' || A[i]=='O' || A[i]=='U' || A[i]=='I' || A[i]=='Y')
            s = 0;
        else
            s++;
        if (s > ciag)
            ciag = s;
    }
    return ciag;
}


int main()
{
    ifstream in("tekst.txt");
    ofstream out("wyniki.txt",fstream::app);
    int najdluzsze = 0;
    int licznik = 0;
    string odpowiedz;
    for(int i=0; i<dlugosc; i++)
    {
        string slowo;
        in >> slowo;
        int k = spolgloski(slowo);
        if (k>najdluzsze)
        {
            najdluzsze = k;
            licznik = 1;
            odpowiedz = slowo;
        } 
        else if (k==najdluzsze)
            licznik ++;
    }
    out << "Najdluzszy ciag spolglosek: " << najdluzsze << endl;
    out << "Znalezionych slow: " << licznik << endl;
    out << "Pierwsze z nich: " << odpowiedz << endl;
}
