#include <stdio.h>
#include <stdlib.h>

/*작업용 배열*/
static int *buff;

static void __mergesort(int a[], int left, int right){
    if(left <right){
        int center = (left + right) /2;
        int p = 0;
        int i;
        int j = 0;
        int k = left;
        __mergesort(a, left,center);
        __mergesort(a, center+1, right);
        for(i = left; i<center + 1; i++){
            buff[p++] = a[i];
        } /* p는 왼쪽 배열 버퍼의 인덱스*/
        while(i <= right && j < p){
            a[k++] = (buff[j] <= a[i]) ? buff[j++] : a[i++];
        }
        while(j<p){
            a[k++] = buff[j++];

        }
    }
}

int mergesort(int a[], int n){
    if((buff = calloc(n, sizeof(int)))==NULL)
    return -1;
    __mergesort(a, 0, n-1);
    free(buff);
    return 0;
}

int main(void){
    int i, nx;
    int *x;
    puts("병합 정렬");
    print("요소 개수 : ");
    scanf("%d" ,&nx);
    x = calloc(nx, sizeof(int));

    for(i = 0; i<nx; i++){
        print("x[%d] : ", i);
        scanf("%d", &x[i]);
    }
    mergesort(x,nx);
    puts("오름차순으로 정렬했습니다.");
    for(i = 0; i <nx; i++){
        print("x[%d] = %d\n", i , x[i]);

    }free(x);

    return 0;
}