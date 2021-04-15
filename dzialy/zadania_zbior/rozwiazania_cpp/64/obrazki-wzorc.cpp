#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <time.h>
using namespace std;

#define ROZM 20
#define SIZE 200

typedef short obrazek[ROZM+1][ROZM+1];
ifstream in;
ofstream out;

obrazek gobraz;
struct korekta{
    int numerObrazka;
    int wiersz;
    int kolumna;};

struct korekta jakKorygowac[SIZE];

int ileCzarnych(obrazek pobraz){
    int i,j,czarne=0;

    for(i=0;i<ROZM;i++){
        for(j=0;j<ROZM;j++){
            czarne+=pobraz[i][j];
        }
    }
    return czarne;

}

int stanPoprawnosci(obrazek pobraz){
    // 0 poprawny
    // 1 naprawialny
    // >1 nienaprawialny, wynik to liczba blednych parzystosci
    int i,j,parzw,parzk;
    int ileBlWiersz, ileBlKol;

    ileBlWiersz=0;
    ileBlKol=0;
    for(i=0;i<ROZM;i++){
        parzw=parzk=0;
        for(j=0;j<ROZM;j++){
            parzw=parzw+pobraz[i][j];
            parzk=parzk+pobraz[j][i];
        }
        if ((parzw%2)!=pobraz[i][ROZM]) ileBlWiersz++;
        if ((parzk%2)!=pobraz[ROZM][i]) ileBlKol++;
    }

    if (ileBlWiersz+ileBlKol==0) return 0;
    if (ileBlWiersz<=1 && ileBlKol<=1) return 1;
    return ileBlWiersz+ileBlKol;

}

/* OLD
int stanPoprawnosci(obrazek pobraz){
    // 0 poprawny
    // 1 naprawialny
    // >1 nienaprawialny, wynik to liczba blednych parzystosci
    int i,j,parzw,parzk[ROZM];
    int ileBlWiersz, ileBlKol;

    ileBlWiersz=0;
    ileBlKol=0;
    for(i=0;i<ROZM;i++) parzk[i]=0;
    for(i=0;i<ROZM;i++){
        parzw=0;
        for(j=0;j<ROZM;j++){
            parzw=parzw+pobraz[i][j];
            parzk[j]=parzk[j]+pobraz[i][j];
        }
        if ((parzw%2)!=pobraz[i][ROZM]) ileBlWiersz++;
    }
    for(j=0;j<ROZM;j++)
        if (pobraz[ROZM][j]!=(parzk[j]%2)) ileBlKol++;

    if (ileBlWiersz+ileBlKol==0) return 0;
    if (ileBlWiersz<=1 && ileBlKol<=1) return 1;
    return ileBlWiersz+ileBlKol;

}
*/
struct korekta korygujObrazek(obrazek pobraz){
    int i,j,parzw,parzk;
    struct korekta wynik;

    wynik.wiersz=ROZM+1;
    wynik.kolumna=ROZM+1;
    for(i=0;i<ROZM;i++){
        parzw=parzk=0;
        for(j=0;j<ROZM;j++){
            parzw=parzw+pobraz[i][j];
            parzk=parzk+pobraz[j][i];
        }
        if ((parzw%2)!=pobraz[i][ROZM])
            wynik.wiersz=i+1;
        if ((parzk%2)!=pobraz[ROZM][i])
            wynik.kolumna=i+1;
    }
    return wynik;
}

/*void skoryguj(obrazek pobraz){
    // 0 poprawny
    // 1 naprawialny
    // 2 nienaprawialny
    int i,j,parzw,parzk[ROZM];
    int ileBlWiersz=0, ileBlKol=0;
    int BlednyWiersz=-1, BlednaKol=-1;

    for(i=0;i<ROZM;i++) parzk[i]=0;
    for(i=0;i<ROZM;i++){
        parzw=0;
        for(j=0;j<ROZM;j++){
            parzw+=pobraz[i][j];
            parzk[j]=parzk[j]+pobraz[i][j];
        }
        if ((parzw%2)!=pobraz[i][ROZM]) {
                ileBlWiersz++; BlednyWiersz=i;
        }
    }
    for(i=0;j<ROZM;j++)
        if (pobraz[ROZM][j]!=(parzk[j]%2)) {
                ileBlKol++; BlednaKol=j;
    }
    if (ileBlWiersz+ileBlKol>0){
        if (ileBlWiersz<=1 && ileBlKol<=1) {
            out << "Pozycja do skorygowania: ";
            if (BlednyWiersz>=0 && BlednaKol >=0 )
                out << BlednyWiersz+1 << " " << BlednaKol << endl;
            else if (BlednyWiersz>=0)
                    out << BlednyWiersz+1 << " " << ROZM+1 << endl;
                 else out << ROZM+1 << " " << BlednaKol+1 << endl;
        }

    }

}
*/

