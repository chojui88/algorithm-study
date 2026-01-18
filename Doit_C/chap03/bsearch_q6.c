#include <stdio.h>
#include <stdlib.h>

int long_cmpr(const long *a, long *b){
    if (*a<*b){
        return 1;
    }else if (*a>*b){
        return -1;
    }else   
        return 0;
    
}

int main(void){
    long nx, ky;
    long *x;
    long *p;
    puts("bsearch 함수를 이용해서 검색");
    printf("요소 개수: ");
    scanf("%ld",&nx);
    x = calloc(nx, sizeof(long));
    printf("x[0]: ");
    scanf("%ld",&x[0]);
    for(int i = 1; i<nx; i++){
        do{
        printf("x[%d]: ",i);
        scanf("%ld",&x[i]);
        }while(x[i]>x[i-1]);
    }
    scanf("%ld",&ky);
    p = bsearch(&ky,x,nx,sizeof(long),(long(*)(const void*, const void*))long_cmpr);
    if (p==NULL){
        puts("검색 실패");
    }else
    printf("%ld은 x[%ld]에 있습니다.",ky,(long)(p-x));
    free(x);
    return 0;

}