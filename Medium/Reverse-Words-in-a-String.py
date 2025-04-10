#Link :https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
def reverseWords(s):
    fin=""
    rev= list(filter(None,s.strip().split(" ")[::-1]))
    for str in rev:
        fin+=str
        fin+=" "
    return fin
print(reverseWords("a good   example"))