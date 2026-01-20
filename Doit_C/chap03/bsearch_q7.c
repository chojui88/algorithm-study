#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
    int ia = *(int*)a;
    int ib = *(int*)b;
    if (ia < ib){
        return -1;
    }else if (ia > ib){
        return 1;
    }else 
        return 0;
}

void *seqsearch(const void *key, const void *base,size_t nmemb, size_t size, int(*compar)(const void*, const void*)){
    int i;
    const char *x = (const char *)base;

    for(size_t i= 0; i<nmemb; i++)
    {
        if (compar(key,x+i*size)==0){
            return (void *)(x+i*size);
        }
        
    }
    return NULL;
}   
