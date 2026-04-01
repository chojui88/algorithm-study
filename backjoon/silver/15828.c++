#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    //인터넷 연결 
    // 패킷으로 요청 주고받음
    // 패킷은 라우터를 여러번 거침 
    int n;
    cin >> n;
    queue <int> q;

        int x;
    while(true){
        cin >> x;
        if (x==0){ // 라우터가 패킷 처리함
            q.pop();
        }else if (x==-1){
            break;
        }else{
            if (q.size()<n){
                q.push(x);
            }else {
                continue;
            }
           
        }
    }
    //버퍼 =  패킷을 임시적으로 보관 
    //  들어온 패킷이 순서대로 위치 = 큐
    // 라우터에 먼저 온 패킷부터 하나씩 처리한후 버퍼에서 제거
    // 라우터가 패킷을 처리하는 속도보다 패킷이 더 빨리 들어오면 버려짐
    // 하나의 라우터, 버퍼의 상태 어떻게 변하는가
    if (q.empty()) {
        cout << "empty" << '\n';
    }
    while(!q.empty()){        
        cout<<q.front()<< " ";
        q.pop();
    }
}