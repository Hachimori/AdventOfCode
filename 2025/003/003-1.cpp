#include<bits/stdc++.h>
using namespace std;


vector<string> str;

void read() {
    string s;
    while (cin >> s) {
        str.push_back(s);
    }
}


void work() {
    int sum = 0;
    for (string &s : str) {
        int maxV = 0;
        for (int i = 0; i < s.size(); ++i) {
            for (int j = i + 1; j < s.size(); ++j) {
                maxV = max(maxV, 10 * (s[i] - '0') + (s[j] - '0'));
            }
        }
        sum += maxV;
    }
    cout << sum << endl;
}


int main() {
    read();
    work();
    return 0;
}
