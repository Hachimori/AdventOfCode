#include<bits/stdc++.h>
using namespace std;


vector<vector<long long>> vList;
vector<string> ops;

void read() {
    string line;
    while (getline(cin, line)) {
        stringstream ss(line);
        string s;
        vector<string> sList;
        while (ss >> s) {
            sList.emplace_back(s);
        }

        if (sList[0] == "+" || sList[0] == "*") {
            ops = sList;
        } else {
            vList.push_back(vector<long long>());
            for (int i = 0; i < sList.size(); ++i) {
                vList.back().push_back(stoll(sList[i]));
            }
        }
    }
}


void work() {
    long long sum = 0;
    for (int c = 0; c < vList[0].size(); ++c) {
        long long toAdd = ops[c] == "+" ? 0 : 1;
        for (int r = 0; r < vList.size(); ++r) {
            if (ops[c] == "+") {
                toAdd += vList[r][c];
            } else {
                toAdd *= vList[r][c];
            }
        }
        sum += toAdd;
    }
    cout << sum << endl;
}


int main() {
    read();
    work();
    return 0;
}
