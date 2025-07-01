import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = 1 + freq.get(word, 0)

        heap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(heap)

        topKWords = [heapq.heappop(heap)[1] for _ in range(k)]
        return topKWords
        
