def strStr(haystack, needle):
    hlength = len(haystack)
    nlength = len(needle)
    for i in range (hlength-nlength+1):
        if ((haystack[i:i+(nlength)]) == needle):
            return i 
    return -1 
v =strStr("sadbutsad", "sad") 
print(v)
# print(sol.strStr("sadbutsad", "sad"))  # Output: 0
# print(sol.strStr("leetcode", "leeto")) # Output: -1
# print(sol.strStr("hello", "ll"))       # Output: 2
# print(sol.strStr("aaaaa", "bba"))      # Output: -1
# print(sol.strStr("abc", ""))           # Output: 0 (Edge case)
