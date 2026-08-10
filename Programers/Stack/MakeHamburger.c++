#include <string>
#include <vector>

using namespace std;

int solution(vector<int> ingredient){
    int answer = 0;


    vector<int> burger;

    for (int x : ingredient){
        burger.push_back(x);
    
        if (burger.size() >= 4){

            int n = burger.size();
            
                if (burger[n-4] == 1 &&
                burger[n-3] == 2 &&
                burger[n-2] == 3 &&
                burger[n-1] == 1)
                {
                    for (int i = 0; i<4; i++){
                        burger.pop_back();
                    
                    } answer++;
                    
                }
            }
        }
        return answer;
    }
