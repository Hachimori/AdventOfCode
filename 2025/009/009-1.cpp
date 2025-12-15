#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef pair<int, int> Point;


vector<Point> pts;

void read() {
    Point pt;
    char ch;
    while (cin >> pt.x >> ch >> pt.y) {
        pts.push_back(pt);
    }
}


void work() {
    long long ans = 0;
    int n = pts.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            Point &a = pts[i];
            Point &b = pts[j];
            ans = max(ans, 1LL * (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1));
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
