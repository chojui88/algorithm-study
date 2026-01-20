#include <stdio.h>
#include "IntQuere.h"

int Search2(const IntQueue* q, int x){
    int i, idx, idx2;
   
    for(i =0; i< q->num ; i++){
        idx = q->que[(i+q->front) % q->max];
        if(x == idx ){
           return i;
        }
    }return -1;
    
}