#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<ctype.h>
using namespace std;

bool zawiera_same_cyfry(string s)
{
	for (char c : s) if ( !isdigit(c) ) return false;
	return true;
}
bool kolejne(char a,char b,char c,char d)
{
	char T[4] = { a,b,c,d }; sort(T, T+4);
	a = T[0]; b = T[1]; c = T[2]; d = T[3];
	return (a+1==b && b+1==c && c+1==d);
}
bool zawiera_4kolejne(string s)
{
	if ( s.size()<4 ) return false;
	for (unsigned int i=3; i<s.size(); i++)
		if ( kolejne(s[i-3], s[i-2], s[i-1],  s[i]) ) return true;
	return false;
}
bool zawiera_wszystko(string s)
{
	bool digit=false, az=false, AZ=false;
	for (char c : s)
		if ( '0' <= c && c <= '9' ) digit = true;
		else if ( 'a' <= c && c <= 'z' ) az = true;
		else if ( 'A' <= c && c <= 'Z' ) AZ = true;
	return digit && az && AZ;
}

vector<string> hasla;

void zadanie1()
{
	int odp = 0;
	for (string s : hasla) if ( zawiera_same_cyfry(s) ) odp++;
	cout << "--------------\nZadanie 1\n" << odp << endl;
}
void zadanie2()
{
	cout << "--------------\nZadanie 2\n";
	sort( hasla.begin(), hasla.end() );
	for (unsigned int i=0; i<hasla.size();i++)
	{
		int j = 0;
		while(i+j+1<hasla.size() && hasla[i+j+1]==hasla[i]) j++;
		if ( j )
		{
			cout << hasla[i] << endl;
			i += j;
		}
	}
}
/* 
void zadanie2p()
{
	cout << "--------------\nZadanie 2p\n";
	set<string> S, Q;
	for (string h : hasla)
		if ( S.find(h) != S.end() ) Q.insert(h);
		else S.insert(h);
	for (string h : Q)
		cout << h << endl;
}
*/
void zadanie3()
{
	int odp = 0;
	for (string s : hasla) if ( zawiera_4kolejne(s) ) odp++;
	cout << "--------------\nZadanie 3\n" << odp << endl;
}
void zadanie4()
{
	int odp = 0;
	for (string s : hasla) if ( zawiera_wszystko(s) ) odp++;
	cout << "--------------\nZadanie 4\n" << odp << endl;
}
int main()
{
	int N = 200;
	hasla.resize(N);
	for (int i=0; i<N; i++) cin >> hasla[i];
	
	zadanie1();
	zadanie2();
	zadanie3();
	zadanie4();
}
