#Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
def strStr(source, target):
    temp =""
    j=0
    for i in range(0,len(source)):
        if temp != target:
            if source[i] == target[j]:
                temp+=target[j]
                j+=1
            else:
                temp=''
                j=-1
        else:
            return i - len(target)
    return -1
print(strStr('sadbutsad','sad'))

