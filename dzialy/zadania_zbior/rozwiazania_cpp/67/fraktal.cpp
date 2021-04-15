#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

bool pierwsza( long a) {
   if (a==1) return false;
   if (a==2 || a==3) return true;
   for (long  p=2; p<=sqrt((double)a); p++){
      if (a%p == 0) return false;
   }
    return true;
}

string bin(long a) {
    string b = "";
    while (a>0) {
        if (a%2 == 0) b = "0"+ b; else b = "1" + b;
        a /= 2;
    }
    return b;
}

int main()
{   const int n = 40;
    string B[n+1];
    B[1]= bin(1);
    B[2]= bin(1);
    long int f1=1, f2=1, f;
    
    ofstream wy_p("pierwsze.txt");
    ofstream wy_f("fibonacciego.txt");
    ofstream wy_bin("binarnie.txt");
    ofstream wy_jed("6jedynek.txt");
    ofstream wy_z("zer_bin.txt");   
    
    for (int i=3; i<=n; i++) {
        f = f1+f2;
        B[i] = bin(f);
        wy_bin << i << "\t" << bin(f) << endl;
        if (pierwsza(f)) wy_p << i << "\t" << f << endl;
        f1 = f2;
        f2 = f;
        if (i%10 == 0) wy_f << i << "\t" << f << endl;
    }

    int m = B[n].length();           //dlugosc zapisu binarnego 40. wyrazu ciagu Fib

    for (int i=1; i<=n; i++) {
        int licz1 = 0;
        string b = B[i];
        while (b.length()<m) b = "0" + b;
        for (int j=0; j<m; j++)
            if (b[j]=='0') { cout << " "; wy_z << "0";}
            else { cout << ' '; wy_z << '1'; licz1++;  }
        
        wy_z << endl;
        if (licz1 == 6) wy_jed << i << "\t" << B[i] << endl;
    }
    

    wy_p.close();
    wy_f.close();
    wy_bin.close();
    wy_jed.close();
    wy_z.close();

    cout << endl;
    cout<<"Aby zakonczyc prosze nacisnac dowolny klawisz...";
    getchar();
}
