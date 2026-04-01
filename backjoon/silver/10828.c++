#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    //정수를 저장하는 스탯을 구현, 
    //입력으로 주어지는 명령을 처리
    cin.tie(0)->sync_with_stdio(0);
    stack<int> s;

    int n = 0;
    cin>> n;
    

    for (int i = 0; i<n; i++){
        string st ;
        cin>>st;
        if (st == "push"){
            int x;
            cin >> x;
            s.push(x);
        }
        else if (st == "pop"){
            if (s.empty()){
                cout << -1 << '\n';
            }else {
                cout << s.top()<< '\n';
                s.pop();
            }
        }
        else if (st == "size"){
            cout << s.size() << '\n';
        }
        else if (st == "empty"){
            if (s.empty()){
                cout << 1 << '\n';
            }else {
                cout << 0 << '\n';
            }


        }else if (st == "top"){
            if (s.empty()){
                cout << -1 << '\n';
            }else {
                cout << s.top() << '\n';
                
            }
        }
        


    }
    return 0;
}