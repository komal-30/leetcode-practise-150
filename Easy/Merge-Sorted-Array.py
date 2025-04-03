
#Problem Statement : https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150 



def merge(nums1, m, nums2, n):
        i = m-1 #Last valid index of nums1
        j = n-1 #Last valid index of nums2
        k = m+n-1 #Last valid index of nums1+nums2 
        if m == 0: #Handling the edge case, if the nums1 is empty,just merge nums2 in same order
            i=0
            while i < len(nums2):   
                nums1[i]=nums2[j]
                i+=1
        else: 
            while i>=0 and j>=0:    #Start comparing each element from the end of array
                if nums1[i] > nums2[j]: #If ith element in nums1 > jth element of nums2,replace kth element of final nums1(O/P array) with ith current nums1
                    nums1[k] = nums1[i]
                    i-=1
                else:
                    nums1[k] = nums2[j] #If ith element in nums1 < jth element in num2,replace kth element of final nums1 with jth element in nums2
                    j-=1
                k-=1
        #For running in local
        return nums1
#For running in local
print(merge([1,2,3,0,0,0],3,[2,5,6],3))



#Check for the edge cases failing while submitting to leetcode : https://leetcode.com/problems/merge-sorted-array/submissions/1596015187/?envType=study-plan-v2&envId=top-interview-150 