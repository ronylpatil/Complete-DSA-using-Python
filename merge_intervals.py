intervals = [[1,4],[2,3]]
stack = []
intervals = sorted(intervals, key = lambda x : x[0])

def isEmpty(stack) :
    if stack : return False
    else : return True
    
for i in intervals :
    if isEmpty(stack) :
        stack.append(i)
    else :
        if stack[-1][1] >= i[0] and stack[-1][1] >= i[1] :
            continue
        elif stack[-1][1] >= i[0] and stack[-1][1] <= i[1] :
            stack[-1][1] = i[1]
        else :
            stack.append(i)

print(stack)
