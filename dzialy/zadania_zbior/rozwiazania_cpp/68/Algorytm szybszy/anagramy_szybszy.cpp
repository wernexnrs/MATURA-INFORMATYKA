#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;

//typedef czestosc int;
string s1[2000];
int c1[2000][10];


bool jednolity(string s)
{
    for(int i=1; i<s.length();i++)
        if (s[i]!=s[i-1]) return false;
    return true;
}


bool czyAnag(int t1[10], int t2[10])
{
    int i;

    for(i=0;i<10;i++) //porownywanie czy tyle samo kazdej litery
        if (t1[i]!=t2[i]) return false;

    return true;
}

int puntkCPom(int c[10], int dokad)
{
        int ile=0,j;
        for(j=0;j<dokad;j++){ // zliczanie anagramow s1[i] w calym pliku
            if (czyAnag(c,c1[j])) ile++;
        }
        return ile;

}

int punktC()
{   int maxPowt=0, ilePowt, maxIndeks=-1;
    string s;
    int i, j;

    for(i=0; i<2000; i++){
        ilePowt=puntkCPom(c1[i],i); //tylko do i-tego elementu
        if (ilePowt>maxPowt) {
                maxPowt=ilePowt; maxIndeks=i;
        }

    }

    return maxPowt;
}

void zamien(string slowo, int t[10])
{   int i;
    for(i=0;i<10;i++)
        t[i] = 0;
    for(i=0;i<slowo.length();i++)
        t[slowo[i] - 65]++;


}
int main()
{
	string x;

	ifstream in;
	ofstream out;
	in.open("dane_napisy.txt");
	out.open("wynik_napisy.txt");


    int ileB = 0, ileA=0;
	for (int i=0; i<2000; i++)
	{
		in >> s1[i];
        zamien(s1[i],c1[i]);
        if (i%2==1){
            if (czyAnag(c1[i],c1[i-1])) ileB++;
            if (jednolity(s1[i]) && (s1[i]==s1[i-1]))
              {
                    ileA++;
                }
        }
	}

    out << "Punkt (a): ";
    out << ileA << endl;
    out << "Punkt (b): ";
    out << ileB << endl;
    out << "Punkt (c): " << punktC()+1;
    out.close();

    return 0;
}
