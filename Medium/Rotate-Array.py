#Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
def rotate(nums, k):
    i=0
    j=len(nums)-1
    while(k>0):
        nums[i] = nums[j]
        nums[j] = nums[i]
        i+=1
        j-=1
        k-=1
    return nums
print(rotate([1,2,3,4,5,6,7],3))
