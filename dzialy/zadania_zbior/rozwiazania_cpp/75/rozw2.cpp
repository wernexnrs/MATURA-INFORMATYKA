#include <fstream>
#include <string>

using namespace std;

const int slowa = 805;

int main()
{
    string S;
    ifstream in("tekst.txt");
    ofstream out("wyniki.txt",fstream::app);
    out << "Zaszyfrowane slowa o co najmniej 10 literach:" << endl;
    for(int k=0; k<slowa; k++)
    {
        in >> S;
        for(int i=0; i<S.length(); i++)
        {
            S[i] -= 'a';
            S[i] = S[i]*5 + 2;
            S[i] %= 26;
            S[i] += 'a';
        }
        if (S.length()>=10)
            out << S << endl;
    }
}
