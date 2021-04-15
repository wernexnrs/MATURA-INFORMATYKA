#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <time.h>
using namespace std;


typedef struct{
    int bg;
    int end;
}Gen;
#define ROZ 1000
string genotypes[ROZ];
ofstream out;

string mut="BCDDC";
int ile;

void zad1(){
    int i,maxl=0,l,ileg=0;
    for(i=0;i<ile;i++){
        l=genotypes[i].length();
        if (l>maxl) maxl=l;
    }
    //cout << "maxl: " << maxl << endl;
    int licz[maxl+1];
    int najw=0;
    for(i=1;i<=maxl;i++) licz[i]=0;
    for(i=0;i<ile;i++){
        licz[genotypes[i].length()]++;
    }
    for(i=1;i<=maxl;i++){
        if (licz[i]>0) ileg++;
        if (licz[i]>najw) najw=licz[i];
    }

    out << "Zadanie 1: " << endl;
    out << "Liczba gatunkow: " << ileg << endl;
    out << "Rozmiar najwiekszego gatunku: " << najw << endl;

}


void zad2A(){
    int i,j, stat[5];
    char z;

    for(i=0;i<5;i++) stat[i]=0;
    for(i=0;i<ile;i++)
        for(j=0;j<genotypes[i].length();j++)
            stat[genotypes[i][j]-'A']++;
    out << "Zadanie 2A" << " " << endl;
    for(i=0;i<5;i++){
        z='A'+i;
        out << z << ": " << stat[i] << endl;
    }


}

Gen nextGen(string s, int i)
{   int len=s.length();
    //int bg=i;
    Gen pom;
    pom.bg=pom.end=len;

    while (i<len-4 && (s[i]!='A' || s[i+1]!='A'))
        i++;
    if (i>len-4) // || s[i]!='A' || s[i+1]!='A')
        return pom;
    pom.bg=i;
    while (i<len-1 && (s[i]!='B' || s[i+1]!='B'))
        i++;
    if (i==len-1) //|| s[i]!='B' || s[i+1]!='B')
        { pom.bg=len; return pom;}
    pom.end=i+1;
//    cout << "gen:" << s.substr(pom.bg,pom.end-pom.bg+1) << endl;

    return pom;
}

int ileGenow(string s)
{   Gen pom;
    int len=s.length();

    int i=0;
    int ileg=0;
    while (i<s.length()){
        pom=nextGen(s,i);
        if (pom.bg<len) ileg++;
        i=pom.end+1;
    }
    return ileg;
}

int najdluzszyGen(string s)
{   Gen pom;
    int len=s.length();

    int i=0;
    int maxL=0;
    while (i<s.length()){
        pom=nextGen(s,i);
        if (pom.bg<len)
            if (pom.end-pom.bg+1>maxL)
                maxL=pom.end-pom.bg+1;
        i=pom.end+1;
    }
    return maxL;
}

bool czyMutacjaGen(string s, int bg, int end)
{   int len = mut.length();
    if (bg<0) return false;
    while (bg<=end-len+1) {
        if (mut==s.substr(bg,len))
            return true;
        bg++;
    }
    return false;
}


bool czyMutacjaGenotyp(string s)
{
    int lenMut= mut.length();
    Gen  pom;
    bool czyM=false;

    pom.bg=0;
    int i=0;
    do{
        pom = nextGen(s,pom.bg);
        if (czyMutacjaGen(s,pom.bg,pom.end))
            return true;
        pom.bg=max(pom.bg,pom.end)+1;
    } while(pom.bg<s.length());
    return false;
}

void zad2B(){
    int ilemut=0,i,j, stat[5];
    char z;

    for(i=0;i<ile;i++)
        if (czyMutacjaGenotyp(genotypes[i])) ilemut++;
    out << "Zadanie 2B: " << ilemut << endl;

}

void zad3(){
    int maxLGenow=0,maxDlGenu=0,i,j, stat[5];
    char z;
    int LGenow, DlGenu;

    for(i=0;i<ile;i++){
        //cout << "genotyp:" << genotypes[i] << endl;
        LGenow=ileGenow(genotypes[i]);
        if (LGenow>maxLGenow) maxLGenow=LGenow;
        DlGenu=najdluzszyGen(genotypes[i]);
        if (DlGenu>maxDlGenu)
            maxDlGenu = DlGenu;
    }

        //if (czyMutacjaGenotyp(genotypes[i])) ilemut++;
        ;


    out << "Zadanie 3: " << endl;
    out << "Najwieksza liczba genow w genotypie: " << maxLGenow << endl;
    out << "Najdluzszy gen: " << maxDlGenu << endl;


}

string czescKodujaca(string s)
{   Gen pom;
    int len=s.length();
    string rob="";

    int i=0;
    while (i<s.length()){
        pom=nextGen(s,i);
        if (pom.bg<len) rob=rob+s.substr(pom.bg,pom.end-pom.bg+1);
        i=pom.end+1;
    }
    return rob;
}

bool palindrom(string s){
    int len = s.length();
    for(int i=0;i<len/2;i++)
        if (s[i]!=s[len-1-i]) return false;
    return true;
}

string odwroc(string s)
{
    string rob="";
    for(int i=0;i<s.length();i++)
        rob=s[i]+rob;
    //cout << "odwroc : " << rob << endl;
    return rob;
}

void zad4(){
    int i,ileOdp=0,ileSOdp=0;
    string rob, rob2;

    for(i=0;i<ile;i++){
        //cout << "genotyp:" << genotypes[i] << endl;
        if (palindrom(genotypes[i])) ileSOdp++;
        rob = czescKodujaca(genotypes[i]);
        rob2 = czescKodujaca(odwroc(genotypes[i]));
        //cout << "czesc kodujaca: " << rob;
        if (rob==rob2) ileOdp++;
    }

        //if (czyMutacjaGenotyp(genotypes[i])) ilemut++;
        ;


    out << "Zadanie 4: " << endl;
    out << "Liczba odpornych: " << ileOdp << endl;
    out << "Liczba silnie odpornych: " << ileSOdp << endl;


}

int main()
{   long long i;

    srand (time(NULL));

	ifstream in;

	in.open("dane_geny.txt");
	out.open("wyniki_geny.txt");

    //ile = 4;
    ile=ROZ;
    for(i=0;i<ile;i++){
        in >> genotypes[i];
        //cout << genotypes[i] << endl;
    }

    zad1();
    //zad2A();
    zad2B();
    zad3();
    zad4();

    out.close();
    return 0;
}
