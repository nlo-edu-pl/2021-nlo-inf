#include <stdio.h>
#include <stdlib.h>

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

    return 0;
}
