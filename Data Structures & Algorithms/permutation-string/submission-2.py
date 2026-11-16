class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freqDict = {}
        windowCount = {}

        for char in s1:
            if char not in freqDict:
                freqDict[char] = 1
            else:
                freqDict[char] += 1

        k = len(s1)

        for char in s2[:k]:
            if char not in windowCount:
                windowCount[char] = 1
            else:
                windowCount[char] += 1
        
        if windowCount == freqDict:
            return True

        for i in range(k, len(s2)):     
            if s2[i] not in windowCount:
                windowCount[s2[i]] = 1
            else: 
                windowCount[s2[i]] += 1

            windowCount[s2[i-k]] -= 1
            if windowCount[s2[i-k]] == 0:
                del windowCount[s2[i-k]]
            
            if windowCount == freqDict: 
                return True
        
        return False

        # more optimal solution would be to init a dictionary of frequencies
        # use sliding window to keep track of frequencies of 3 chars in window
        # if frequency dict equals the frequency dict of s1 then return true
        # else decrement the frequency of char leaving dict and
        # increment the frequency of the char entering the dictionary