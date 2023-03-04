intervals = [[1,2],[3,5],[6,9],[7,8],[12,16]]
newInterval = [8,10]

intervals.append(newInterval)
intervals = list(sorted(intervals, key = lambda x : x[0]))

def isSubset(x, y) :
    if x[0] <= y[1] and x[1] <= y[1] : return True
    else : return False

def isEmpty(stack) :
    if len(stack) == 0 : return True
    else : return False

stack = []
for i in intervals :
    if isEmpty(stack) :
        stack.append(i)
        continue
    top = stack[-1]
    if top[1] > i[0] :
        if isSubset(i, top) :
            continue
        else :
            top[1] = i[1]
    else :
        stack.append(i)

print(stack)
