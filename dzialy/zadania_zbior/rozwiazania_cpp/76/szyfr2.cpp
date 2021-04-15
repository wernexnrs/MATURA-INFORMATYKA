#include<cstdio>
#include<string>
#include<iostream>
#include<cassert>
using namespace std;

const int n=15;
int P[n];

string szyfr(string A)
{
    for (int i=0; i<A.size(); i++) swap(A[i], A[P[i%n]-1]);
    return A;
}

int main()
{
	string tekst;
    cin >> tekst;
    cerr << "Dlugosc tekstu = " << tekst.size() << endl;
    for (int i=0; i<n; i++) cin >> P[i];
    cout << szyfr( tekst ) << endl;
}
