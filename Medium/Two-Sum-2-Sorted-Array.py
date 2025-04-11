#Link:https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    while(left<right):
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1,right+1]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return [-1,-1]
print(twoSum([2,7,11,15],9))    



