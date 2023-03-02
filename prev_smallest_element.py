height = [2,1,5,6,2,3]

stack = []
prev_smallest = []

def isEmpty(stack) :
    if stack : return False
    else : return True

for i in height :
    if isEmpty(stack) :
        prev_smallest.append(-1)
        stack.append(i)
        continue

    if i < stack[-1] :
        while i < stack[-1] :
            stack.pop()
            if isEmpty(stack) :
                prev_smallest.append(-1)
                break
        else :
            prev_smallest.append(stack[-1])
        stack.append(i)
    else :
        prev_smallest.append(stack[-1])
        stack.append(i)

print(height)
print(prev_smallest)
