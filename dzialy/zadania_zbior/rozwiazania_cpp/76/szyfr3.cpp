#include<cstdio>
#include<string>
#include<iostream>
#include<cassert>
using namespace std;

int n=6, P[6]  = {6, 2, 4, 1, 5, 3};

string deszyfr(string A)
{
    for (int i=A.size()-1; i>=0; i--)
        swap(A[i], A[P[i%n]-1]);
    return A;
}

int main()
{
	string tekst;
    cin >> tekst;
    cerr << "Dlugosc tekstu = " << tekst.size() << endl;
    cout << deszyfr( tekst ) << endl;
}

