#include <fstream>
#include <string>

using namespace std;

const int N = 200;

int main()
{
    ifstream in("napisy.txt");
    ofstream out("wyniki.txt");
    int wynik = 0;
    bool wypisalem = false;
    for(int i=0; i<N; i++)
    {
        string a,b;
        in >> a >> b;
        if (a.length()>=3*b.length() || a.length()*3 <= b.length())
        {
            wynik++;
            if (!wypisalem)
            {
                wypisalem = true;
                out << "Pierwsza para: " << endl;
                out << a << " " << b << endl;
            }
        }
    }
    out << "Par znalezionych: " << endl;
    out << wynik << endl;
}
