#include <stdio.h>
#include <math.h>

void main(int argc, char *argv[]) {
    long long int prime_factor = 2;
    long long int number = 600851475143;
    long long int limit = (long long int)(ceil(number / 2));
    for (long long int i = 3; i <= limit; i++) {
        if (number % i == 0) {
            prime_factor = i;
            printf("%lld", prime_factor);
        }
    }
}
