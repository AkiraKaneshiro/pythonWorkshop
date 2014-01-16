#include <stdio.h>
#include <time.h>

/* compile with: gcc -O2 -o loop loop.c */

int main() {
    clock_t f = 0;
    clock_t s = clock();

    long total = 0;
    for (int i = 0; i < 1000; i++)
        for (int j = 0; j < 1000; j++) {
            total += i;
        }

    printf("%ld\n", total);
    f = clock();
    printf("ran in: %.3f sec\n", ((double)f - (double)s) * 1.0e-6);
    return 0;
}

