#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string Vigenere(string tresc, string klucz, bool szyfruj) {
    int n = tresc.length();
    cout << "dlugosc tekstu = " << n << endl;
    int nk = klucz.length();

    // odwzorowanie klucza dla calej tresci
    string q = "";
    int powtorzenia = 1;
    int j = 0;
    for (int i=0; i<n; i++) {
        char c = tresc[i];
        if (c>='A' && c<='Z') {
            c = klucz[j];
            j++;
            if (j==nk) { j=0; powtorzenia++; }
        }
        q += c;
    }
    cout << powtorzenia <<" powtorzenia klucza\n";

    // kodowanie lub dekodowanie
    string t="";
    for (int i=0; i<n; i++) {
        char c = tresc[i];
        if (c>='A' && c<='Z') {
            int k = q[i]-int('A');
            if (szyfruj) {          // szyfruj
                c += k;
                if (c>'Z') c -=26;
            }
            else {                  // deszyfruj
                c -= k;
                if (c<'A') c +=26;
            }
        }
        t += c;
    }
    return t;
}

int main()
{
    // zadanie 1
    string s;
    ifstream we("dokad.txt");
    getline(we,s);
    we.close();
    string klucz = "LUBIMYCZYTAC";
    cout << Vigenere(s,klucz,true) << endl;

    // zadanie 2
    we.open("szyfr.txt");
    getline(we,s);
    getline(we,klucz);
    we.close();
    cout << Vigenere(s,klucz,false) << endl;

    // zadanie 3
    int L[26];                      // liczniki wystapien liter
    for (int j=0; j<26; j++) L[j]=0;
    int n = 0;                      // liczba wszystkich liter
    for (int i=0; i<s.length(); i++) {
        if (s[i]>='A' && s[i]<='Z') {
            int j = s[i] - 'A';
            L[j]++;
            n++;
        }
    }

    cout << n << " liter w tresci szyfru\n";
    cout << "Liczniki wystapien liter:\n";
    for (int j=0; j<26; j++)
        cout << char(j+'A') << " - " << L[j] << endl;;

    int suma = 0;
    for (int j=0; j<26; j++) suma += L[j]*(L[j]-1);
    double ko = (double)suma/n/(n-1);
    double d = 0.0285/(ko-0.0385);

    d += 0.005;             // w celu zaokraglenia do 2 cyfr dziesietnych
    d = 0.01*int(100*d);
    cout << d << " - szacunkowa dlugosc klucza\n";
    cout << klucz.length() << " - dokladna dlugosc klucza\n";

    return 0;
}
