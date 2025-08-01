#include <unordered_map>
#include <list>
using namespace std;

class LFUCache {
private:
    int capacity;
    int minFreq;
    unordered_map<int, pair<int, int>> keyToValFreq;           // key -> {value, freq}
    unordered_map<int, list<int>> freqToKeys;                  // freq -> list of keys (LRU order)
    unordered_map<int, list<int>::iterator> keyToIter;         // key -> iterator in freqToKeys

public:
    LFUCache(int capacity) {
        this->capacity = capacity;
        minFreq = 0;
    }

    int get(int key) {
        if (keyToValFreq.find(key) == keyToValFreq.end())
            return -1;

        // Update frequency
        int val = keyToValFreq[key].first;
        int freq = keyToValFreq[key].second;
        keyToValFreq[key].second++;

        // Remove from old freq list
        freqToKeys[freq].erase(keyToIter[key]);

        // Clean up if freq list becomes empty and update minFreq
        if (freqToKeys[freq].empty()) {
            freqToKeys.erase(freq);
            if (minFreq == freq) minFreq++;
        }

        // Add to new freq list
        freqToKeys[freq + 1].push_front(key);
        keyToIter[key] = freqToKeys[freq + 1].begin();

        return val;
    }

    void put(int key, int value) {
        if (capacity == 0) return;

        if (keyToValFreq.find(key) != keyToValFreq.end()) {
            keyToValFreq[key].first = value;
            get(key);  // Update frequency
            return;
        }

        // Eviction
        if (keyToValFreq.size() >= capacity) {
            // Evict LRU from lowest freq
            int evictKey = freqToKeys[minFreq].back();
            freqToKeys[minFreq].pop_back();

            if (freqToKeys[minFreq].empty())
                freqToKeys.erase(minFreq);

            keyToValFreq.erase(evictKey);
            keyToIter.erase(evictKey);
        }

        // Insert new key
        keyToValFreq[key] = {value, 1};
        freqToKeys[1].push_front(key);
        keyToIter[key] = freqToKeys[1].begin();
        minFreq = 1;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
