#include <stdio.h>
#include <stdlib.h>
#include "IntQuere.h"

int main(void){
    IntQueue que;

    if(Initialize(&que,64)==-1){
        puts("큐의 생성에 실패햐였습니다.");
        return 1;
    }

    while(1){
        int m, x;

        printf("현재 데이터 수: %d / %d \n", Size(&que),Capacity(&que));
        printf("(1)인큐 (2)디큐 (3)피크 (4)출력 (5)비었니 (6)꽉찼니 (7)검색 (8)검색 (0)종료");
        scanf("%d",&m);

        if(m==0)break;
        switch(m){
            case 1 :
            printf("데이터 : ");
            scanf("%d",&x);
            if(Enque(&que,x)==-1){
                puts("\a오류: 인큐에 실패");
            }break;

            case 2 :
            if(Deque(&que,&x)==-1){
                puts("\a오류: 디큐에 실패");
            }else
                printf("디큐한 데이터는 %d입니다",x);
            break;

            case 3 :
            if(Peek(&que,&x)==-1){
                 puts("\a오류: 피큐에 실패");
            }else
                printf("피큐한 데이터는 %d입니다",x);
            break;

            case 4 :
            Print(&que);
            break;

            case 5 :
            if (IsEmpty(&que)== 1){
                puts("비어있습니다");
            }else
                printf("비어있지 않습니다.");
            break;

            case 6 : 
            if (IsFull(&que)== 1){
                puts("차있습니다");
            }else
                printf("차있지않습니다.");
            break;

            case 7 :
            printf("데이터 : ");
            scanf("%d",&x);
            int idx=Search(&que, x);
            if(idx ==-1){
                puts("조회에 실패");
            }else
                printf("%d에 있습니다.",idx);
            break;

        }
    }
    Terminate(&que);
    return 0;
}