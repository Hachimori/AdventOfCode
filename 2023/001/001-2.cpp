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
    string digits[2][10] = {
        {"#", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
        {"#", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
    };

    int ans = 0;
    for (string &s : sList) {
        vector<int> vList;
        for (int idx = 0; idx < s.size(); ++idx) {
            for (int i = 0; i < 2; ++i) {
                for (int d = 1; d < 10; ++d) {
                    string &candi = digits[i][d];
                    if (s.substr(idx, candi.size()) == candi) {
                        vList.emplace_back(d);
                    }
                }
            }
        }
        ans += vList[0] * 10 + vList.back();
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
