#include<bits/stdc++.h>
using namespace std;

vector<int> row;
vector<int> col;
vector<int> totalShape;


void read() {
    for (int i = 0; i < 30; ++i) {
        string line;
        getline(cin, line);
    }

    char ch;
    int r, c;
    while (cin >> r >> ch >> c >> ch) {
        int shape = 0;
        for (int i = 0; i < 6; ++i) {
            int v;
            cin >> v;
            shape += v;
        }
        row.push_back(r);
        col.push_back(c);
        totalShape.push_back(shape);
    }
}


void work() {
    int cnt = 0;
    for (int i = 0; i < row.size(); ++i) {
        cnt += totalShape[i] <= (row[i] / 3) * (col[i] / 3);
    }
    cout << cnt << endl;
}


int main() {
    read();
    work();
    return 0;
}
