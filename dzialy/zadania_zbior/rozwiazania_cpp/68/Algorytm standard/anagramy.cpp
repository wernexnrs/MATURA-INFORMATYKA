#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
using namespace std;

//typedef czestosc int;
string s1[1000], s2[1000];
int c1[1000][10], c2[1000][10];
int maxPowt=0;

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
        for(j=0;j<dokad;j++){ // zliczanie anagramow s1[i]
            if (czyAnag(c,c1[j])) ile++;
            if (czyAnag(c,c2[j])) ile++;
        }
        return ile;

}

void punktC()
{   int ilePowt, maxIndeks=-1;
    string s;
    int i, j;

    for(i=0; i<1000; i++){
        ilePowt=puntkCPom(c1[i],i+1); //tylko do i-tego wiersza
        if (ilePowt>maxPowt) {
                maxPowt=ilePowt; maxIndeks=i;
        }

        ilePowt=puntkCPom(c2[i],i+1);
        if (ilePowt>maxPowt) {
                maxPowt=ilePowt; maxIndeks=i+1000;
        }
//    return maxPowt;

    }


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
	for (int i=0; i<1000; i++)
	{
		in >> s1[i];
        in >> s2[i];
        //cout << "1" << s1[i] << "***" <<s2[i]<< endl;
        zamien(s1[i],c1[i]);
        zamien(s2[i],c2[i]);
        if (czyAnag(c1[i],c2[i])) ileB++;
        if (jednolity(s1[i]) && jednolity(s2[i]))
            if (s1[i][0]==s2[i][0] && s1[i].length()==s2[i].length())
            {
                ileA++;
                //cout << i << " " << s1[i] << " " << s2[i];
                //cout << " " << s1[i].length() << " " << s2[i].length() << endl;
            }
	}

    out << "Punkt (a): ";
    out << ileA << endl;
    out << "Punkt (b): ";
    out << ileB << endl;
    out << "Punkt (c): ";
    punktC();
    out << maxPowt << endl;


//    system ("pause");
    return 0;
}
