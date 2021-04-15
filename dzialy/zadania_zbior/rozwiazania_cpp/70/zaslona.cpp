#include <iostream>
#include <cmath>
#include <stdio.h>

using namespace std;

double f(double x)
{
   return (pow(x,4)/500-pow(x,2)/200-0.012);
}

double g(double x)
{
   return (-x*x*x/30+x/20+1.0/6);
}

double pole(double a, double b, double blad)
{
double pfgora=0, pfdol=0, pf;
double pggora=0, pgdol=0, pg;
double x,h;
int n=10;
//pole f
do{
  h=(b-a)/n; x=a;
  pfdol=pfgora=0;
  for(int i=0; i<n; i++)
  {
      pfdol=pfdol+f(x);
      x=x+h;
      pfgora=pfgora+f(x);
  }
  pfgora=pfgora*h;
  pfdol=pfdol*h;
  n=2*n;
}while (pfgora-pfdol>blad/2);
pf=(pfgora+pfdol)/2;
//pole g
x=a; n=10;
do{
  h=(b-a)/n; x=a;
  pgdol=pggora=0;
  for(int i=0; i<n; i++)
  {
      pgdol=pgdol-g(x);
      x=x+h;
      pggora=pggora-g(x);
  }
  pggora=pggora*h;
  pgdol=pgdol*h;
  n=2*n;
} while (pggora-pgdol>blad/2);
pg=(pggora+pgdol)/2;
return (pf+pg);
}


double dlugosc(double a, double b, double n)
{
double d=0;

d=d+16+f(10)-g(10);
double h = 1.0*(b-a)/n;
int i;
double x=a;
double tmp;
//dlugosc luku f

for (i=0; i<=n-1; i++)
{
       tmp=sqrt(h*h+(f(x+h)-f(x))*(f(x+h)-f(x)) ); //fragment luku
       d=d+tmp;//nowa dlugosc
       x=x+h; //zmiana x_i
}

//dlugosc luku g
x=a;
for (i=0; i<=n-1; i++)
{
       tmp=sqrt(h*h+(g(x+h)-g(x))*(g(x+h)-g(x)) ); //fragment luku
       d=d+tmp;//nowa dlugosc
       x=x+h; //zmiana x_i
}

return d;
}


double zadanie3()
{
     double d=0;
     for (double x=2; x<=9.75; x=x+0.25)
        d=floor(d+(f(x)-g(x)));
     return d;
}

int main()
{

 double a=2;
 double b=10;
 double blad=0.001;
 int n=1000;
 cout<<"Powierzchnia pozostalego materialu: "<<pole(a,b,blad)<<endl;
 cout<<"Powierzchnia pozostalego materialu: "<<pole(a,b,blad)-117.705<<endl;
 printf("%f\n",pole(a,b,blad));
 cout<<"Dlugosc tasmy: "<<dlugosc(a,b,n)<<endl;
 cout<<"Suma dlugosci pasow: " <<zadanie3()<<endl;
// system("PAUSE");
 return 0;




}
