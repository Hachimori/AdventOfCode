#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef pair<int, int> Point;
const double PI = acos(-1);

vector<Point> pts;

void read() {
    Point pt;
    char ch;
    while (cin >> pt.x >> ch >> pt.y) {
        pts.push_back(pt);
    }
}


bool isInside(Point &p) {
    for (int i = 0; i < pts.size(); ++i) {
        Point &a = pts[i];
        Point &b = pts[(i + 1) % pts.size()];
        if (a.x == b.x && a.x == p.x && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y)) return true;
        if (a.y == b.y && a.y == p.y && min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x)) return true;
    }

    double sum = 0;
    for (int i = 0; i < pts.size(); ++i) {
        Point &ap = pts[i];
        Point &bp = pts[(i + 1) % pts.size()];
        complex<double> a(ap.x - p.x, ap.y - p.y);
        complex<double> b(bp.x - p.x, bp.y - p.y);
        sum += arg(b / a);
    }

    return fabs(sum - 2 * PI) < 1e-9;
}


bool hasCross(Point bgn, Point end) {
    for (int i = 0; i < pts.size(); ++i) {
        Point &a = pts[i];
        Point &b = pts[(i + 1) % pts.size()];
        if (bgn.x == end.x && a.y == b.y && min(bgn.y, end.y) < a.y && a.y < max(bgn.y, end.y) && min(a.x, b.x) < bgn.x && bgn.x < max(a.x, b.x)) {
            return true;
        }
        if (bgn.y == end.y && a.x == b.x && min(bgn.x, end.x) < a.x && a.x < max(bgn.x, end.x) && min(a.y, b.y) < bgn.y && bgn.y < max(a.y, b.y)) {
            return true;
        }
    }
    return false;
}


void work() {
    long long ans = 0;
    int n = pts.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            Point &a = pts[i];
            Point &b = pts[j];

            vector<Point> toCheck;
            toCheck.push_back(Point(min(a.x, b.x), min(a.y, b.y)));
            toCheck.push_back(Point(min(a.x, b.x), max(a.y, b.y)));
            toCheck.push_back(Point(max(a.x, b.x), max(a.y, b.y)));
            toCheck.push_back(Point(max(a.x, b.x), min(a.y, b.y)));

            for (int k = 0; k < 4; ++k) {
                if (!isInside(toCheck[k])) {
                    goto _fail;
                }
            }

            for (int k = 0; k < 4; ++k) {
                if (hasCross(toCheck[k], toCheck[(k + 1) % 4])) {
                    goto _fail;
                }
            }
            ans = max(ans, 1LL * (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1));

            _fail:;
        }
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
