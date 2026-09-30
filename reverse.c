#include <stdio.h>

int main(void)
{
    int n, rev = 0;

    printf("Enter an integer: ");
    scanf("%d", &n);

    while (n != 0) {
        int digit = n%10;      // last digit of n
        rev = rev*10 + digit;            // append digit to rev
        n = n/10 ;              // chop last digit off n
    }

    printf("Reversed: %d\n", rev);
    return 0;
}