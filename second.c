// Read an integer and print the sum of its digits (e.g. 4821 → 15). Use only a loop, %, and /.
#include<stdio.h>
int main(void){
    int num , sum = 0;
    
    if(scanf(" %d ", &num) != 1) return 1;
// for 0 

    if (num < 0){
        num = -num;
        // for negative value
    }

    while (num>0){
        sum += num % 10;
        num = num/10;
    }
    printf("%d is the sum of digit of %d ",sum,num);
    return 0;
}