def isPalindrome(s):
    fin = ""
    for ch in s:
            if ch.isalpha() or ch.isdigit():  # or add `or ch.isdigit()` if numbers should be allowed
                fin += ch.lower()  # convert to lowercase for case-insensitive check
        
        # Check if the filtered string is a palindrome
    return fin == fin[::-1] 
print(isPalindrome("0P"))




