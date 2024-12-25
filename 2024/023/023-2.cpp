#include<bits/stdc++.h>
using namespace std;


int N;
vector<vector<bool>> adj;
vector<string> i2s;
map<string, int> s2i;

void read() {
    N = 0;

    set<string> sSet;
    vector<pair<string, string>> edges;

    string line;
    while (cin >> line) {
        string a = line.substr(0, 2);
        string b = line.substr(3);

        sSet.insert(a);
        sSet.insert(b);
        edges.push_back({a, b});
    }

    for (const string &s : sSet) {
        s2i[s] = N++;
        i2s.push_back(s);
    }

    adj = vector(N, vector(N, false));
    for (auto [a, b] : edges) {
        adj[s2i[a]][s2i[b]] = adj[s2i[b]][s2i[a]] = true;
    }
}


bool rec(int idx, vector<int> &ids, int size) {
    if (ids.size() == size) {
        return true;
    }

    if (idx == N) {
        return false;
    }

    bool isOk = true;
    for (int i = 0; i < ids.size(); ++i) {
        if (!adj[ids[i]][idx]) {
            isOk = false;
            break;
        }
    }

    if (isOk) {
        ids.push_back(idx);
        if (rec(idx + 1, ids, size)) {
            return true;
        }
        ids.pop_back();
    }

    return rec(idx + 1, ids, size);
}


void work() {
    for (int size = 4; ; ++size) {
        vector<int> ids;
        if (rec(0, ids, size)) {
            for (int i = 0; i < size; ++i) {
                if (i) cout << ',';
                cout << i2s[ids[i]];
            }
            cout << endl;
        } else {
            break;
        }
    }
}


int main() {
    read();
    work();
    return 0;
}
