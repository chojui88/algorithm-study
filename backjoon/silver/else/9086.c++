#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string s; // s를

    cin >> n;

    while(n--){
        cin >> s; //s를 계속 받는데 
        cout << s[0] << s[s.length() - 1] << '\n';
    } //s의 문자열의 개수번째를 출력한다.
// 문자열 첫글자와 마지막글자 출력

    return 0;
}