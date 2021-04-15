#include <cstdlib>
#include <iostream>


using namespace std;


int pierwsza(int k)
{
 int i=2, wyn=1;
 if (k==1) return 0;
 while((i*i<=k)&& wyn) 
 {
  if (k%i==0) wyn=0;
  i++;
 }
 return wyn;
}

int suma_cyfr(int a)
{int suma=0;
while (a>0) {suma=suma+a%10;a=a/10;}
return(suma);
}

int czy_prostokatny(int a, int b, int c)
{
    return(((a*a+b*b)==c*c)||((a*a+c*c)==b*b)||((c*c+b*b)==a*a));
}

/*int czy_prostokatny(int a, int b, int c)
{
    return((a*a+b*b)==c*c);
}*/

int czy_trojkat(int a, int b, int c)
{
    return((a+b>c)&&(b+c>a)&&(a+c>b));
}

int zadanie1()
{
 int i, liczba1, liczba2, liczba3;
 for (i=1; i<=1000; i++)
 {
  scanf("%i %i %i\n",&liczba1, &liczba2, &liczba3);
  if ((suma_cyfr(liczba1)+suma_cyfr(liczba2))==liczba3) printf("%i %i %i\n",liczba1, liczba2, liczba3); 
 }
}

int zadanie2()
{
 int i, liczba1, liczba2, liczba3;
 for (i=1; i<=1000; i++)
 {
  scanf("%i %i %i\n",&liczba1, &liczba2, &liczba3);
  if ((liczba1*liczba2)==liczba3) {if (pierwsza(liczba1)&&pierwsza(liczba2)) printf("%i %i %i\n",liczba1, liczba2, liczba3);} //
 }
}

int zadanie3()
{
 int i, liczba1, liczba2, liczba3, poprzedni=0, aktualny=0, pop1, pop2, pop3;
 for (i=1; i<=1000; i++)
 {
  scanf("%i %i %i\n",&liczba1, &liczba2, &liczba3);
  aktualny=czy_prostokatny(liczba1, liczba2, liczba3);
  if (poprzedni&&aktualny) {printf("%i %i %i\n",pop1, pop2, pop3);printf("%i %i %i\n\n",liczba1, liczba2, liczba3);} // 
  poprzedni=aktualny;
  pop1=liczba1; pop2=liczba2; pop3=liczba3;
 }
}

int zadanie4()
{
 int i, liczba1, liczba2, liczba3,  licznik=0,  dlugosc=0, max=0;
 for (i=1; i<=1000; i++)
 {
  scanf("%i %i %i\n",&liczba1, &liczba2, &liczba3);
  if (czy_trojkat(liczba1, liczba2, liczba3)) 
    {dlugosc++; licznik++;}
  else 
    {if (dlugosc>max)max=dlugosc;dlugosc=0;}
 }
 printf("Liczba trojek reprezentujacych dlugosci bokow trojkata %i\n",licznik);
 printf("Dlugosc nadluzszego ciagu trojkatnego: %i\n", max);
}

int main(int argc, char *argv[])
{
  zadanie1();
 //zadanie2();
 //zadanie3();
 //zadanie4(); 
 //system("PAUSE");
 return EXIT_SUCCESS;
}
