#include <iostream>
#include <string>
// aaah 말해봐
//입력 두 줄
using namespace std;



int main() {
    string x, y;  // 가장 길개 낼 수 있는
 // 의사가 원하는
    cin >> x >> y;
    if (x.size() >= y.size()) 
        cout << "go";
    else 
        cout << "no";

    return 0;

}
