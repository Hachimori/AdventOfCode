#include<bits/stdc++.h>
using namespace std;


vector<string> lines;

void read() {
    string line;
    while (getline(cin, line)) {
        lines.push_back(line);
    }
}


void work() {
    long long sum = 0;

    for (int cIdx = 0; cIdx < lines.back().size(); ) {
        int nexCidx = cIdx + 1;
        while (nexCidx < lines.back().size() && lines.back()[nexCidx] == ' ') {
            ++nexCidx;
        }

        vector<long long> vList;
        for (int c = cIdx; c < nexCidx; ++c) {
            long long toPush = 0;
            for (int r = 0; r < lines.size() - 1; ++r) {
                if (lines[r][c] != ' ') {
                    toPush = toPush * 10 + (lines[r][c] - '0');
                }
            }
            if (toPush != 0) {
                vList.push_back(toPush);
            }
        }

        long long toAdd = lines.back()[cIdx] == '+' ? 0 : 1;
        for (int i = 0; i < vList.size(); ++i) {
            if (lines.back()[cIdx] == '+') {
                toAdd += vList[i];
            } else {
                toAdd *= vList[i];
            }
        }
        sum += toAdd;

        cIdx = nexCidx;
    }

    cout << sum << endl;
}


int main() {
    read();
    work();
    return 0;
}
