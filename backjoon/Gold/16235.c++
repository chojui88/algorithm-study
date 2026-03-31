#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,m,k;
     // nxn 땅, m개의 나무를 구매,
    cin >> n >> m >> k;
    // A는 로봇이 각 칸을 돌아다니면서 추가하는 양분의 양
    vector<int> A[n][n];
      //r 세로열 , c 가로횡 1부터 시작
    for (int i = 1; i <= n; i++){
        for (int j = 0; j<=n; j++){
            cin >> A[i][j];
        }
    }    

    // 현재 양분값 5로 초기화
    vector<int> nutrient[n][n];
        for (int i = 1; i<=n; i++){
            for (int j = 1; j<=n; j++){
            nutrient[i][j] = 5;
            }
        }

    vector<int> tree[101][101];

    int x, y, z;
    //x,y 좌표 값에 나이 넣기
    for (int i = 0; i<m; i++){
        cin>> x >> y >> z;
        tree[x][y].push_back(z);
    }
    
    for (int a = 0; a<k; a++){
        
        //봄, 여름
        for (int i = 1; i<=n; i++){
            for (int j = 1; j<=n; j++){
                if (tree[i][j].empty()) continue;
                sort(tree[i][j].begin(), tree[i][j].end());  //어린순서대로 정렬
                //나무 있는 땅에 양분 먹음
                // 하나 칸에 여러나무, 나이어린 나무부터 나이만큼 양분 얻는다
                vector<int> alive;
                for (int age: tree[i][j]){
                    if (nutrient[i][j]>=age){
                        nutrient[i][j] -= age;
                        alive.push_back(age+1);
                    }else {
                    
                        nutrient[i][j] +=(age/2); // 양분 = 나무 나이 /2 , 소수점 아래 버림 floor() 
                    }
                } tree[i][j] = alive;         
            }
        }
    // 가을에는 나무가 번식, 나이가 5의 배수여야 함. 인접한 8칸에 나이 1인 나무 생성
        for (int i = 1; i<=n; i++){
            for (int j = 1; j<=n; j++){
                for (int age : tree[i][j]) {
                    if (age%5==0){
                        tree[i-1][j-1].push_back(1);
                        tree[i-1][j].push_back(1);
                        tree[i-1][j+1].push_back(1);
                        tree[i][j-1].push_back(1);
                        tree[i-1][j+1].push_back(1);
                        tree[i+1][j-1].push_back(1);
                        tree[i+1][j].push_back(1);
                        tree[i+1][j+1].push_back(1);
                    }
            }
        }
    // 겨울에는 로봇 돌아다니면서 땅에 양분 추가 A[r][c] 입력으로 주어짐
        for (int i = 1; i<=n; i++){
            for (int j = 1; j<=n; j++){
                nutrient[i][j] += A[i][j];
            }
        }
    }}
    //k 년이 지난후 살아있는 나무의 개수
    int sum_tree = 0;
    for (int i = 1; i<=n; i++){
        for (int j = 1; j<=n; j++){
            
                sum_tree += tree[i][j].size();
            }
        }
    cout <<sum_tree;
} 
