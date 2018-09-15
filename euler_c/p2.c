#include <stdio.h>

void main(int argc, char *argv[]) {
    int sumOfNum = 0;
    int fib = 0;
    int prev = 1;
    int curr = 1;
    while (fib  <= 4000000) {
        if (fib % 2 == 0) {
                sumOfNum += fib;
        }
        fib = prev + curr;
        prev = curr;
        curr = fib;
    }
    printf("%d\n", sumOfNum);

}