void czytajObrazek(obrazek pobraz)
{
    int i,j,sum,bit, dl;
    char znak;

    for(i=0;i<ROZM+1;i++){
        if (i<ROZM) dl=ROZM+1;
        else dl=ROZM;
        for(j=0;j<dl;j++){
            in >> znak;
            pobraz[i][j]=znak-'0';
        }
    }
//    in >> endl;

    /*cout << endl;
    for(i=0;i<ROZM+1;i++){
        if (i<ROZM) dl=ROZM+1;
        else dl=ROZM;
        for(j=0;j<dl;j++)
            cout << pobraz[i][j];
        cout << endl;
    }
    cout << endl;
    */
}


void wypiszObraz(obrazek wobraz){
    int i,j;

    for(i=0;i<ROZM;i++)
    {
        for(j=0;j<ROZM;j++)
            out << wobraz[i][j];
        out << endl;
    }
}

void kopiujObraz(obrazek iobraz, obrazek oobraz){
    int i,j;

    for(i=0;i<ROZM;i++)
    {
        for(j=0;j<ROZM;j++)
            oobraz[i][j]=iobraz[i][j];

    }
}

bool czyRek(obrazek robraz){
    int i,j,shift=ROZM/2;

    for(i=0;i<ROZM/2;i++)
        for(j=0;j<ROZM/2;j++){
            if (robraz[i][j]!=robraz[i+shift][j]) return false;
            if (robraz[i][j]!=robraz[i][j+shift]) return false;
            if (robraz[i][j]!=robraz[i+shift][j+shift]) return false;
    }

    return true;
}
int main()
{   int i,nRewers=0, maxCzarnych=0, lCzarnych;
    int lPopr=0, lNapr=0,st;
    obrazek mojeobrazy[SIZE],rekobraz;


    srand (time(NULL));

	in.open("dane_obrazki.txt");
	out.open("wyniki_obrazki.txt");


    int gdzieRek=-1;
    int ileRek=0;
    int maxLBledow=0;
    for( int i=0; i<SIZE; i++){
        czytajObrazek(mojeobrazy[i]);
        lCzarnych=ileCzarnych(mojeobrazy[i]);
        if (czyRek(mojeobrazy[i])){
            ileRek++;
            if (gdzieRek<0) {
                gdzieRek=i; //kopiujObraz(mojobraz,rekobraz);

            }
        }
        if (lCzarnych>ROZM*ROZM/2)
            nRewers++;
        if (lCzarnych>maxCzarnych)
            maxCzarnych=lCzarnych;
        st=stanPoprawnosci(mojeobrazy[i]);
        switch (st){
            case 0: lPopr++;
                    break;
            case 1: jakKorygowac[lNapr]=korygujObrazek(mojeobrazy[i]);
                    jakKorygowac[lNapr].numerObrazka=i+1;
                    lNapr++;
                    break;
            default:
                    if (maxLBledow<st) maxLBledow=st;
                    break;
        }

    }

    //zad1
    out << "Zadanie 1: " << endl;
    out << "Liczba rewersow: " << nRewers << endl;
    out << "Najwieksza liczba pikseli czarnych: " << maxCzarnych << endl;

    //zad2
    out << "Zadanie 2: " << endl;
    out << "Liczba rekurencyjnych: " << ileRek << endl;
    out << "Pierwszy rekurencyjny: " << endl;
    wypiszObraz(mojeobrazy[gdzieRek]);

    //zad3
    out << "Zadanie 3: " << endl;
    out << "Liczba poprawnych: " << lPopr << endl;
    out << "Liczba naprawialnych: " << lNapr << endl;
    out << "Liczba nienaprawialnych: " << SIZE-lPopr-lNapr << endl;
    out << "Najwieksza liczba blednych parzystosci: " << maxLBledow << endl;


    //zad 4
    out << "Zadanie 4: " << endl;
    out << "Obrazki naprawialne (numer obrazka, wiersz, kolumna):" << endl;
    for(i=0;i<lNapr;i++){
        out << "(" << jakKorygowac[i].numerObrazka << ",";
        out << jakKorygowac[i].wiersz << ",";
        out << jakKorygowac[i].kolumna << ")" << endl;
    }


    out.close();
    return 0;
}
