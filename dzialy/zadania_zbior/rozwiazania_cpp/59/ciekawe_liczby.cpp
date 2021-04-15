#include<iostream>
#include<fstream>

int t[1000];
using namespace std;





void wczytaj()
{
  ifstream fin;
  fin.open("liczby.txt");
   int i;
   for(i=0; i<1000; i++)
   {   
      fin>>t[i];   
   } 
   fin.close(); 
}

bool czynniki(int liczba)//do zadania a)
//tylko 3 rozne czynniki nieparzyste w rozkladzie.

{
  int ile=0;
  int czynnik=3;
  if(liczba %2 == 0) return false;
  while (liczba>1)
  {
     if (liczba % czynnik == 0) ile++;  
     while (liczba%czynnik==0){
        liczba = liczba/czynnik;
      }   
      
      czynnik=czynnik+2;
      if (ile>3) return false;
  }     
if (ile == 3) return true; 
if (ile <3) return false;
 
}

int odwroc (int liczba) //do zadania b)
{
   int nowa=0;
    
   while(liczba>0)
   {
      nowa=10*nowa+liczba%10;
      liczba=liczba/10;               
   }    
   return nowa; 
}


int iloczyn_cyfr(int x)
{
int wynik=1;
    while (x>0)
    {
       wynik=wynik*(x%10);
       x=x/10;
    }
    return wynik;
    
}

int moc(int liczba)
{
   
    int ile=1;
    
    
    liczba=iloczyn_cyfr(liczba); //iloczyn poczatkowy
       
    while (liczba>9)
    {
       liczba=iloczyn_cyfr(liczba);
       ile++;      
     }
    return ile;
}

int zadanie_a()
{
   
   int i, liczba;
   int ile=0;
   
 
   
   for(i=0; i<1000; i++)
   {
      liczba=t[i];
      if (czynniki(liczba)==true) 
         ile++;
         
   }
   return ile;
    
    
}

int zadanie_b()
{
   int i, liczba, odwrocona, suma, ile=0;
   
   for(i=0; i<1000; i++)
   {
      liczba=t[i]; 
      odwrocona = odwroc(liczba); 
      suma=odwrocona+liczba; // najpierw odwracamy liczbe, potem liczymy sume, potem sprawdzamy palindrom...
      if (odwroc(suma)==suma){
       ile++;
        }
      
   }
  return ile;  
}

void zadanie_c(int &min, int &max, int licz[21])
{
   ifstream fin;
   int i, liczba;
   int tmp;
  
   int ile=0;
  
   min=999999999, max=10;
  
   
   for(i=0; i<1000; i++)
   {
      liczba=t[i];      
      tmp=moc(liczba);
      licz[tmp]++;
      if (tmp==1) 
      {
         if (liczba<min) min=liczba;
         if (liczba>max) max=liczba;
      }
     
   }
}


int main()
{
   
   wczytaj();
   ofstream fout;
   fout.open("wyniki_liczby.txt");
   
   fout<<"Zadanie 1: " <<endl;
   fout<<zadanie_a()<<endl;
   fout<<endl<<endl;
   
   fout<<"zadanie 2:"<<endl;
   fout<<zadanie_b()<<endl;
   fout<<endl<<endl;
   
   int licz[21]={0};
   int min; int max;
    
   zadanie_c(min, max,licz);
   fout<<"zadanie 3:"<<endl;
   fout<<"Moc   Liczba liczb"<<endl;
   for(int i=1; i<=8; i++)
      fout<<i<<"   "<<licz[i]<<endl;   
   fout<<endl;
   fout<<"Minimalna liczba o mocy jeden jest rowna: "<<min<<endl;
   fout<<"Maksymalna liczba o mocy jeden jest rowna: "<<max<<endl;
   fout.close();
   
 return 0;
    
}
