#include<bits/stdc++.h>
using namespace std;

string S;

void read() {
    cin >> S;
}


void add(vector<int> &buf, int cnt, int id) {
    for (int i = 0; i < cnt; ++i) {
        buf.push_back(id);
    }
}


void work() {
    int nId = 0;
    vector<int> buf;
    for (int i = 0; i < S.size(); ++i) {
        if (i % 2 == 0) {
            add(buf, S[i] - '0', nId++);
        } else {
            add(buf, S[i] - '0', -1);
        }
    }

    int L = 0, R = buf.size() - 1;
    while (L < R) {
        while (buf[L] != -1 && L < buf.size()) {
            ++L;
        }
        while (buf[R] == -1 && R >= 0) {
            --R;
        }
        if (L < R) {
            swap(buf[L], buf[R]);
        }
    }

    long long ans = 0;
    for (int i = 0; i < buf.size(); ++i) {
        if (buf[i] == -1) {
            break;
        }
        ans += 1LL * i * buf[i];
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
