#include <fstream>
#include <string>

using namespace std;

const int ile = 5;

string szyfruj(string jawny, int x, int y)
{
    string wynik = jawny;
    for(int i=0; i<wynik.length(); i++)
    {
        int c = wynik[i] - 'a';
        c = c*x + y;
        c %= 26;
        wynik[i] = c + 'a';
        
    }
    return wynik;
}

int main()
{
    ifstream in("probka.txt");
    ofstream out("wyniki.txt",fstream::app);
    for(int i=1; i<=ile; i++)
    {
        string jawne,zakodowane;
        in >> jawne;
        in >> zakodowane;
        for(int A=0; A<=25; A++)
            for(int B=0; B<=25; B++)
                if (szyfruj(jawne,A,B)==zakodowane)
                    out << "Klucz szyfrujacy numer " << i << ": (" << A << "," << B << ")" << endl;
        for(int A=0; A<=25; A++)
            for(int B=0; B<=25; B++)
                if (szyfruj(zakodowane,A,B)==jawne)
                    out << "Klucz deszyfrujacy numer " << i << ": (" << A << "," << B << ")" << endl;
    }
}
