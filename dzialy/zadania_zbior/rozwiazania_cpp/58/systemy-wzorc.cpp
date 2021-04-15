#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <time.h>
using namespace std;

#define ROZM 3*365
//#define ROZM 100
int g1[ROZM], g2[ROZM], g3[ROZM];
int t1[ROZM], t2[ROZM], t3[ROZM];
ofstream out;

string nasystem(int l,int b){
    // l - liczba
    // b -system docelowy
    string s="";
    char z;
    int znak=1;
    if (l<0) {
        znak=-1; l=-l;
    }
    if (!l) return "0";
    while (l>0){
        z=48+l%b;
        s=z+s;
        l=l/b;
    }
    if (znak<0) s='-'+s;
    return s;
}

int zsystemu(string s, int b)
{   int wynik=0, i=0, znak=1;

    if (s[0]=='-'){
        znak=-1;
        i=1;
    }
    for(;i<s.length();i++){
        wynik=wynik*b+(s[i]-48);
    }
    return znak*wynik;
}

void zad1(){
    int i;
    int min1=t1[0], min2=t2[0], min3=t3[0];

    int ile=ROZM;
    for(i=1;i<ile;i++){
        if (t1[i]<min1) min1=t1[i];
        if (t2[i]<min2) min2=t2[i];
        if (t3[i]<min3) min3=t3[i];
    }
    out << "Zad 1: " << endl;
    out << "Min temp w stacji S1: " << nasystem(min1,2) << endl;
    out << "Min temp w stacji S2: " << nasystem(min2,2) << endl;
    out << "Min temp w stacji S3: " << nasystem(min3,2) << endl;

}

void zad2(){
    int i;
    int licz=0, stan=12;

    int ile=ROZM;
    for(i=0;i<ile;i++){
        if (g1[i]!=stan && g2[i]!=stan && g3[i]!=stan)
            licz++;
        stan+=24;
    }

    out << "Zad 2: " << endl;
    out << "Liczba dni z blednymi zegarami: " << licz << endl;

}

void zad3(){
    int i;
    int min1=t1[0], min2=t2[0], min3=t3[0];
    int licz=1;
    int ileR, ile=ROZM;
    for(i=1;i<ile;i++){
        ileR=0;
        if (t1[i]>min1) { min1=t1[i]; ileR++; }
        if (t2[i]>min2) { min2=t2[i]; ileR++; }
        if (t3[i]>min3) { min3=t3[i]; ileR++; }
        if (ileR>0) licz++;
    }

    out << "Zad 3: " << endl;
    out << "Liczba rekordow: " << licz << endl;

}

void zad4(){
    int rij,j,i,mj,mi;
    int maxS=0;
    int ileR, ile=ROZM, kwadrat;
    for(i=0;i<ile;i++)
        for(j=i+1;j<ile; j++){
            kwadrat=(t1[i]-t1[j])*(t1[i]-t1[j]);
            rij=kwadrat/(j-i);
            if (rij*(j-i)<kwadrat) rij++;
            if (rij>maxS) {
                maxS=rij;
                mi=i; mj=j;
            }
        }



    out << "Zad 4: " << endl;
    out << "Najwiekszy skok: " << maxS << endl;
    //out << "Kontrolne: " << mi << " " << mj << " " << t1[mi] << " " << t1[mj] << endl;

}

int main()
{   int i, ile;
    int temp, temp2;

    srand (time(NULL));

	ifstream in1, in2, in3;

	in1.open("dane_systemy1.txt");
	in2.open("dane_systemy2.txt");
	in3.open("dane_systemy3.txt");
	out.open("wyniki_systemy.txt");


    int godz=12;
    string g, t;
    ile = ROZM;
    for( int i=0; i<ROZM; i++){
        in1 >> g >> t;
        g1[i]=zsystemu(g,2);
        t1[i]=zsystemu(t,2);
        in2 >> g >> t;
        g2[i]=zsystemu(g,4);
        t2[i]=zsystemu(t,4);
        in3 >> g >> t;
        g3[i]=zsystemu(g,8);
        t3[i]=zsystemu(t,8);
        //in2 !!!
        //cout << g << " " << t << endl;
        //cout << g1[i] <<" "<< t1[i] << endl;

        //in1 >> g1; // >> endl;
        //cout << g1 << endl;

        //godz+=24;
    }
    //cout << nasystem(15,2) << endl;
    //cout << nasystem(15,4) << endl;
    //cout << nasystem(15,8) << endl;

    zad1();
    zad2();
    zad3();
    zad4();

    in1.close();
    in2.close();
    in3.close();
    out.close();
    return 0;
}
