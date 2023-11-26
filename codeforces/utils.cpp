#include <bits/stdc++.h>
using namespace std;

/*
read a vector of integers from stdin

@param int len: size of vector to parse
*/
vector<int> read_vector(int len) {
  vector<int> arr;
  int n;
  while (len-- > 0) {
    cin >> n;
    arr.push_back(n);
  }
  return arr;
}

/*
print a vector of integers to stdout
each element separated by " "
newline added at vector end

@param vector<int> arr: vector to print
*/
void print_vector(const vector<int>& arr) {
  for (int n : arr)
    cout << n << " ";
  cout << "\n";
}

/*
print a map of integers to intergers to stdout
each key, value in format: "key: value"
each pair on a new line

@param map<int,int> map: map to print
*/
void print_map(const map<int,int>& map) {
  for (pair<int,int> pair : map)
    cout << pair.first << ": " << pair.second << "\n";
}

// --- input ---
// getline(cin, str)  get a whole line into str

// --- vectors ---
// vector<type>
// begin()                            start iterator
// end()                              end+1 iterator
// size()                             size
// push_back(elem)                    append
// empty()                            if empty
// rbegin()                           reverse iterator
// rend()                             start-1 reverse iterator
// front()                            first elem
// back()                             last elem
// pop_back()                         pop from end
// insert(iter pos, val)              insert
// erase(iter start, iter end)        remove
// clear()                            clear
// iter_swap(iter, iter)              swap elems
// count(iter start, iter end, elem)  count occs of elem (>= 1 in map, < 1 not in map)

// --- maps ---
// map<key,value>
// begin()          start iterator
// end()            end+1 iterator
// empty()          if empty
// erase(key)       remove key
// clear()          clear
// count(key)       check if key in map (1 in map, 0 not in map)

// --- pairs ---
// pair<t1,t2>
// make_pair(elem, elem)  create pair
// first()                first elem
// second()               second elem

// --- tuples ---
// tuple<t1,t2,t3,...>
// make_tuple(e1,e2,e3,...)   create tuple
// get<pos>(tuple)            get elem

// --- strings ---
// +          concatenation
// length()   length
