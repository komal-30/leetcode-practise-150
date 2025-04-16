#Link: https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
def isSubsequence(s, t):
    prev_ind = 0
    counts=0
    for i in s:
        if i in t and t.index(i) >= prev_ind:
            counts+=1
            prev_ind = t.index(i)
        else:
            return False
    return True if counts==len(s) else False
print(isSubsequence("aaaaaa","bbaaaa"))