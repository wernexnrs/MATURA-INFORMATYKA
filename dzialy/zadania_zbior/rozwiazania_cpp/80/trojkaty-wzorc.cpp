#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <time.h>
using namespace std;


#define ROZ 1000
int ile;
int boki[ROZ];
ofstream out;


bool trojkat(int a, int b, int c)
{
    return ((a+b>c)&&(a+c>b)&&(b+c>a));
}

bool prost(int a, int b, int c)
{   int d;

    if (a<b) {d=b; b=a; a=d;}
    if (a<c) {d=c; c=a; a=d;}

    return (c*c+b*b==a*a);
}

void zad1(){
int ileP=0;

out << "Zadanie 1: ";
for(int i=0; i<ile-2;i++)
    if (prost(boki[i],boki[i+1],boki[i+2])){
        out << boki[i]<< ", " << boki[i+1]<<", "<<boki[i+2]<<";  ";
    }
out << endl;

}

void zad2(){
    int maxObw=0;
    int i, j, k, pom, obwod;

    for (i=ile-1;i>0;i--)
        for (j=0;j<i;j++)
            if (boki[j]>boki[j+1]){
                pom=boki[j];boki[j]=boki[j+1]; boki[j+1]=pom;
            }

    //for(i=0;i<ile;i++) cout << boki[i] << " ";
    bool brak = true;
    i=ile;
    while(brak && i>1){
        i--;
        if (trojkat(boki[i],boki[i-1],boki[i-2]))
            brak=false;
    }

    maxObw = boki[i]+boki[i-1]+boki[i-2];
    out << "Zadanie 2: " << maxObw << endl;
    //out << boki[i]<<" "<<boki[i-1]<<" "<<boki[i-2] << endl;


}



void zad3(){
    int i,j,k,ileT=0;

    for (i=0;i<ile-2;i++)
        for (j=i+1;j<ile-1;j++)
            for (k=j+1;k<ile;k++){
                if (trojkat(boki[i],boki[j],boki[k])){
                    ileT++;
                    //cout << ileT << ":" << boki[i] << " "<< boki[j]<< " " << boki[k] << endl;
                }
            }

    out << "Zadanie 3: " << ileT << endl;

}


int main()
{   int i,j,k;


    srand (time(NULL));

	ifstream in;
    //in.open("przyklad_trojkaty.txt");
	in.open("dane_trojkaty.txt");
	out.open("wyniki_trojkaty.txt");

    ile = 500;
    for(i=0;i<ile;i++){
        in >> boki[i];
        //cout << boki[i] << " " << mian[i] << endl;
    }



    zad1();
    zad2();
    zad3();

    out.close();
    return 0;
}
