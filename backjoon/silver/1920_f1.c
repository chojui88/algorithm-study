#include <stdio.h>

int main(void){
int n;
scanf("%d",&n);
int arr[n+1];
for(int i = 1 ;i<=n;i++){
    scanf("%d",&arr[i]);
}
int m;

scanf("%d",&m);
int arr_m[m];
for(int i = 0 ;i<m;i++){
    scanf("%d",&arr_m[i]);
}

for (int j = 0; j<m;j++){
    int flag = 0;
    for (int i = 1 ; i<=n ; i++){
        if (arr_m[j] == arr[i] ){
        printf("1\n");
        flag = 1;
        break;
        }
        
    }
    if (flag == 0)
    printf("0\n");
}
}