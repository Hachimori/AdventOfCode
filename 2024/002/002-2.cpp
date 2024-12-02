#include<bits/stdc++.h>
using namespace std;


vector<vector<int>> input;

void read() {
    string line;
    while (getline(cin, line)) {
        stringstream ss(line);
        vector<int> row;
        int num;
        while (ss >> num) {
            row.push_back(num);
        }
        input.push_back(row);
    }
}


bool isSafe(vector<int> &vList) {
    int inc = false;
    int dec = false;
    for (int i = 0; i + 1 < vList.size(); ++i) {
        if (vList[i] < vList[i + 1]) {
            inc = true;
        }
        if (vList[i] > vList[i + 1]) {
            dec = true;
        }
        int diff = abs(vList[i] - vList[i + 1]);
        if (!(1 <= diff && diff <= 3)) {
            return false;
        }
    }
    return inc + dec == 1;
}


void work() {
    int ans = 0;

    for (vector<int> vList : input) {
        for (int toRemove = 0; toRemove < vList.size(); ++toRemove) {
            int backup = vList[toRemove];
            vList.erase(vList.begin() + toRemove);
            if (isSafe(vList)) {
                ++ans;
                break;
            }
            vList.insert(vList.begin() + toRemove, backup);
        }
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
