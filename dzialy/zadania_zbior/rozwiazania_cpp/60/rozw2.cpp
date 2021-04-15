#include <fstream>

using namespace std;

int main()
{
    ifstream in("liczby.txt");
    ofstream out("wyniki.txt",fstream::app);
    for(int i=0; i<200; i++)
    {
        int a;
        in >> a;
        int ile_dzielnikow = 0;
        for(int i=1; i<=a; i++)
            if (a%i == 0)
                ile_dzielnikow++;
        if (ile_dzielnikow==18)
        {
            out << a << endl;
            for(int i=1; i<=a; i++)
                if (a%i == 0)
                    out << i << " ";
            out << endl;
        }
    }
}
