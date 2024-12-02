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


void work() {
    int ans = 0;
    for (vector<int> vList : input) {
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
                goto _fail;
            }
        }

        if (inc + dec == 1) {
            ans++;
        }

        _fail:;
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
