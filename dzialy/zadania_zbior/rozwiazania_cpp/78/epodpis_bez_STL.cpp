#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool pierwsza = true;

ifstream we1("wiadomosci.txt");
ifstream we2("podpisy.txt");
ofstream wy("epodpis_wynik.txt");

string skrot(string t) {
   string S = "ALGORYTM";
   while (t.length()%8 !=0) t += '.';
   int n = t.length();
   if (pierwsza) wy << "Dlugosc pierwszej wiadomosci = " << n << endl;
   int i=0;
   while (i<n) {
        for (int j=0; j<8; j++) {
           S[j] = (S[j]+t[i]) %128;
           i++;
        }
   }
   if (pierwsza) {
        wy << "Bajty pierwszej wiadomosci po przetworzeniu: ";
        for (int j=0; j<8; j++) wy << (int)S[j] << " ";
        wy << endl;
   }
   for (int j=0; j<8; j++)
        S[j] = 65 + S[j]%26;
   if (pierwsza) {
        wy << "Skrot pierwszej wiadomosci = " << S << endl << endl;
        pierwsza = false;
   }
   return S;
}

int main()
{
    string t;
    string s, mojSkrot;
    int x,y;
    int n =200 , d = 3;

    bool W[12];  // numery wiarygodnych informacji
    for (int i=1; i<=11; i++) W[i] = false;

    for (int i=1; i<=11; i++) {

        getline(we1,t);
        s = skrot(t);

        mojSkrot = "";
        for (int j=0; j<8; j++) {
           we2 >> y;
           x = (y*d) % n;
           mojSkrot += (char)x;
        }
        wy << i << "\t" << mojSkrot << "\t";
        if (s==mojSkrot) {
                wy << "wiarygodna\n";
                W[i] = true;
        }
        else wy << "zmieniona\n";
    }

    wy << "\nNumery wiarygodnych wiadomosci: ";
    for (int i=1; i<=11; i++)
       if (W[i]) wy << i << " ";

    we1.close();
    we2.close();
    wy.close();

    return 0;
}
