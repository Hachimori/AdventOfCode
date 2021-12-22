// Compile:
//   $ g++ -O2 022-2.cpp
// Runtime is 1m49.639s
// Environment:
//   - 2.6 GHz 6 core intel Core i7
//   - 16 GB 2400 MHz DDR4 RAM

#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
using namespace std;


class Op {
public:
    bool onOff;
    int x1, x2, y1, y2, z1, z2;
};


vector<Op> opList;

void read() {
    while (1) {
        string s;
        if (!getline(cin, s)) break;

        for (int i = 3; i < s.size(); ++i) {
            if (!(isdigit(s[i]) || s[i] == '-')) {
                s[i] = ' ';
            }
        }

        
        istringstream in(s);
        
        string onOffStr;
        Op op;
        in >> onOffStr >> op.x1 >> op.x2 >> op.y1 >> op.y2 >> op.z1 >> op.z2;
        op.onOff = onOffStr == "on";

        opList.push_back(op);
    }
}



void work() {
    vector<int> xList, yList, zList;
    for (int i = 0; i < opList.size(); ++i) {
        Op &op = opList[i];
        xList.push_back(op.x1);
        xList.push_back(op.x2 + 1);
        yList.push_back(op.y1);
        yList.push_back(op.y2 + 1);
        zList.push_back(op.z1);
        zList.push_back(op.z2 + 1);
    }

    sort(xList.begin(), xList.end());
    xList.erase(unique(xList.begin(), xList.end()), xList.end());
    sort(yList.begin(), yList.end());
    yList.erase(unique(yList.begin(), yList.end()), yList.end());
    sort(zList.begin(), zList.end());
    zList.erase(unique(zList.begin(), zList.end()), zList.end());

    long long total = 0;
    for (int xIdx = 0; xIdx + 1 < xList.size(); ++xIdx) {
        for (int yIdx = 0; yIdx + 1 < yList.size(); ++yIdx) {
            for (int zIdx = 0; zIdx + 1 < zList.size(); ++zIdx) {
                bool isOn = false;
                for (int i = 0; i < opList.size(); ++i) {
                    Op &op = opList[i];
                    if (op.x1 <= xList[xIdx] && xList[xIdx] <= op.x2 &&
                        op.y1 <= yList[yIdx] && yList[yIdx] <= op.y2 &&
                        op.z1 <= zList[zIdx] && zList[zIdx] <= op.z2) {
                        isOn = op.onOff;
                    }
                }
                if (isOn) {
                    total += 1LL * (xList[xIdx + 1] - xList[xIdx]) * (yList[yIdx + 1] - yList[yIdx]) * (zList[zIdx + 1] - zList[zIdx]);
                }
            }
        }
    }

    cout << total << endl;
}


int main() {
    read();
    work();
    return 0;
}
