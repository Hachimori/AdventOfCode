#include<iostream>
#include<list>
#include<set>
#include<string>
using namespace std;
const int MAX_VAL = 1000000;
const int LOOP = 10000000;
// const int MAX_VAL = 9;
// const int LOOP = 100;


list<int> read() {
    string s;
    cin >> s;
    
    list<int> ret;
    for (int i = 0; i < s.size(); ++i) {
        ret.push_back(s[i] - '0');
    }
    
    return ret;
}


void print(list<int> &vList) {
    for (list<int>::iterator it = vList.begin(); it != vList.end(); ++it) {
        cout << *it << ' ';
    }
    cout << endl;
}


void work(list<int> vList) {
    int maxV = *max_element(vList.begin(), vList.end());
    for (int i = maxV + 1; i <= MAX_VAL; ++i) {
        vList.push_back(i);
    }

    list<int>::iterator v2iter[MAX_VAL + 1];
    for (list<int>::iterator it = vList.begin(); it != vList.end(); ++it) {
        v2iter[*it] = it;
    }

    list<int>::iterator cur = vList.begin();
    for (int loop = 0; loop < LOOP; ++loop) {
        // print(vList);
        
        set<int> insertedVal;
        list<int>::iterator insertedIter = cur;
        for (int i = 0; i < 3; ++i) {
            ++insertedIter;
            if (insertedIter == vList.end()) insertedIter = vList.begin();
            insertedVal.insert(*insertedIter);
        }
        
        list<int>::iterator dest;
        int destVal = *cur - 1;
        while (destVal == 0 || insertedVal.count(destVal)) {
            if (destVal == 0) {
                destVal = MAX_VAL;
            } else {
                --destVal;
            }
        }
        dest = v2iter[destVal];
        ++dest;
        
        insertedIter = cur;
        for (int i = 0; i < 3; ++i) {
            ++insertedIter;
            if (insertedIter == vList.end()) insertedIter = vList.begin();
            v2iter[*insertedIter] = dest = vList.insert(dest, *insertedIter);
            ++dest;
        }

        insertedIter = cur;
        ++insertedIter;
        for (int i = 0; i < 3; ++i) {
            if (insertedIter == vList.end()) insertedIter = vList.begin();
            insertedIter = vList.erase(insertedIter);
        }

        ++cur;
        if (cur == vList.end()) cur = vList.begin();
    }

    // print(vList);
    
    list<int>::iterator oneIt = v2iter[1];
    int a = *(++oneIt);
    int b = *(++oneIt);
    cout << 1LL * a * b << endl;
}


int main() {
    work(read());
    return 0;
}
