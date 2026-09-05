#include<stdio.h>
int main(){
    int a = 7;
    for (int i = 1; i<=10; i++){
        int b = a*i;
        printf("%d * %d = %d \n",a,i,b);
    }
}