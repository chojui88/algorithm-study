#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[10];
    int height;
    int weight;
}Person;

/*Person 형 비교함수 - 이름 오름차순*/
int npcmp (const Person *x,const Person *y){
    return strcmp(x->name, y->name);
}
/*strcmp = 문자열 전체를 비교해서 사전순으로 앞뒤 구분해줌*/

int hpcmp (const Person *x,const Person *y){
    return x->height < y->height ? -1 : x->height > y->height ? 1 : 0;
}

int wpcmp (const Person *x,const Person *y ){
    return x->weight < y->weight ? 1 : x->weight > y->weight ? -1 : 0;
}

/*사람 no 명의 데이터 출력*/
void print_person(const Person x[], int no){
    int i;
    for(i = 0; i< no; i++){
        print("%-10s %dcm %dkg\n", x[i].name, x[i].height, x[i].weight);
    }
}

int main(void){
    Person x[] = {
        {"summi", 170, 52},
        {"yoobin", 150, 23},
        {"sohee", 152, 34},
        {"jina", 171, 43},
    };

    int nx= sizeof(x) / sizeof(x[0]);

    puts("정렬 전");
    print_person(x, nx);
    
    qsort(x, nx, sizeof(Person),(int(*)(const void *, const void *))npcmp);
    puts("\n이름 순으로 오름차순 정렬 후");
    print_person(x, nx);

    qsort(x, nx, sizeof(Person), (int(*)(const void*, const void*))hpcmp);
    puts("\n 키 순으로 오름차순 정렬 후");
    print_person(x, nx);

    qsort(x, nx, sizeof(Person),(int(*)(const void *, const void *))wpcmp);
    puts("\n몸무게 내림차순으로 정렬 후");
    print_person(x,nx);

    return 0;
}