#include<iostream>
#include<algorithm>
#include<sstream>
using namespace std;
const int CASE = 1000;


int nCase = 0;
string pattern[CASE][10], word[CASE][4];


void read() {
    while (1) {
        string s;
        if (!getline(cin, s)) break;

        istringstream in(s);
        for (int i = 0; i < 10; ++i) {
            in >> pattern[nCase][i];
        }

        char dummy; in >> dummy;

        for (int i = 0; i < 4; ++i) {
            in >> word[nCase][i];
        }
        
        ++nCase;
    }
}


int getValue(string p[10], string w[4], int mapping[7]) {
    static int v2mask[10] =
        {
         1 | 2 | 4 | 0 | 16 | 32 | 64, // 0
         0 | 0 | 4 | 0 |  0 | 32 |  0, // 1
         1 | 0 | 4 | 8 | 16 |  0 | 64, // 2
         1 | 0 | 4 | 8 |  0 | 32 | 64, // 3
         0 | 2 | 4 | 8 |  0 | 32 |  0, // 4
         1 | 2 | 0 | 8 |  0 | 32 | 64, // 5
         1 | 2 | 0 | 8 | 16 | 32 | 64, // 6
         1 | 0 | 4 | 0 |  0 | 32 |  0, // 7
         1 | 2 | 4 | 8 | 16 | 32 | 64, // 8
         1 | 2 | 4 | 8 |  0 | 32 | 64  // 9
        };

    int p2mask[10], w2mask[4];
    for (int i = 0; i < 10; ++i) {
        p2mask[i] = 0;
        for (int j = 0; j < p[i].size(); ++j) {
            p2mask[i] |=  1 << mapping[p[i][j] - 'a'];
        }
    }

    for (int i = 0; i < 4; ++i) {
        w2mask[i] = 0;
        for (int j = 0; j < w[i].size(); ++j) {
            w2mask[i] |=  1 << mapping[w[i][j] - 'a'];
        }
    }

    for (int loop = 0; loop < 10; ++loop) {
        for (int i = 0; i < 10; ++i) {
            if (p2mask[loop] == v2mask[i]) {
                goto _success1;
            }
        }
        return -1;
    _success1:;
    }

    int value = 0;
    for (int loop = 0; loop < 4; ++loop) {
        value *= 10;
        for (int i = 0; i < 10; ++i) {
            if (w2mask[loop] == v2mask[i]) {
                value += i;
                goto _success2;
            }
        }
        return -1;
    _success2:;
    }
    
    return value;
}


void work() {
    int ans = 0;
    
    for (int loop = 0; loop < nCase; ++loop) {
        int mapping[] = {0, 1, 2, 3, 4, 5, 6};

        do {
            int val = getValue(pattern[loop], word[loop], mapping);
            if (val != -1) {
                ans += val;
                break;
            }
        } while(next_permutation(mapping, mapping + 7));
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
