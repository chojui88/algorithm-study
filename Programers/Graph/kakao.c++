#include <string>
#include <vector>

using namespace std;

vector<int> solution(int m, int n, int h, int w, vector<vector<int>> drops){


vector<vector<int>> time(m, vector<int>(n,비가 안오는 칸 최대값?));


//time 배열 만들기 drop에서부터
for(int i = 0; i<drops.size(); i++){
    
    int r = drops[i][1];
    int c = drops[1][i];
    time[r][c] = i + 1;
}
    // 가능한 선인장의 위치 찾기 
    
    deque<int> dq;

    for (int i = 0; i< n; i++) {
        while (!dq.empty()&& arr[dq.back()] >= arr[i])
            dq.pop_back();
        dq.push_back(o);

        if (dq.front()<= i - w)
            dq.pop_front();
        if(i>= w-1)
            result.push_back(arr[dq.front))])
    }
    
        if (mn != best){
            if (mn > best){
                best = mn;

                answerRow = i;
                answerCol = j;
            }
        else
            continue;
            }
            }
        
}




    //비가 처음으로 떨어진 곳이 선인장이 처음 비를맞는 순간
    //선인장이 최대한 늦게 비를 맞도록
    //그중에서도 위쪽, 왼쪽 행을 가장 최우선으로 (x값이 가장 작고 y값이 가장 작은)

}