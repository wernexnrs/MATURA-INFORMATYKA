#include <fstream>

using namespace std;

const int rozmiar = 200;


int nwd(int x, int y)
{
    if (x < y)
        return nwd(y,x);
    if (y == 0)
        return x;
    return nwd(y,x%y);
}

int main()
{
    ifstream in("liczby.txt");
    ofstream out("wyniki.txt",fstream::app);
    int liczby[rozmiar];
    for(int i=0; i<rozmiar; i++)
    {
        int a;
        in >> liczby[i];
    }
    int najwieksza = 0;
    for(int i=0; i<rozmiar; i++)
    {
        bool ok = true;
        for(int j=0; j<rozmiar; j++)
            if (i != j && nwd(liczby[i],liczby[j])>1)
                ok = false;
        if (ok && liczby[i] > najwieksza)
            najwieksza = liczby[i];
    }
    out << "Najwieksza wzglednie pierwsza: " << najwieksza << endl;
}
