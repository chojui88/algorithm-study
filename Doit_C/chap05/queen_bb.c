#include <stdio.h>

int flag[8]; /* 행에 퀸 배치했는지*/
int pos[8]; /* 열에서 퀸 위치*/

void print(void){
    int i;
    for(i = 0; i<8; i++){
        printf("%2d",pos[i]);
    }
    putchar('\n');
}

void set(int i){
    int j;
    for(j = 0; j <8; j++){
        if(!flag[j]){
            pos[i] = j;
            if(i == 7){
                print();
            }else{
                flag[j] = 1;
                set(i+1);
                flag[j] = 0;
            }
        }
    }
}

int main(void){
    int i;
    for(i = 0; i<8; i++){
        flag[i] = 0;
    }
    set(0);

    return 0;
}