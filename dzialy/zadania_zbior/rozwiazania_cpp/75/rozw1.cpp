#include <fstream>
#include <string>
#include <iostream>

using namespace std;

const int slowa = 805;

int main()
{
    string S;
    ifstream in("tekst.txt");
    ofstream out("wyniki.txt");
    out << "Slowa zaczynajace sie i konczace na 'd':" << endl;
    for(int i=0; i<slowa; i++)
    {
        in >> S;
        if (S[0]=='d' && S[S.length()-1]=='d')
            out << S << endl;
    }
}
