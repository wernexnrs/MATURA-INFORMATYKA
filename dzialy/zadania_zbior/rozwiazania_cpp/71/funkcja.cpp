#include<cstdio>
using namespace std;

double a[5][4];

double f(double x)
{
	if (x<1.0) return ((a[0][3]*x+a[0][2])*x+a[0][1])*x+a[0][0];
	if (x<2.0) return ((a[1][3]*x+a[1][2])*x+a[1][1])*x+a[1][0];
	if (x<3.0) return ((a[2][3]*x+a[2][2])*x+a[2][1])*x+a[2][0];
	if (x<4.0) return ((a[3][3]*x+a[3][2])*x+a[3][1])*x+a[3][0];
	return            ((a[4][3]*x+a[4][2])*x+a[4][1])*x+a[4][0];
}

void zadanie1()
{
	printf("-----------------------\nZadanie 1\n");
	printf("f(1.5) = %.5lf\n", f(1.5));
}	

double mx, mfx;
void maksimum(double from, double to, double step)
{
	double x = from;
	mx=x; mfx = f(mx);
	for (x = from+step; x<to; x+=step)
	{
		double fx = f(x);
		if ( fx > mfx )
		{
			mx = x;
			mfx = fx;
		}
	}
}

void zadanie2()
{
	printf("-----------------------\nZadanie 2\n");
	maksimum(4.0, 4.5, 0.0000001);
	printf("Rozwiazanie z duza precyzja:\nx = %.5lf\nf(x)=%.5lf\n", mx, mfx);
/*
TEST: f(   4.092)=3.06495
TEST: f(   4.093)=3.06495
*/
	double x;
	x = 4.090; fprintf(stderr, "TEST: f(%8.3lf)=%.5lf\n", x, f(x));
	x = 4.091; fprintf(stderr, "TEST: f(%8.3lf)=%.5lf\n", x, f(x));
	x = 4.092; fprintf(stderr, "TEST: f(%8.3lf)=%.5lf\n", x, f(x));
	x = 4.093; fprintf(stderr, "TEST: f(%8.3lf)=%.5lf\n", x, f(x));
	x = 4.094; fprintf(stderr, "TEST: f(%8.3lf)=%.5lf\n", x, f(x));
}


void bisekcja(double left, double right)
{
	double fl = f(left);
	while ( right-left > 1e-8 )
	{
		double middle = (left+right)/2.0, fm = f(middle);
		if ( fl * fm < 0.0 )
		{
			right = middle;
		}
		else
		{
			left = middle; fl = fm;
		}
	}
	printf("Miejsce zerowe : %8.5lf\n", (left+right)/2.0);
}

void zadanie3()
{
	printf("-----------------------\nZadanie 3\n");
	for (double x=0.0; x<5.0; x += 1.0)
		if ( f(x) * f(x+1.0) < 0.0 ) bisekcja(x, x+1.0);
	
}	

int main()
{
	for (int i=0; i<5; i++)
		for (int j=0; j<4; j++)
			scanf("%lf", &a[i][j]);

	zadanie1();
	zadanie2();
	zadanie3();
}
