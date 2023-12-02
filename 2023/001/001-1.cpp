#include<bits/stdc++.h>
using namespace std;


vector<string> sList;

void read() {
    sList.clear();

    string s;
    while (cin >> s) {
        sList.emplace_back(s);
    }
}


void work() {
    int ans = 0;
    for (string &s : sList) {
        for (int i = 0; i < s.size(); ++i) {
            if (isdigit(s[i])) {
                ans += 10 * (s[i] - '0');
                break;
            }
        }
        for (int i = 0; i < s.size(); ++i) {
            if (isdigit(s[s.size() - i - 1])) {
                ans += (s[s.size() - i - 1] - '0');
                break;
            }
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
