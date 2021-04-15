/**
    Wiazka zadan. Okregi.
    Autor: Rafal Nowak

    Uruchomienie:
        okregi.exe < okregi.txt
*/
#include<cmath>
#include<iostream>
using namespace std;

const int N = 2000;
double x[N], y[N], r[N];

/* funkcja sprawdza, w ktorej cwiartce znajduje sie okrag (x,y,r) */
int cwiartka(double x, double y, double r)
{
    if ( r <= 0.0 ) return 0;
    if ( r >= fabs(x) || r >= fabs(y) ) return 0;
    if ( x > 0 && y > 0 ) return 1;
    if ( x < 0 && y > 0 ) return 2;
    if ( x < 0 && y < 0 ) return 3;
    return 4;
}

void zadanie1()
{
    int p[5] = { 0,0,0,0,0 };
    for (int i=0; i<N; i++)
        p[ cwiartka(x[i],y[i],r[i]) ]++;

    cout << "------------------\nZadanie 1\n";
    for (int i=1; i<=4; i++)
        cout << "Cwiartka " << i << " : " << p[i] << "\n";
    cout << "pozostale okregi : " << p[0] << "\n";
}

bool czyParaLustrzana(double x1, double y1, double r1, double x2, double y2, double r2)
{
    if ( r1 != r2 ) return false;
    if ( x1 == x2 && y1 == -y2 ) return true;
    if ( y1 == y2 && x1 == -x2 ) return true;
    return false;
}

void zadanie2()
{
    int ilePar = 0;
    for (int i=1; i<N; i++)
        for (int j=0; j<i; j++)
            if ( czyParaLustrzana( x[i], y[i], r[i], x[j], y[j], r[j] ) ) ilePar++;

    cout << "------------------\nZadanie 2\n";
    cout << "Liczba lustrzanych par : " << ilePar << "\n";
}

bool czyParaProstopadla(double x1, double y1, double r1, double x2, double y2, double r2)
{
    if ( r1 != r2 ) return false;

    double nx1 = -y1, ny1 = x1;
    double nx2 = -y2, ny2 = x2;

	if ( nx1 == x2 && ny1 == y2 ) return true;
	if ( nx2 == x1 && ny2 == y1 ) return true;

    return false;
}

void zadanie3()
{
    int ilePar = 0;
    for (int i=1; i<N; i++)
        for (int j=0; j<i; j++)
            if ( czyParaProstopadla( x[i], y[i], r[i], x[j], y[j], r[j] ) ) ilePar++;
    cout << "------------------\nZadanie 3\n";
    cout << "Liczba par prostopadlych : " << ilePar << "\n";
}

// prawidlowe sprawdzanie przecinania sie okregow
bool czySiePrzecinaja(double x1, double y1, double r1, double x2, double y2, double r2)
{
    double D = sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) );
    if ( r1+r2 >= D && fabs(r1-r2) <= D )
        return true;
    return false;
}

// drugi prawidlowy sposob sprawdzania
bool czySiePrzecinaja_ok(double x1, double y1, double r1, double x2, double y2, double r2)
{
	//cout << "1 : " << x1 << " " << y1 << " " << r1 << endl;
	//cout << "2 : " << x2 << " " << y2 << " " << r2 << endl;
	double D = sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) );
    //cout << "D = " << D << endl;

	if ( D <= r1 ) // czy (x2,y2) jest w srodkku okregu (x1,y1,r1)
	    return D + r2 >= r1 && D + r1 >= r2;
    else
        return D-r1 <= r2 && r2 <= D+r1;
    return false;
}

// zle sprawdzanie przecinania sie okregow
bool czySiePrzecinaja_zle(double x1, double y1, double r1, double x2, double y2, double r2)
{
    double D = sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) );
    if ( D <= r1 + r2 )
        return true;
    return false;
}


void zadanie4()
{
    cout << "------------------\nZadanie 4\n";
    int n = 1000;
    int dlugosc = 1, max_dlugosc = 1;
    for (int i=1; i<n; i++)
    //for (int i=203; i<204; i++)
    {
        if ( czySiePrzecinaja( x[i], y[i], r[i], x[i-1], y[i-1], r[i-1] ))
        {
			dlugosc = dlugosc + 1;
			//cout << "TAK\n";
		}
        else
        {
            if ( max_dlugosc < dlugosc ) max_dlugosc = dlugosc;
            cout << "Dlugosc kolejnego lancucha = " << dlugosc << "\n";
            dlugosc = 1;
            //cout << "i = " << i << "\n";
        }
    }
    if ( max_dlugosc < dlugosc ) max_dlugosc = dlugosc;
            cout << "Dlugosc kolejnego lancucha = " << dlugosc << "\n";
    cout << "Dlugosc najdluzszego lancucha = " << max_dlugosc << "\n";
}


int main()
{
   for (int i=0; i<N; i++) cin >> x[i] >> y[i] >> r[i];

    zadanie1();
    zadanie2();
    zadanie3();
    zadanie4();
}
