def minSubArrayLen(target, nums):
    
    if target in nums:
        return 1
    elif sum(nums) < target or (len(nums)<2 and sum(nums<target)):
        return 0
    else:
        sorted_array = sorted(nums)
        sum_arr = sorted_array[-1] + sorted_array[-2]
        count = 2
        for i in range(len(sorted_array)-3,-2,-1):
                if sum_arr == target or sum_arr>target:
                    return count
                sum_arr += sorted_array[i]
                count+=1
        return 0
print(minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12]))

 