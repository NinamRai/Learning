#include<stdio.h>
int main(){
    printf("Prime number from 2 - 100 are:");
    
    for (int n = 2; n<=100; n++){
        int is_prime = 1;
        for (int i = 2; i*i <= n; i++){
            if (n%i == 0){
                is_prime = 0;
                break;
            }
        }
    if (is_prime){
        printf("%d ",n);
    }

    }
    return 0;
}