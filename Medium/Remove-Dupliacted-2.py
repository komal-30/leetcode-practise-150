#Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
def removeDuplicates(nums):
    previous_elem = nums[0]
    count_curr_elem = 1
    j=1
    for i in range(1,len(nums)):
        curr_elem = nums[i]
        if curr_elem == previous_elem and count_curr_elem == 2:
            continue
        elif curr_elem == previous_elem and count_curr_elem < 2:
            nums[j] = curr_elem
            count_curr_elem+=1
            j+=1
            previous_elem=curr_elem
        else:
            count_curr_elem=1
            nums[j] = curr_elem
            j+=1
            previous_elem=curr_elem
    return j
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
            
