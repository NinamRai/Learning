#include<stdio.h>
int main(){
    for (int i = 0; i < 10; i++) {
    if (i % 3 == 0) continue;   // skip the REST of this iteration
    if (i == 7) break;
    printf("%d ", i);}
}


