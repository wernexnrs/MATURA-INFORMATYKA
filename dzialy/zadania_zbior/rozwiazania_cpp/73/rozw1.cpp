#include <fstream>
#include <string>

using namespace std;

const int dlugosc = 1876;

int main()
{
    ifstream in("tekst.txt");
    ofstream out("wyniki.txt");
    int licznik = 0;
    for(int i=0; i<dlugosc; i++)
    {
        string slowo;
        in >> slowo;
        for(int j=0; j<slowo.length()-1; j++)
            if (slowo[j]==slowo[j+1])
            {
                licznik++;
                break;
            }
    }
    out << "Slow z dwoma kolejnymi literami: " << licznik << endl;
}
