#include <stdio.h>
#include <stdlib.h>
#include "IntStack.h"

typedef struct{
    int *stk; /*공유 배열*/
    int capacity;
    int topA;
    int topB;
}DoubleStack;

int Initialize(DoubleStack *s, int max){
    s->stk = calloc(max, sizeof(int));
}

int main(void){
    IntStack s;
    if(Initialize(&s,64) == -1){
     puts("스택 생성에 실패하였습니다.");
        return -1;
    }

    int *x = calloc(64, sizeof(int));
}