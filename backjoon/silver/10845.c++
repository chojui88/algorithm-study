#include <iostream>
#include <queue>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    queue<int>q;
    for (int i = 0; i<n; i++){
        string len;
        cin >> len;
        
        if (len == "push"){
            int x;
            cin>> x;
            q.push(x);

        }else if (len == "pop"){
            if (q.empty()){
                cout << -1 << '\n';
            }else{
                cout << q.front()<< '\n';
                q.pop();
            }

        }else if (len == "size"){
            cout << q.size()<<'\n';
            
        }else if (len == "empty"){
            if(q.empty()){
                cout << 1 << '\n';
            }else{
                cout << 0 << '\n';
            }
            
        }else if (len == "front"){
            if (q.empty()){
                cout << -1 << '\n';
            }else{
                cout << q.front()<< '\n';
            }
            
        }else if (len == "back"){
            if (q.empty()){
                cout << -1 << '\n';
            }else {
            cout << q.back()<< '\n';
            }
            
        }
    }

}