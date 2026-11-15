class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        res = []

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        for num, freq in freqMap.items():
            buckets[freq].append(num)

        
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res













