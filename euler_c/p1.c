#include <stdio.h>

void main(int argc, char *argv[]) {
    int sumOfNum = 0;
    for (int i = 1; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
             sumOfNum += i;
        }
    }

    printf("%d\n", sumOfNum);
}
