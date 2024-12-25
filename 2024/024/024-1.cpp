#include<bits/stdc++.h>
using namespace std;

class Gate {
public:
    string a, op, b;
    Gate(){}
    Gate(string a, string op, string b) : a(a), op(op), b(b) {}
};


map<string, int> input2value;
map<string, Gate> input2gate;

void read() {
    string line;
    while (getline(cin, line)) {
        if (line.length() == 0) {
            break;
        }
        input2value[line.substr(0, 3)] = line[5] - '0';
    }

    string a, op, b, dummy, out;
    while (cin >> a >> op >> b >> dummy >> out) {
        input2value[out] = -1;
        input2gate[out] = Gate(a, op, b);
    }
}


int rec(string in) {
    if (input2value[in] != -1) {
        return input2value[in];
    }

    Gate &gate = input2gate[in];
    int a = rec(gate.a);
    int b = rec(gate.b);

    if (gate.op == "AND") {
        return input2value[in] = a & b;
    } else if (gate.op == "OR") {
        return input2value[in] = a | b;
    } else if (gate.op == "XOR") {
        return input2value[in] = a ^ b;
    }
    return -1;
}


void work() {
    long long ans = 0;

    for (auto [in, gate] : input2gate) {
        input2value[in] = rec(in);
        if (in[0] == 'z' && input2value[in]) {
            int bit = atoi(in.substr(1).c_str());
            ans += 1LL << bit;
        }
    }

    cout << ans << endl;
}


int main() {
    read();
    work();
    return 0;
}
