#include<iostream>
#include<string>
#include<cstring>
using namespace std;
const int REP = 10000;
const int PHASE = 100;
const int ORIG_LEN = 655;
const int BUF = REP * ORIG_LEN;


int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b) {
    return a / gcd(a, b) * b;
}


int len;
int origLen;
int vList[BUF];

void read() {
    string s;
    cin >> s;
    
    len = s.size() * REP;
    origLen = s.size();
    
    int cur = 0;
    for (int i = 0; i < REP; ++i) {
        for (int j = 0; j < s.size(); ++j) {
            vList[cur++] = s[j] - '0';
        }
    }
}


void work() {
    int offset = 0;
    for (int i = 0; i < 7; ++i) {
        offset = offset * 10 + vList[i];
    }
        
    for (int phase = 0; phase < PHASE; ++phase) {
        static int subSum[BUF];
        subSum[0] = vList[0];
        for (int i = 1; i < len; ++i) {
            subSum[i] = subSum[i - 1] + vList[i];
        }
        

        for (int loop = 1; loop <= len; ++loop) {
            int total = 0;

            int idxInPattern = len % (4 * loop);
            if (loop <= idxInPattern && idxInPattern < loop * 2 - 1) {
                int nGet = idxInPattern - loop + 1;
                total += subSum[len - 1] - subSum[len - 1 - nGet];
            }
            if (loop * 3 <= idxInPattern && idxInPattern < loop * 4 - 1) {
                int nGet = idxInPattern - loop * 3 + 1;
                total -= subSum[len - 1] - subSum[len - 1 - nGet];
            }
            
            int patternLen = loop * 4;
            int cycle = lcm(origLen, patternLen);
            
            int idx;
            bool visited[ORIG_LEN] = {};

            idx = (patternLen + loop - 1) % patternLen;
            while (!visited[idx % origLen] && idx + loop - 1 < len) {
                visited[idx % origLen] = true;
                total += (subSum[idx + loop - 1] - (idx == 0 ? 0 : subSum[idx - 1])) * ((len - idx + cycle - 1) / cycle);
                idx += patternLen;
            } 

            idx = (patternLen + loop * 3 - 1) % patternLen;
            memset(visited, 0, sizeof(visited));
            while (!visited[idx % origLen] && idx + loop - 1 < len) {
                visited[idx % origLen] = true;
                total -= (subSum[idx + loop - 1] - (idx == 0 ? 0 : subSum[idx - 1])) * ((len - idx + cycle - 1) / cycle);
                idx += patternLen;
            }
            vList[loop - 1] = abs(total) % 10;
        }
    }

    for (int i = offset; i < offset + 8; ++i)
        cout << vList[i];
    cout << endl;
}


int main() {
    read();
    work();
    return 0;
}
