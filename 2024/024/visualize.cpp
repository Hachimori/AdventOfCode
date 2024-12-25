// Used GraphVis to visualize graph

#include<bits/stdc++.h>
using namespace std;
const int NO_LABEL = 1<<30;


class Edge {
public:
    int dst, cost;
    Edge(int dst, int cost): dst(dst), cost(cost){}
};


class Graph {
public:
    int n;
    bool isDirectGraph;
    vector< vector<Edge> > edge;
    vector<string> label;
    vector<string> shape;

    Graph() {}
    Graph(int nNode) {
        n = nNode;
        isDirectGraph = true;
        edge.assign(n, vector<Edge>());
        label.assign(n, string());
        shape.assign(n, string());
    }

    // directed graph かどうかのフラグをセット
    void setDirectGraph(bool toSet) {
        isDirectGraph = toSet;
    }

    // s -> t, コストcost の辺を追加
    void addEdge(int s, int t, int cost=NO_LABEL) {
        edge[s].push_back(Edge(t, cost));
    }

    // node にラベルsを追加
    void setLabel(int node, string s) {
        label[node] = s;
    }

    // node にshape sを追加
    void setShape(int node, string s) {
        shape[node] = s;
    }

    // ファイル名 filename に画像を出力
    void output(string filename="") {
        if (filename.empty()) {
            filename = "output.png";
        }

        ofstream out("tmp.dot");

        // dotファイルの出力(graph)
        out << (isDirectGraph ? "digraph" : "graph") << " {" << endl;

        // dotファイルの出力(node)
        for (int i = 0; i < n; ++i) {
            out << i << "[";
            if (!shape[i].empty())
                out << " shape = " << shape[i] << ", ";
            if (!label[i].empty())
                out << " label = \"" << label[i] << "\",";
            out << "];";
        }

        // dotファイルの出力(edge)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < edge[i].size(); ++j) {
                Edge &e = edge[i][j];
                out << i
                    << (isDirectGraph ? " -> " : " -- ")
                    << e.dst;
                if (e.cost != NO_LABEL) {
                    out << " [ label = \"" << e.cost << "\" ]";
                }
                out << ";" << endl;
            }

        out << "}" << endl;

        out.close();

        // GraphVis を使って dot ファイルを画像に変換
        system(("dot -Tpng tmp.dot -o " + filename).c_str());

        // dot ファイルの削除
        system("rm tmp.dot");
    }
};



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


void work() {
    vector<string> idx2input;

    for (auto [in, value] : input2value) {
      idx2input.push_back(in);
    }

    Graph graph(input2value.size());
    graph.setDirectGraph(true);

    for (int i = 0; i < idx2input.size(); ++i) {
        graph.setLabel(i, idx2input[i]);
    }

    for (auto [in, gate] : input2gate) {
        int out = find(idx2input.begin(), idx2input.end(), in) - idx2input.begin();
        int a = find(idx2input.begin(), idx2input.end(), gate.a) - idx2input.begin();
        int b = find(idx2input.begin(), idx2input.end(), gate.b) - idx2input.begin();

        graph.addEdge(a, out);
        graph.addEdge(b, out);
        graph.setLabel(out, in + "\n" + gate.op);
    }

    graph.output();
}


int main() {
    read();
    work();
    return 0;
}
