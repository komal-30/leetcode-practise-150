def majorityElement(nums):
    n = len(nums)
    seen = set()  # Track numbers we've already checked
    for num in nums:
        if num not in seen:
            count = nums.count(num)
            if count > n // 2:
                return num
            seen.add(num) 
print(majorityElement([3,2,3]))
    
