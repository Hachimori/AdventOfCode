// It took 60 min 18 sec to process input.
//
// Compile command:
//   $ g++ -O2 019-1.cpp
//
// MacBook Pro (15-inch, 2019)
// CPU: 2.6 GHz 6 core intel Corei7
// MEM: 16 GB 2400 MHz DDR4

#include<bits/stdc++.h>
using namespace std;

struct Blueprint {
    int id;
    int costs[4][4];
};


vector<Blueprint> blueprintList;

void read() {
    string line;
    while (getline(cin, line)) {
        for (char &ch : line) {
            if (!isdigit(ch)) {
                ch = ' ';
            }
        }

        Blueprint b;
        memset(&b, 0, sizeof(b));

        stringstream in(line);
        in >> b.id >> b.costs[0][0] >> b.costs[1][0] >> b.costs[2][0] >> b.costs[2][1] >> b.costs[3][0] >> b.costs[3][2];

        blueprintList.emplace_back(b);

        if (blueprintList.size() == 3) {
            break;
        }
    }
}


int rec(int time, vector<int> &res, vector<int> &robots, int costs[4][4], int goal) {
    if (res[3] >= goal) return true;

    int maximumCreate = 0, robot3 = robots[3];
    for (int i = time; i < 32; ++i) {
        maximumCreate += robot3;
        ++robot3;
    }

    if (maximumCreate + res[3] < goal) return false;

    auto createRobot = [&] (int robotId, bool isRevert) {
        for (int i = 0; i < 4; ++i) {
            res[i] += costs[robotId][i] * (isRevert ? +1 : -1);
        }
        robots[robotId] += (isRevert ? -1 : +1);
    };

    auto createResource = [&] (bool isRevert) {
        for (int i = 0; i < 4; ++i) {
            res[i] += robots[i] * (isRevert ? -1 : +1);
        }
    };

    // Create robot i
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (res[j] < costs[i][j]) {
                goto _fail;
            }
        }

        createResource(false);
        createRobot(i, false);
        if (rec(time + 1, res, robots, costs, goal)) {
            return true;
        }
        createRobot(i, true);
        createResource(true);

        _fail:;
    }

    // Do nothing
    createResource(false);
    if (rec(time + 1, res, robots, costs, goal)) {
        return true;
    }
    createResource(true);

    return false;
}


void work() {
    int prod = 1;
    for (Blueprint &b : blueprintList) {
        for (int goal = 0; ; ++goal) {
            vector<int> res(4, 0);
            vector<int> robots(4, 0);
            robots[0] = 1;
            if (!rec(0, res, robots, b.costs, goal)) {
                prod *= goal - 1;
                break;
            }
        }
    }
    cout << prod << endl;
}


int main() {
    read();
    work();
    return 0;
}
