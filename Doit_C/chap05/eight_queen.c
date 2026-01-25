#include <stdio.h>

int flag_a[8];
int flag_b[15];
int flag_c[15];
int pos[8];

void print(void){
    int i;
    for(i = 0; i < 8; i++){
        printf("2d", pos[i]);
    }putchar('\n');
}