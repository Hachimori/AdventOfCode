#include<bits/stdc++.h>
using namespace std;


class Event {
public:
    long long pos;
    int toAdd;
    Event(long long p, int t) : pos(p), toAdd(t) {}
    bool operator< (const Event &other) const {
        return pos < other.pos;
    }
};


vector<pair<long long, long long>> range;

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
}


void work() {
    vector<Event> events;
    for (auto [a, b] : range) {
        events.emplace_back(a, 1);
        events.emplace_back(b + 1, -1);
    }
    sort(events.begin(), events.end());

    long long ans = 0;
    long long lastPos = 0;
    int sum = 0;
    for (int idx = 0; idx < events.size();) {
        int nex = idx;
        int toAdd = 0;
        while (nex < events.size() && events[nex].pos == events[idx].pos) {
            toAdd += events[nex].toAdd;
            ++nex;
        }

        if (sum > 0) {
            ans += events[nex - 1].pos - lastPos;
        }
        lastPos = events[nex - 1].pos;
        sum += toAdd;

        idx = nex;
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
