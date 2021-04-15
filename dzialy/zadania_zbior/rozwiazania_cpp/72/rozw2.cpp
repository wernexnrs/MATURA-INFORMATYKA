#include <fstream>
#include <string>

using namespace std;

const int N = 200;

int main()
{
    ifstream in("napisy.txt");
    ofstream out("wyniki.txt",fstream::app);
    int wynik = 0;
    bool wypisalem = false;
    out << "Pary, dla ktorych drugi lancuch jest wydluzeniem pierwszego: " << endl;
    for(int i=0; i<N; i++)
    {
        string a,b;
        in >> a >> b;
        if (a.length()>b.length())
            continue;
        bool dobry = true;
        for(int j=0; j<a.length(); j++)
            if (a[j]!=b[j])
                dobry = false;
        if (dobry)
        {
            out << a << " " << b << " ";
            for(int j=a.length(); j<b.length(); j++)
                out << b[j];
            out << endl;
        }
    }
}
