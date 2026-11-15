class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        res = []

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        
        

        while len(res) != k:
            maxFreq = 0
            maxNum = None
            
            for num, freq in freqMap.items():
                if freq > maxFreq:
                    maxFreq = freq
                    maxNum = num

            res.append(maxNum)
            del freqMap[maxNum]
        
        return res
