#include <stdlib.h>
#include <stdio.h>

/* no개수의 원반을 x기둥부터 y기둥까지 옮기는 횟수*/
void move(int no, int x, int y){
    if (no > 1){
        move(no-1,x,6-x-y); /* 그룹을 시작기둥에서 중간 기둥으로*/
        printf("원반 [%d]를 %d 기둥에서 %d 기둥으로 옮김", no, x, y);
    /* 바닥 원반을 목표 기둥으로*/
    }

    if (no>1){
        move(no-1,6-x-y,y);
    }
}

int main(void){
    int n;
    printf("하노이 탑의 \n원반 개수 : ");
    scanf("%d",&n);
    move(n,1,3);

    return 0;
}