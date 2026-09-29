#include <stdio.h>

int main() {
    long long first = 0, second = 1, next;

    printf("First 20 Fibonacci numbers:\n");

    for (int i = 0; i < 20; i++) {
        if (i == 0) {
            printf("%d: %lld\n", i + 1, first);
        } else if (i == 1) {
            printf("%d: %lld\n", i + 1, second);
        } else {
            next = first + second;
            first = second;
            second = next;
            printf("%d: %lld\n", i + 1, next);
        }
    }

    return 0;
}