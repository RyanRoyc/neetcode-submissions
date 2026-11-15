class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        l, r = 0, len(people)-1

        boatCount = 0

        while l <= r:
            if (people[r] + people[l]) <= limit:
                boatCount += 1
                r -= 1
                l += 1
            else:
                r -= 1
                boatCount += 1
            
        return boatCount