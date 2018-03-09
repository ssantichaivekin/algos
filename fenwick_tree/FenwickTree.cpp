#include<iostream>
#include<vector>

using namespace std;

class FenwickTree {
    vector<int> A;
    int size;

    public:
    FenwickTree(int n) {
        A = vector<int>(n+1, 0);
        size = n;
    }
    void update(int pos, int val) { for(; pos <= size; pos += pos & -pos) { A[pos] += val; } }
    int sum(int pos) { int sum = 0; for(; pos > 0; pos -= pos & - pos) { sum += A[pos]; } return sum; }
    int range(int i, int j) { return sum(j) - sum(i-1); }
};

int main() {
    int n, k;
    cin >> n >> k;
    FenwickTree tree = FenwickTree(n);
    for(int i = 0; i < k; i++) {
        int pos, val;
        cin >> pos >> val;
        tree.update(pos, val);
    }
    cin >> n;
    for(int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        cout << tree.range(x, y) << "\n";
    }
}