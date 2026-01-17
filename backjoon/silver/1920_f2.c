#include <stdio.h>
#include <stdlib.h>

int search(int a[], int n, int key){
    for(int i = 0; i < n ; i++){
        if (a[i]== key)
        return 1;
        }
        return 0;
    }

int main() {
    int n , m;
    int *arr_n;
    scanf("%d",&n);
    arr_n = calloc(n , sizeof(int));

    for (int i = 0; i<n;i++){
        scanf("%d",&arr_n[i]);
    
    }
    scanf("%d",&m);
   int *arr_m;
    arr_m = calloc(m, sizeof(int));

    for (int i = 0; i<m;i++){
        scanf("%d",&arr_m[i]);
    
    }

    for (int i = 0; i<m; i++){
        printf("%d",search(arr_n, n, arr_m[i]));
    }


    
    free(arr_n);
    free(arr_m);
    return 0;
}