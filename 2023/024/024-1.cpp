#include<bits/stdc++.h>
using namespace std;
#define EPS  (1.0e-7)
#define EQ(x,y) (fabs((x)-(y))<EPS)
#define GT(x,y) ((x)>=(y)+EPS)
#define LT(x,y) ((x)<=(y)-EPS)
#define GE(x,y) (GT(x,y) || EQ(x,y))
#define LE(x,y) (LT(x,y) || EQ(x,y))
typedef complex<double> Point;

double PI = acos(-1.0);

class Line {
public:
    Point bgn, end;
    Line(Point bgn, Point end): bgn(bgn), end(end) {}
};

double dot(Point a, Point b){
  return real(conj(a)*b);
}

double cross(Point a, Point b){
  return imag(conj(a)*b);
}

int ccw(Point a, Point b, Point c){
  Point d1 = b-a, d2 = c-a;
  if(GT(cross(d1,d2),0)) return 1;
  if(LT(cross(d1,d2),0)) return -1;
  if(LT(dot(d1,d2),0)) return 2;       // b-a-c
  if(LT(norm(d1),norm(d2))) return -2; // a-b-c
  return 0;                            // a-c-b
}

Point calcIntersect(Line a, Line b){
  Point d1 = Point(a.end-a.bgn), d2 = Point(b.end-b.bgn);

  return a.bgn + d1*cross(b.bgn-a.bgn,d2)/cross(d1,d2);
}

bool isParallel(Line a, Line b){
  return EQ(cross(a.end-a.bgn,b.end-b.bgn),0);
}


int N;
vector<double> px, py, pz, vx, vy, vz;

void read() {
    px = py = pz = vx = vy = vz = vector<double>();

    double a, b, c, d, e, f;
    char ch;
    while (cin >> a >> ch >> b >> ch >> c >> ch >> d >> ch >> e >> ch >> f) {
        px.emplace_back(a);
        py.emplace_back(b);
        pz.emplace_back(c);
        vx.emplace_back(d);
        vy.emplace_back(e);
        vz.emplace_back(f);
    }

    N = px.size();
}


void work() {
    int ans = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            Line a = Line(Point(px[i], py[i]), Point(px[i] + vx[i], py[i] + vy[i]));
            Line b = Line(Point(px[j], py[j]), Point(px[j] + vx[j], py[j] + vy[j]));

            if (isParallel(a, b)) {
                continue;
            }

            Point xp = calcIntersect(a, b);

            double c1 = (xp.real() - a.bgn.real()) / vx[i];
            double c2 = (xp.real() - b.bgn.real()) / vx[j];

            if (GT(c1, 0) && GT(c2, 0) &&
                LE(200000000000000LL, xp.real()) && LE(xp.real(), 400000000000000LL) &&
                LE(200000000000000LL, xp.imag()) && LE(xp.imag(), 400000000000000LL)) {
                ++ans;
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
