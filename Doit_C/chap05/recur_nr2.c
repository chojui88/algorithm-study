#include <stdio.h>
#include "IntStack.h"

void recur(int n){

    IntStack stk;
    Initialize(&stk, 100);
    
    Top:
        if(n > 0){
            Push(&stk , n);
            n = n -1;
            goto Top;
        }
        if(!IsEmpty(&stk)){ /* 스택이 비어있지 않으면*/
            Pop(&stk,&n);
            printf("%d\n",n);
            n = n-2;
            goto Top;
        }

    Terminate (&stk);

}
int main(void){
    recur(5);
    return 0;
}