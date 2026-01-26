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