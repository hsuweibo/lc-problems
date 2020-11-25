

class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1

        count = 0
        while left <= right:
            # If the heaviest person cant be paired with the lightest person, allocate an entire boat to him
            if people[left] + people[right] > limit:
                right -= 1
                count += 1

            # If the lightest person can pair with the heaviest person, he can pair with anyone.
            # So pair him with the heaviest person.
            else:
                right -= 1
                left += 1
                count += 1

        return count