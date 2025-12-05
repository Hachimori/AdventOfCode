#include<bits/stdc++.h>
using namespace std;


vector<pair<long long, long long>> range;
vector<long long> id;

void read() {
    string line;
    while (1) {
        getline(cin, line);
        if (line.empty()) break;
        stringstream ss(line);
        long long a, b;
        char ch;
        ss >> a >> ch >> b;
        range.emplace_back(a, b);
    }

    long long v;
    while (cin >> v) {
        id.push_back(v);
    }
}


void work() {
    int cnt = 0;
    for (long long v : id) {
        for (auto [a, b] : range) {
            if (a <= v && v <= b) {
                cnt++;
                break;
            }
        }
    }
    cout << cnt << endl;
}


int main() {
    read();
    work();
    return 0;
}
