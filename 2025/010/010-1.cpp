#include<bits/stdc++.h>
using namespace std;


class Machine {
public:
    string light;
    vector<vector<int>> ops;
    vector<int> requirements;
};


vector<Machine> machines;

void read() {
    string line;
    while (getline(cin, line)) {
        Machine machine;
        stringstream ss(line);

        string s;
        ss >> s;

        machine.light = s.substr(1, s.size() - 2);

        while (ss >> s) {
            bool isOp = s[0] == '(';
            for (int i = 0; i < s.size(); ++i) {
                if (!isdigit(s[i])) {
                    s[i] = ' ';
                }
            }
            stringstream innerSS(s);
            int v;
            vector<int> vList;
            while (innerSS >> v) {
                vList.push_back(v);
            }
            if (isOp) {
                machine.ops.push_back(vList);
            } else {
                machine.requirements = vList;
                break;
            }
        }

        machines.push_back(machine);
    }
}


int calc(Machine &machine) {
    const int n = machine.light.size();

    map<string, int> visited;
    queue<string> Q;

    visited[string(n, '.')] = 0;
    Q.push(string(n, '.'));

    while (!Q.empty()) {
        string curr = Q.front();
        Q.pop();


        if (curr == machine.light) {
            return visited[curr];
        }

        for (const vector<int> &op : machine.ops) {
            string next = curr;
            for (int idx : op) {
                next[idx] = next[idx] == '.' ? '#' : '.';
            }
            if (!visited.count(next)) {
                visited[next] = visited[curr] + 1;
                Q.push(next);
            }
        }
    }

    cerr << "Unsolved" << endl;
    return -1;
}


void work() {
    int ans = 0;
    for (Machine &machine : machines) {
        ans += calc(machine);
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
