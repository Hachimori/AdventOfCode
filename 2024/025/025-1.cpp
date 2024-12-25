#include<bits/stdc++.h>
using namespace std;


vector<vector<string>> locks;
vector<vector<string>> keys;

void read() {
    while (1) {
        vector<string> toPush(7);
        for (int i = 0; i < 7; ++i) {
            if (!(cin >> toPush[i])) {
                return;
            }
        }

        if (toPush[0] == "#####") {
            locks.push_back(toPush);
        } else {
            keys.push_back(toPush);
        }
    }
}


vector<int> convert(vector<string> &v) {
    vector<int> ret(5, 0);
    for (int i = 0; i < v[0].size(); ++i) {
        for (int j = 0; j < v.size(); ++j) {
            ret[i] += v[j][i] == '#' ? 1 : 0;
        }
        ret[i] -= 1;
    }
    return ret;
}

void work() {
    vector<vector<int>> lockValues;
    vector<vector<int>> keyValues;

    for (int i = 0; i < locks.size(); ++i) {
        lockValues.push_back(convert(locks[i]));
    }
    for (int i = 0; i < keys.size(); ++i) {
        keyValues.push_back(convert(keys[i]));
    }

    int cnt = 0;
    for (int i = 0; i < lockValues.size(); ++i) {
        for (int j = 0; j < keyValues.size(); ++j) {
            for (int k = 0; k < lockValues[i].size(); ++k) {
                if (lockValues[i][k] + keyValues[j][k] >= 6) {
                    goto _fail;
                }
            }
            ++cnt;
            _fail:;
        }
    }
    cout << cnt << endl;
}


int main() {
    read();
    work();
    return 0;
}
