#Link : https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        base_element = strs[0]
        ls=""
        if len(strs) == 1:
               return strs[0]
        else:
            for i in range(1,len(strs)):
                    current_elemnt = strs[i]
                    ls=""
                    for j in range(0,len(current_elemnt)):
                            if(base_element[j] == current_elemnt[j]):
                                    ls+=current_elemnt[j]
                            elif(j == 0):
                                    return ""
                            else:
                                   break
                    base_element=ls
                    
            return ls if ls.strip() != "" else ""
print(longestCommonPrefix(["aaa","aa","aaa"]))

                
        