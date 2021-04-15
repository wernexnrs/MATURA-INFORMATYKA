#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string ciagi[1000];


void wczytaj(string ciagi[1000])
{
int i;
ifstream fin;
fin.open("ciagi.txt");
for(i=0; i<1000; i++)
{
   fin>>ciagi[i];
}
fin.close();
}


bool dwucykliczny(string ciag)
{
int j;
int d=ciag.length();
for (j=0; j<d/2; j++)
   if (ciag[j]!=ciag[d/2+j]) return false;
return true;
}


bool dwie_jedynki(string ciag)
{
int i;
for (i=0; i<ciag.length()-1; i++)
   if  (ciag[i]=='1' && ciag[i+1]=='1') return false;
return true;
}

long long int bin2wart(string bin)
{
long long int w=0;

for(int i=0; i<bin.length(); i++)
   w=w*2+(bin[i]-'0');
return w;

}

bool czy_pierwsza(long long int x)
{
     if (x==1) return false;
     if (x%2 == 0 && x!=2) return false;
     for(long long int i=3; i*i<=x; i+=2)
        if (x%i == 0) return false;
     return true;


     }

bool czy_polpierwsza(long long int x)
{
for (long long int j=1; j<=x; j++)
   if (x%j == 0 && czy_pierwsza(j) && czy_pierwsza(x/j))
       return true;
return false;
}

bool czy_polpierwsza2(long long int x)
{
int ile=0;
int i=2;
while (x>1)
{
      if (x%i==0){
        ile++;
        x=x/i;
        if (ile>2) return false;
      }
      else i++;
}
if (ile==1) return false;
return true;
}

bool czy_polpierwsza1(long long int x)
{    if (czy_pierwsza(x)) return false;
     if (x%2==0) return (czy_pierwsza(x/2));
     for (long long j=3; j*j<=x; j+=2)
          if (x%j==0) return (czy_pierwsza(x/j));
}


int main(){


wczytaj(ciagi);

ofstream fout;
fout.open("wyniki_ciagi.txt");


int i,j;
//zadanie 1
fout<<"Zadanie 1"<<endl;
for(i=0; i<1000; i++)
{

   if (ciagi[i].length()%2==0 && dwucykliczny(ciagi[i]))
      fout<<ciagi[i]<<endl;
}
fout<<endl;
//zadanie 2

int ile=0;
for (i=0; i<1000; i++)
{
    if (dwie_jedynki(ciagi[i])) ile++;
}
fout<<"Zadanie 2"<<endl;
fout<<ile;
fout<<endl;

//Zadanie 3
long long int min, max, liczba;
j=0;
bool wystepuje=false;
while(j<1000 && (!wystepuje)){
   liczba = bin2wart(ciagi[j]);
   if (czy_polpierwsza(liczba)){
      wystepuje=true;
      min=max=liczba;
   } else j++;
}
ile=0;

for(int i=j; i<1000; i++)
{
   liczba = bin2wart(ciagi[i]);
   if (czy_polpierwsza(liczba))
   {
      ile++;
      if (liczba>max) max = liczba;
      if (liczba<min) min = liczba;
   }
}


fout<<"Zadanie 3"<<endl;
fout<<"Liczb polpierwszych jest "<<ile<<endl;
fout<<"Min = "<<min<<endl;
fout<<"Max = "<<max<<endl;

fout.close();
cout<<endl<<endl;


    return 0;
}


