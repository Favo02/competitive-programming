#include <bits/stdc++.h>
using namespace std;

typedef map<string,string> attributes;
typedef map<string,string> parent;
typedef map<string,attributes> tags;

int main() {
  int t, q;
  cin >> t >> q;

  string null;
  getline(cin, null);

  tags tgs;
  parent par;

  string open = "";

  while (t-- > 0) {
    string line;
    getline(cin, line);
    line = line.substr(1, line.size()-2);

    if (line[0] == '/') {
      line = line.substr(1, line.size());

      open = par[line];

      continue;
    }

    size_t pos = 0;
    vector<string> tokens;
    while ((pos = line.find(" ")) != string::npos) {
      tokens.push_back(line.substr(0, pos));
      line.erase(0, pos + 1);
    }
    tokens.push_back(line.substr(pos+1, line.size()));

    attributes attr;
    for (size_t i = 1; i < tokens.size(); i+=3) {
      attr[tokens[i]] = tokens[i+2].substr(1, tokens[i+2].size()-2);
    }
    tgs[tokens[0]] = attr;

    par[tokens[0]] = open;
    open = tokens[0];
  }

  while (q-- > 0) {
    string line;
    getline(cin, line);

    vector<string> nesting;

    size_t pos = 0;
    while ((pos = line.find(".")) != string::npos) {
      nesting.push_back(line.substr(0, pos));
      line.erase(0, pos + 1);
    }

    size_t attrPos = line.find("~");
    if (attrPos == string::npos) {
      nesting.push_back(line.substr(pos+1, line.size()));
    }
    else {
      nesting.push_back(line.substr(pos+1, attrPos));
    }

    string att = line.substr(attrPos+1, line.size());

    bool valid = true;

    for (size_t i = nesting.size()-1; i > 0; i--) {
      string child = nesting[i];
      string parent = nesting[i-1];

      if (par[child] != parent) {
        valid = false;
        break;
      }
    }

    if (valid && par[nesting[0]] != "") {
      valid = false;
    }

    if (valid && tgs[nesting[nesting.size()-1]].count(att) < 1) {
      valid = false;
    }

    if (valid) {
      cout << tgs[nesting[nesting.size()-1]][att] << "\n";
    }
    else {
      cout << "Not Found!\n";
    }
  }
}
