#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

template <class T>
class Heap {

    vector<T> arr;

    int   leftchild(int pos)  { return 2 * pos; }
    int   rightchild(int pos) { return 2 * pos + 1; }
    int   parent(int pos)     { return pos / 2; }
    bool  ishead(int pos)     { return pos == 1; }
    bool  inheap(int pos)     { return pos < arr.size(); }
    // If a node's left child is out of the heap,
    // then it is a leaf!
    bool  isleaf(int pos)     { return !inheap(leftchild(pos)); }

    public:

    // Construct an empty heap
    Heap() {
        arr = vector<T>(1, T());
    }

    // Print all elements in the heap
    void printall() {
        for (T x : arr) {
            cout << x << ' ';
        }
    }

    // Bubble up an element in the heap after an insert.
    void bubble_up(int pos) {
        // If this is the head, do nothing.
        if(!ishead(pos)){
            int par = parent(pos);
            // If the current element is greater than the element
            // above, then bubble up.
            if(arr[pos] > arr[par]) {
                swap(arr[pos], arr[par]);
                bubble_up(par);
            }
        }
    }
    
    // Insert an element to the heap
    void insert(T val) {
        arr.push_back(val);
        int pos = arr.size() - 1;
        bubble_up(pos);
    }

    int size() {
        return arr.size() - 1;
    }

    bool empty() {
        return size() == 0;
    }

    T peek_max() {
        return arr[1];
    }

    void bubble_down(int pos) {
        // A normal case, have both left and right child
        if(inheap(leftchild(pos)) && inheap(rightchild(pos))) {
            // Choose the greater child
            int greaterchild = (arr[leftchild(pos)] < arr[rightchild(pos)])? rightchild(pos):leftchild(pos);
            // Compare it with the current position
            if(arr[greaterchild] > arr[pos]) {
                // If bottom is higher, swap!
                swap(arr[greaterchild], arr[pos]);
                bubble_down(greaterchild);
            }

        }
        // Leaf case, only have left child
        else if(inheap(leftchild(pos))) {
            if(arr[leftchild(pos)] > arr[pos]) {
                swap(arr[leftchild(pos)], arr[pos]);
            }
        }
        // The base case, there is no element in the bottom!
        else {
            return;
        }

        // Note that this can be made more efficient by 
    }

    void pop_max() {
        arr[1] = arr[arr.size() - 1];
        arr.pop_back();
        bubble_down(1);
    }

};

// Driver function :
// small test.
int main() {
    int size;
    cin >> size;
    Heap<float> h = Heap<float>();
    for(int i = 1; i <= size; i++) {
        h.insert(float(i) / 10);
    }
    for(int i = 1; i <= size; i++) {
        h.insert(i);
    }
    for(float i = size; i > 0; i -= 2.5) {
        h.insert(i);
    }
    while(!h.empty()) {
        float val = h.peek_max();
        cout << val << ' ';
        h.pop_max();
    }
}