#include<bits/stdc++.h>
using namespace std;


vector<string> strList;
vector<vector<int>> patternList;

void read() {
    string str, patternStr;
    while (cin >> str >> patternStr) {
        for (int i = 0; i < patternStr.size(); ++i) {
            if (patternStr[i] == ',') {
                patternStr[i] = ' ';
            }
        }

        vector<int> pattern;
        stringstream in(patternStr);
        int v;
        while (in >> v) {
            pattern.emplace_back(v);
        }

        string toPushStr;
        vector<int> toPushPattern;
        for (int i = 0; i < 5; ++i) {
            if (i) toPushStr += '?';
            toPushStr += str;
            toPushPattern.insert(toPushPattern.end(), pattern.begin(), pattern.end());
        }

        strList.emplace_back(toPushStr);
        patternList.emplace_back(toPushPattern);
    }
}


long long rec(int idx, int consecutiveDamage, int patternIdx, vector<vector<vector<long long>>> &dp, string &str, vector<int> &pattern) {
    if (idx == str.size()) {
        return (patternIdx == pattern.size() && consecutiveDamage == 0) ||
                (patternIdx == pattern.size() - 1 && pattern.back() == consecutiveDamage);
    }

    long long &ret = dp[idx][consecutiveDamage][patternIdx];
    if (ret != -1) return ret;

    ret = 0;

    if (str[idx] == '#') {
        ret += rec(idx + 1, consecutiveDamage + 1, patternIdx, dp, str, pattern);
    } else if (str[idx] == '.') {
        if (patternIdx < pattern.size() && consecutiveDamage > 0) {
            ret += pattern[patternIdx] == consecutiveDamage ? rec(idx + 1, 0, patternIdx + 1, dp, str, pattern) : 0;
        } else if (consecutiveDamage == 0) {
            ret += rec(idx + 1, 0, patternIdx, dp, str, pattern);
        }
    } else {
        // '?' -> '#'
        ret += rec(idx + 1, consecutiveDamage + 1, patternIdx, dp, str, pattern);

        // '?' -> '.'
        if (patternIdx < pattern.size() && consecutiveDamage > 0) {
            ret += pattern[patternIdx] == consecutiveDamage ? rec(idx + 1, 0, patternIdx + 1, dp, str, pattern) : 0;
        } else if (consecutiveDamage == 0) {
            ret += rec(idx + 1, 0, patternIdx, dp, str, pattern);
        }
    }

    return ret;
}


long long calc(string &str, vector<int> &pattern) {
    // dp[idx][consecutive damage][patternIdx]
    vector dp(str.size(), vector(str.size(), vector(pattern.size() + 1, -1LL)));

    return rec(0, 0, 0, dp, str, pattern);
}


void work() {
    long long ans = 0;
    for (int i = 0; i < strList.size(); ++i) {
        ans += calc(strList[i], patternList[i]);
    }
    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
