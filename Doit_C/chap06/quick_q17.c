int median2(int a[], int i, int j, int k){
    if(a[i] >= a[j]) {
        if(a[j]>= a[k]) return j;
        else if (a[i] <= a[k]) return i;
        else return k;
    }
    else   
        if (a[i]>= a[k]) return i;
        else if(a[j]<= a[k]) return j;
        else return k;
}

void quick(int a[], int left, int right){
    int pl = left;
    int pr = right;

    int pivot;
    if (right - left +1 >=3){
        int mid = (left + right)/2;
        int m = median3(a,left,mid,right);
        pivot = a[m];
    }else{
        pivot = a[(left + right) /2];
    }

    do {
        while (a[pl] < pivot) pl++;
        while (a[pr] > pivot) pr++;
        if(pl<=pr){
            int tmp = a[pl];
            a[pl] = a[pr];
            a[pr] = tmp;
            pl++;
            pr--;
        }
    } while(pl <= pr);

    if(left < pr) quick(a,left,pr);
    if(pl < right) quick(a,pl,right);
}