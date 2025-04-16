#Link: https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150

def canJump(nums):
    if len(nums) <2:
            return True
    index = 0
    value=nums[0]
    iteration=0
    while(iteration<=len(nums) -1):
            iteration+=1
            index = index+value
            if index == len(nums)-1:
                return True
            else:
                if(index>len(nums)-1 and len(nums) == 2 ):
                      return True
                value = nums[index]
    return False
print(canJump([2,0]))
