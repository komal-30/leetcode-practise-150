def removeDuplicates(nums):
    #First element
    temp_index = 1

    #We will have atleast one unique element so start with 1
    size = 1

    #If the array is empty just return 0
    if len(nums) == 0:
        return 0
    else:
        #First iteration : First element is previous_element 
        previous_element = nums[0]
        #Iterate from second element of array
        for i in range(1,len(nums)):
            current_element = nums[i]
            #Since the array is sorted in increasing order, the next valid element will be > previous_element
            if(current_element>previous_element):
                #If the valid element , replace it with that index in the same array
                nums[temp_index] = current_element
                temp_index+=1
                #Change the previous element 
                previous_element=current_element
                #To track unique elements we add to the same array
                size+=1
    return size
#Testing
print(removeDuplicates([1,1,2]))






    