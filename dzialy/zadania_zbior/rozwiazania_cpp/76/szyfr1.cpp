#include<cstdio>
#include<string>
#include<iostream>
#include<cassert>
using namespace std;

int n, P[50];

string szyfr(string A)
{
    for (int i=0; i<A.size(); i++) swap(A[i], A[P[i%n]-1]);
    return A;
}

int main()
{
	n = 50;
	string tekst[6];
    for (int i=0; i<6; i++) cin >> tekst[i];
    //cerr << "Dlugosc tekstu = " << tekst.size() << endl;
    for (int i=0; i<n; i++) cin >> P[i];
    for (int i=0; i<6; i++) cout << szyfr( tekst[i] ) << endl;
}
