#include<bits/stdc++.h>
using namespace std;

int N;
vector<vector<bool>> adj;
vector<bool> startsWithT;
map<string, int> s2i;

void read() {
    N = 0;

    vector<pair<int, int>> edges;

    string line;
    while (cin >> line) {
        string a = line.substr(0, 2);
        string b = line.substr(3);

        auto push = [] (string s) {
            if (s2i.count(s)) return;
            s2i[s] = N++;
            startsWithT.push_back(s[0] == 't');
        };
        push(a);
        push(b);

        edges.push_back({s2i[a], s2i[b]});
    }

    adj = vector(N, vector(N, false));
    for (auto [a, b] : edges) {
        adj[a][b] = adj[b][a] = true;
    }
}


void work() {
    int ans = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            for (int k = j + 1; k < N; ++k) {
                ans += ((startsWithT[i] || startsWithT[j] || startsWithT[k]) && adj[i][j] && adj[j][k] && adj[k][i]);
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
