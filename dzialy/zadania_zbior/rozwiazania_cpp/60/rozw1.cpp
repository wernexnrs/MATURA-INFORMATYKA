#include <fstream>

using namespace std;

int main()
{
    ifstream in("liczby.txt");
    ofstream out("wyniki.txt",fstream::app);
    int przedostatnia = 0, ostatnia = 0;
    int licznik = 0;
    for(int i=0; i<200; i++)
    {
        int a;
        in >> a;
        if (a<1000)
        {
            przedostatnia = ostatnia;
            ostatnia = a;
            licznik++;
        }
    }
    out << "Mniejszych od 1000: " << licznik << endl;
    out << "Dwie ostatnie: " << przedostatnia << " " << ostatnia << endl;
}
