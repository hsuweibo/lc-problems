from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        # Return the number of subarrays with at most k distinct integers
        def atMostK(array, k):
            left, right = 0, 0
            window_freq = Counter()
            answer = 0
            while right < len(array):
                window_freq[array[right]] += 1

                # If the window now has k + 1 integers, push the left pointer rightward
                while left <= right and len(window_freq) == k + 1:
                    window_freq[array[left]] -= 1
                    if window_freq[array[left]] == 0:
                        del window_freq[array[left]]
                    left += 1

                # This returns the length of a segment (the curr window) that contains k unique integers
                # This length is the same as the number of subarrays in this segment with at most k unique integers
                answer += right - left + 1
                right += 1

            return answer

        return atMostK(A, K) - atMostK(A, K - 1)