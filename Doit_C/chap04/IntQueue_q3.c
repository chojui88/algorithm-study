#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int max;
    int num;
    int *que;
}ArrayIntQueue;

int Enque(ArrayIntQueue *s, int x){
   
    if (s->max<=s->num){
        return -1;
    }
    s->que[s->num++] = x;
    return 0;
}