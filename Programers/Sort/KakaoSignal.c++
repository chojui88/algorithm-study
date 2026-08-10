#include <string>
#include <vector>

using namespace std;
int solution(vector<vector<int>> signals){
    int answer = 0;

    //i는 흐르는 시간
    for (int i = 1 ; i<=315; i++){
        //해당 시간에서, 그 해당 색이 같은지
        //j는 신호등 줄
       bool ok = true;
        for (int j = 0; j<signals.size(); j++){
            int p = signals[j][0] + signals[j][1] + signals[j][2];
            int idx = (i-1)%p+1;

            if (idx > signals[j][0] &&
                 idx <= signals[j][0] + signals[j][1]){
               continue;
            }else{
                ok = false;
                break;
            }

        }
        if (ok){
            return i;
        }
    }
    return -1;
}