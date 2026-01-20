#include <stdio.h>
#include <stdlib.h>
#include "IntStack.h"

int main(void){
    IntStack s;
    if(Initialize(&s,64) == -1){
        puts("스택 생성에 실패하였습니다.");
        return -1;
    }

    while(1){
        int menu, x;
        printf("현재 데이터 수: %d / %d\n",Size(&s), Capacity(&s));
        printf("(1)푸시 (2)팝 (3)피크 (4)출력 (5)비우기 (6)용량 (7)현재 스택 (8)비어있는가 (9)가득찼는가 (10)검색 (0)종료 : ");
        scanf("%d", &menu);

        if (menu == 0) break;
        switch(menu){
            case 1: 
                printf("데이터 : ");
                scanf("%d",&x);
                if(Push(&s,x)==-1){
                    puts("\a오류 : 푸시에 실패했습니다.");
               
                } break;
            case 2:
                if(Pop(&s,&x) == -1){
                    puts("\a오류 : 팝에 실패했습니다.");
                }else  
                printf("팝 데이터는 %d입니다.",x);
                break;
            case 3:
                if(Peek(&s,&x)==-1){
                    puts("\a오류 : 피크에 실패했습니다.");
                }else 
                printf("피크 데이터는 %d입니다.",x);
                break;
            case 4:
                Print(&s);
                break;
            case 5: 
                Clear(&s);
                puts("초기화 되었습니다");
                break;
            case 6: 
                printf("용량은 %d입니다", Capacity(&s));
                break;
            case 7:
                printf("현재 용량은 %d입니다", Size(&s));
                break;
            case 8:
                if (IsEmpty(&s)==1){
                    puts("스택이 비어있습니다.");
                } else{
                    puts("스택이 비어있지 않습니다.");
                }break;
            case 9:
                if (IsFull(&s)==1){
                    puts("스택이 다 차있습니다.");
                }else{
                    puts("스택이 다 차지 않습니다.");
                }break;
            case 10:
                printf("데이터 : ");
                scanf("%d",&x);
                if (Search(&s,x)==1){
                    puts("\a스택에 없습니다.");
                }else {
                    printf("%d는 %d번쨰에 있습니다.", x,Search(&s,x));
                }break;

        }
    }
    Terminate(&s);
    return 0;
}