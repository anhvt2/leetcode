#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int n = arrival.size();
        vector<int> requestCount(k, 0);

        set<int> available;
        for (int i = 0; i < k; ++i) available.insert(i);

        // busy servers: {end_time, server_id}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> busy;

        for (int i = 0; i < n; ++i) {
            int time = arrival[i];
            int duration = load[i];

            // Free up finished servers
            while (!busy.empty() && busy.top().first <= time) {
                available.insert(busy.top().second);
                busy.pop();
            }

            if (available.empty()) continue; // all servers busy, drop request

            int target = i % k;
            auto it = available.lower_bound(target);
            if (it == available.end()) it = available.begin(); // wrap around

            int server = *it;
            available.erase(it);
            requestCount[server]++;
            busy.push({time + duration, server});
        }

        int maxReq = *max_element(requestCount.begin(), requestCount.end());
        vector <int> result;
        for (int i = 0; i < k; ++i) {
            if (requestCount[i] == maxReq)
                result.push_back(i);
        }
        return result;
    }
};