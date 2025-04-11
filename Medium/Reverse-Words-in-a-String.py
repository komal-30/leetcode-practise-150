def reverseWords(s):
    dum = ""
    for character in s:
        if character.isalpha():
            dum+=character
    return dum[::-1]
print(reverseWords("race a car"))

