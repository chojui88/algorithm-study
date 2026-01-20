#include <stdio.h>
#include <stdlib.h>
#include "DoubleStack.h"

int DS_Initialize(DoubleStack *s, int max){
    s->stk = 0;
    if((s->stk = calloc(max,sizeof(int)))==NULL){
        s->max = 0;
        return -1;
    }
    s->max = max;
    s->ptrA = 0;
    s->ptrB = max-1;
    return 0;
}

int DS_PushA(DoubleStack *s, int x){
    if (s->ptrA > s->ptrB){
        return -1;
    }
    s->stk[s->ptrA++] = x;
    return 0;
}

int DS_PushB(DoubleStack *s, int x){
    if (s->ptrA > s->ptrB){
        return -1;
    }
    s->stk[s->ptrB--] = x;
    return 0;
}
int DS_PopA(DoubleStack *s, int *x){
    if(s->ptrA <= 0){
        return -1;
    }
    *x = s->stk[s->ptrA--];
    return 0;
}

int DS_PopB(DoubleStack *s, int *x){
    if(s->ptrA <= 0){
        return -1;
    }
    *x = s->stk[s->ptrB--];
    return 0;
}
