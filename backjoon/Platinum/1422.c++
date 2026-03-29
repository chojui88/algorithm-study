#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int k, n;
    cin >>k >> n;

    vector<string> lst(k);

    for(int i = 0; i < k; i++){
        cin >> lst[i];
    }

    

string max_val = lst[0];
for(int i = 1; i < k; i++){
    if (lst[i].size() > max_val.size() ||
       (lst[i].size() == max_val.size() && lst[i] > max_val))
    {
        max_val = lst[i];
    }
}

    for(int i = 0; i < n - k; i++){
        lst.push_back(max_val);
    }

   sort(lst.begin(), lst.end(), [](string a, string b){
        return a + b > b + a;
    });

    string result = "";
    for(int i = 0; i < n; i++){
        result += lst[i];
    }

    cout << result;
}