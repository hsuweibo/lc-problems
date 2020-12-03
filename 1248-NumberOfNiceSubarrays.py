def numberOfSubarrays(nums, k):
    answer = 0
    odd_count = 1
    left = 0
    right = 0
    left_moved = 0

    while right < len(nums):
        if nums[right] % 2 == 1:
            odd_count += 1
            if odd_count >= k:
                left_moved = 1
                while nums[left] % 2 == 0:
                    left_moved += 1
                    left += 1
                answer += left_moved
                left += 1
        else:
            answer += left_moved

        right += 1

    return answer


numberOfSubarrays([1,1,2,1,1], 3)