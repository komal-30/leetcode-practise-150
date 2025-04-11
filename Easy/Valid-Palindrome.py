def isPalindrome(s):
    fin = ""
    if len(s.strip())<=1 and not s.isalpha():
        return True
    for ch in s:
        if ch.isalpha():
            fin+=ch
        else:
            return False
    if fin[::-1].lower() == fin.lower() and fin.isalpha():
        return True
    return False
print(isPalindrome(" "))




