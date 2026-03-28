#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
    int n;
    cin >> n;
    double result = 0;
    vector<int> list(n);
   for (int i = 0; i<n ; i++ ){
        cin >> list[i];
    }
   int quater = 0;
   sort(list.begin(), list.end());
   
    if (n){
       int cut =  round(n*0.15);
       int sum = 0;
        
       for (int i = cut; i < n - cut ; i++){
            sum += list[i];
       }
       result = (double)sum / (n - (cut* 2));
       result = round(result);
    }else{
        result = 0;
    }


    cout << result;
}
//절사평균 = 가장 큰 값들과 작은 값들 제외하고 평균 내는것
//30% 절사평균 = 위에서 15%, 아래에서 15% 제외
// 제외되는 사람수, 계산된 평균 반올림

