#include <stdio.h>

int str_chr(const char *s, int c){
    int i = 0;
    c = (char)c; /*c를char타입으로 강제 바꾼뒤 다시c에 저장*/
    while (s[i]!= c){
        if(s[i]== '\0')
            return -1;
        i++;
    }return i;

} 

int main(void){
    char str[64];
    char tmp[64];
    int ch; /*검색할 문자*/
    int idx;

    printf("문자열 : ");
    scanf("%s", str);

    printf("검색할 문자 : ");
    scanf("%s", tmp);
    ch = tmp[0]; /*아스키코드로 저장*/

    if((idx = str_chr(str, ch)) == -1){
        puts("문자열에 없습니다.");
    } else  
        printf("문자 '%c'는 %d 번쨰에 있습니다.",ch,idx+1);

    return 0;
}