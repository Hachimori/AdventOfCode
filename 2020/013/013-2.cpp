#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#define rem first
#define mod second
using namespace std;
typedef pair<int, int> RemMod;


class Data{
public:
  long long d, x, y;
  Data(){}
  Data(long long d, long long x, long long y): d(d), x(x), y(y) {}
};

Data extendGCD(long long a, long long b) {
  if (b == 0) return Data(a, 1, 0);
  Data ret = extendGCD(b, a % b);
  return Data(ret.d, ret.y, ret.x - a / b * ret.y);
}


vector<RemMod> read() {
    vector<RemMod> remMod; // (reminder, mod)
    
    int dummy;
    cin >> dummy;

    string s;
    cin >> s;

    replace(s.begin(), s.end(), ',', ' ');
    
    istringstream in(s);
    for (int i = 0; ; ++i) {
        string st;
        if (!(in >> st)) break;
        if (st == "x") continue;
        int mod = atoi(st.c_str());
        remMod.push_back(make_pair((mod + (-i) % mod) % mod, mod));
    }

    return remMod;
}


long long chineseReminderTheorem(vector<RemMod> remMod) {
    long long rem = 0;
    long long mod = 1;

    for (int i = 0; i < remMod.size(); ++i) {
        Data data = extendGCD(mod, remMod[i].mod);
        assert((remMod[i].rem - rem) % data.d == 0); // no answer
        long long t = (remMod[i].rem - rem) / data.d * data.x % (remMod[i].mod / data.d);
        rem += mod * t;
        mod *= remMod[i].mod / data.d;
    }

    return (rem % mod + mod) % mod;
}


void work(vector<RemMod> remMod) {
    cout << chineseReminderTheorem(remMod) << endl;
}


int main() {
    work(read());
    return 0;
}
