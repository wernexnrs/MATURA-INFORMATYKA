#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <time.h>
using namespace std;


#define ROZ 1000
long ile=5;
int licz[ROZ], mian[ROZ];
ofstream out;


bool rowny(long l1, long m1, long l2, long m2){
    return (l1*m2==l2*m1);

}

bool mniejszy(long l1, long  m1, long l2, long m2){
    return (l1*m2<l2*m1);

}

void zad1(){
    long i,minL, minM;

    minL=licz[0];
    minM=mian[0];
    for(i=1;i<ile;i++){
        if (mniejszy(licz[i],mian[i],minL,minM)){
            minL=licz[i]; minM=mian[i];
        }
        else if (rowny(licz[i],mian[i],minL,minM)){
                //cout << licz[i] << " " << mian[i]<<endl;
                if (mian[i]<minM){
                    minL=licz[i]; minM=mian[i];
                }
              }

    }
    out << "Zadanie 1:" <<" "<< minL << " " << minM << endl;


}

int nwd(int  n, int m){
    if (n<m) return nwd(m,n);
    if (m==0) return n;
    return nwd(m,n%m);
}

void zad2(){
    long i,ileN=0;

    for(i=0;i<ile;i++){
        if (nwd(licz[i],mian[i])==1)
            ileN++;
    }
    out << "Zadanie 2:" << " " << ileN << endl;


}

void zad2bis(){
    long i,j,minL, minM,d,mniejsza;
    long sumL, ileN=0;
    bool czyN;

    for(i=0;i<ile;i++){
        if (licz[i]<mian[i]) mniejsza = licz[i];
        else mniejsza = mian[i];
        j=2; czyN = true;
        while (j<=mniejsza){
            if ((licz[i]%j==0) && (mian[i]%j==0))
                czyN=false;
                j++;
        }

        if (czyN) ileN++;
    }
    out << "Zadanie 2" << " " << ileN << endl;


}


void zad3(){
    long i,minL, minM,d;
    long sumL=0, ileN=0;

    for(i=0;i<ile;i++){
        d=nwd(licz[i],mian[i]);
        sumL = sumL + licz[i]/d;
    }
    out << "Zadanie 3: " << sumL << endl;


}


void zad4(){
    long long i,mianS, liczS, nowyLicz;

    liczS=0;
    mianS=2*3*5*7*13;
    //cout << mianS << " ";
    mianS=mianS*mianS/13;
    //cout << "Zakresy! " << mianS << " " << 3000*mianS << endl;
    for(i=0;i<ile;i++){
        nowyLicz = licz[i]*mianS/mian[i];
        liczS+= nowyLicz;
    }
    out << "Zadanie 4: " << liczS << endl;

    //cout << "Licznik sumy - postac nieskracalna: " << liczS/nwd(liczS,mianS) << endl;
    //cout << "Mianownik sumy - postac nieskracalna: " << mianS/nwd(liczS,mianS) << endl;


}

int main()
{   long i;

    srand (time(NULL));

	ifstream in;

	in.open("dane_ulamki.txt");
	out.open("wyniki_ulamki.txt");

    //in.open("przyklad.txt");
    ile = 1000;
    for(i=0;i<ile;i++){
        in >> licz[i] >> mian[i];
        //cout << licz[i] << " " << mian[i] << endl;
    }

    zad1();
    zad2bis();
    zad3();
    zad4();

    out.close();
    return 0;
}
