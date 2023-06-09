import math


def strcomp(str1, str2):
    length = min(len(str1), len(str2))
    for i in range(length):
        if str1[i] != str2[i]:
            if i != 0:
                return i
    return -1


print(strcomp("abcd", "abcf"))


def findchar(s, c):
    res = []
    for i in range(len(s)):
        if s[i] == c:
            res.append(i)
    return res


print(findchar("aaaaddxfv", "a"))


def sumN(n):
    if n == 1:
        return 1
    else:
        return n + sumN(n-1)
print(sumN(100))