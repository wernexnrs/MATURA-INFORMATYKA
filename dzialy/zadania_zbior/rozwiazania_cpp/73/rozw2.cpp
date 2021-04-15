#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

const int dlugosc = 1876;

int main()
{
    ifstream in("tekst.txt");
    ofstream out("wyniki.txt",fstream::app);
    int czestotliwosc[26];
    for(int j=0; j<26; j++)
        czestotliwosc[26] = 0;
    int suma = 0;
    for(int i=0; i<dlugosc; i++)
    {
        string slowo;
        in >> slowo;
        for(int j=0; j<slowo.length(); j++)
            czestotliwosc[slowo[j]-'A']++;
        suma += slowo.length();
    }
    for(int j=0; j<26; j++)
    {
        out << (char)('A'+j) << ": " << czestotliwosc[j];
        out << " (" << fixed << setprecision(2) <<  100*czestotliwosc[j]/(double)suma << "%)" << endl;
    }
}
