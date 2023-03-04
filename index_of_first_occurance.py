haystack = "leetcode"
needle = "leeto"

i = 0
j = len(needle) - 1

while j < len(haystack) :
    if haystack[i : j+1] == needle : print(i)
        break
    else :
        i += 1
        j += 1
else : print(-1)
