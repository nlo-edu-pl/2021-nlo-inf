#include <stdio.h>
#include <stdlib.h>

/*
def CtoF(temp_C: float) -> float:
    return 1.8 * temp_C + 32
*/


double CtoF(double temp_C) {
    return 1.8 * temp_C + 32;
}

int main()
{
    printf("Hello world!\n");

    long long int a;
    long long int b;

    a = 2000000000L;
    b = 3700000000L;

    printf("Rozmiar short: %d   Rozmiar inta: %d  rozmiar long: %d   rozmiar long long: %d\n", sizeof(short int), sizeof(int), sizeof(long), sizeof(long long));

    printf("Suma wynosi: %lld\n", a + b);
    printf("Roznica wynosi: %lld\n", a - b);
    printf("Iloczyn wynosi: %lld\n", a * b);
    printf("Iloraz wynosi: %lld\n", a / b);


    double x, y;

    //x = 0.333333;
    y = 0.1;

    x = 0.2;

    printf("x + y = %.20f\n", x + y);
    printf("x * y = %.20f\n", x * y);

    double t1, t2, t3;

    t1 = 0;
    t2 = 36.6;
    t3 = 100;

    printf("t1 = %f F\n", CtoF(t1));
    printf("t2 = %f F\n", CtoF(t2));
    printf("t3 = %f F\n", CtoF(t3));

    return 0;
}
