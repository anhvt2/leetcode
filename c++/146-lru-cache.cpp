#include <iostream>
#include <unordered_map>
#include <list>

class LRUCache {
    private:
        int capacity;
        list <pair<int, int>> cacheList; // {key, value}
        unordered_map<int, list<pair <int, int>>::iterator > cacheMap;

    public:
        LRUCache(int capacity) {
            this->capacity = capacity;
        }
        
        int get(int key) {
            if (cacheMap.find(key) == cacheMap.end()) {
                return -1; // not found
            }

            // Move the accessed item to the front of the list
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            return cacheMap[key]->second; // Return the value
        }
        
        void put(int key, int value) {
            if (cacheMap.find(key) != cacheMap.end()){
                // Key exists, update the value and move to front
                cacheMap[key]->second = value;
                cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            }
            else {
                // Key does not exist
                if (cacheList.size() == capacity) {
                    // Remove least recently used item
                    int lruKey = cacheList.back().first;
                    cacheList.pop_back();
                    cacheMap.erase(lruKey);
                }
                // Insert the new key-value pair at the front
                cacheList.emplace_front(key, value);
                cacheMap[key] = cacheList.begin();
            }
        }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */