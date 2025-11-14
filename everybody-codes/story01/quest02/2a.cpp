#include <bits/stdc++.h>
using namespace std;
#define ll long long

struct Node {
    int id;
    int val;
    string name;
    Node *lc;
    Node *rc;
};

void addchild(Node *root, Node *child) {
    Node *cur = root;
    if (child->val > cur->val) {
        if (cur->rc == nullptr) {
            cur->rc = child;
            return;
        }
        addchild(cur->rc, child);
    } else {
        if (cur->lc == nullptr) {
            cur->lc = child;
            return;
        }
        addchild(cur->lc, child);
    }
}

vector<string> bfs(Node *root) {
    vector<string> lines;
    queue<pair<Node *, int>> queue;
    queue.push({root, 0});
    while (!queue.empty()) {
        auto cur = queue.front();
        queue.pop();
        if (cur.first == nullptr)
            continue;
        if (cur.second >= lines.size()) {
            lines.push_back(cur.first->name);
        } else {
            lines[cur.second] += cur.first->name;
        }
        queue.push({cur.first->lc, cur.second + 1});
        queue.push({cur.first->rc, cur.second + 1});
    }
    return lines;
}

string longest(vector<string> &lines) {
    string res = "";
    for (auto l : lines) {
        if (l.length() > res.length())
            res = l;
    }
    return res;
}

// NOTE: the input is manually simplified to this format
// 3
// ADD 1 10 A 30 H
// ADD 2 15 D 25 I
// ADD 3 12 F 31 J
int main() {
    int lines;
    cin >> lines;
    string op, left_name, right_name;
    int id, left, right;
    ll res = 0;

    Node *lt = nullptr;
    Node *rt = nullptr;

    for (int i = 0; i < lines; i++) {
        cin >> op >> id >> left >> left_name >> right >> right_name;

        Node *leftnode = new Node{id, left, left_name, nullptr, nullptr};
        Node *rightnode = new Node{id, right, right_name, nullptr, nullptr};

        if (i == 0) {
            lt = leftnode;
            rt = rightnode;
        } else {
            addchild(lt, leftnode);
            addchild(rt, rightnode);
        }
    }

    auto llines = bfs(lt);
    auto rlines = bfs(rt);
    cout << longest(llines) << longest(rlines) << endl;
}
