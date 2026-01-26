#include <stdio.h>
#include <stdlib.h>
#include "IntStack.h"

#define swap(type, x, y) do { type t = x; x = y; y = t;} while(0)

void quick(int a[], int left, int right){
    IntStack lstack; /* 나눌 첫 요소 인덱스 */
    IntStack rstack;

Initialize(&lstack, right - left + 1);
Initialize(&rstack, right - left + 1);

push(&lstack, left);
push(&rstack, right);

while(!IsEmpty(&lstack)){
    int pl = (Pop(&lstack, &left), left); /* pl = (a,b) -> a를 실행하고 b의 값을 넣는다. */
    int pr = (Pop(&rstack, &right), right);
    int x = a[(left + right) / 2];

    do{
        while(a[pl] < x) pl++;
        while(a[pr] > x) pr--;
        if(pl <= pr){
            swap(int, a[pl], a[pr]);
            pl++;
            pr--;
        }
    }while(pl <= pr);

    int left_size = pr - left + 1;
    int right_size = right - pl + 1;

    if(left_size < right_size){
        if(pl < right){
            Push(&lstack, pl);
            Push(&rstack, right);
        }
        right= pr;
    }else {
    if(left < pr){
        Push(&lstack, left);
        Push(&rstack, pr);
    }
    left = pl;
    }
}
Terminate(&lstack);
Terminate(&rstack);
}