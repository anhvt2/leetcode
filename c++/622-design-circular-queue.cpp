#include <vector>
using namespace std;

class MyCircularQueue {
private:
    vector<int> data;
    int head;
    int count;
    int capacity;
public:
    MyCircularQueue(int k) {
        data.resize(k);
        head = count = 0;
        capacity = k;
    }
    
    bool enQueue(int value) {
        if (isFull()) return false;
        int tail = (head + count) % capacity;
        data[tail] = value;
        count++;
        return true;
    } 
    
    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % capacity;
        count--;
        return true;
    }
    
    int Front() {
        return isEmpty() ? -1: data[head];
    }
    
    int Rear() {
        if (isEmpty()) return - 1;
        int tail = (head + count - 1) % capacity;
        return data[tail];
    }
    
    bool isEmpty() {
        return count == 0;        
    }
    
    bool isFull() {
        return count == capacity;
    }
};
