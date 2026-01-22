#ifndef ___IntStack
#define ___IntStack
/**-스택 구조체 */
typedef struct{
    int max; /*스택 용량*/
    int ptr; 
    int *stk; /* 스택 첫 요소 포인터*/
}IntStack;

/* 스택 구조체, 스택 크기를 받으면 초기화하는 함수*/
int Initialize(IntStack *s, int max);

int Push(IntStack *s, int x);

int Pop(IntStack *s, int *x);

/*-가장 위 데이터 확인 */
int Peek(const IntStack *s, int *x);

void Clear(IntStack *s);

int Capacity(const IntStack *s);

int Size(const IntStack *s);

int IsEmpty(const IntStack *s);

int IsFull(const IntStack *s);

int Search(const IntStack *s, int x);

void Print(const IntStack *s);

void Terminate(IntStack *s);

#endif