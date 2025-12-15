#include<bits/stdc++.h>
using namespace std;
const int NODE = 1005;

class Point {
public:
    int x, y, z;
    Point(){}
    Point(int x, int y, int z) : x(x), y(y), z(z) {}
    long long dist(Point opp) {
        return (long long)(x - opp.x) * (x - opp.x) +
               (long long)(y - opp.y) * (y - opp.y) +
               (long long)(z - opp.z) * (z - opp.z);
    }
};


class Group{
public:
  int g[NODE];
  int cnt[NODE];

  Group(){}

  void build(int n){
    for(int i=0;i<n;i++){
      g[i] = i;
      cnt[i] = 1;
    }
  }

  int find(int n){
    return (n==g[n] ? n : g[n]=find(g[n]));
  }

  int findCnt(int n){
    return cnt[find(n)];
  }

  void merge(int a, int b){
    if (find(a) == find(b)) {
        return;
    }
    cnt[find(b)] += cnt[find(a)];
    g[find(a)] = find(b);
  }
};


vector<Point> pts;

void read() {
    char ch;
    Point pt;
    while (cin >> pt.x >> ch >> pt.y >> ch >> pt.z) {
        pts.push_back(pt);
    }
}


void work() {
    vector<pair<long long, pair<int, int>>> edges;
    int n = pts.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            edges.push_back({pts[i].dist(pts[j]), {i, j}});
        }
    }
    sort(edges.begin(), edges.end());

    Group group;
    group.build(n);
    for (auto &edge : edges) {
        int u = edge.second.first;
        int v = edge.second.second;
        group.merge(u, v);
        if (group.findCnt(u) == n) {
            cout << 1LL * pts[u].x * pts[v].x << endl;
            break;
        }
    }
}


int main() {
    read();
    work();
    return 0;
}
