#ifndef ___DoubleStack
#define ___DoubleStack

typedef struct{
    int *stk; /*스택 시작 주소*/
    int max;
    int ptrA; /*스택 a 현재 포인터(앞에서 증가)*/ 
    int ptrB;
}DoubleStack;

int DS_Initialize(DoubleStack *s, int max);
int DS_PushA(DoubleStack *s, int x);
int DS_PushB(DoubleStack *s, int x);
int DS_PopA(DoubleStack *s, int *x);
int DS_PopB(DoubleStack *s, int *x);

#endif