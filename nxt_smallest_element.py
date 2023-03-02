height = [2,1,5,6,2,3]
stack = []
prev_smallest = []

def isEmpty(stack) :
    if stack : return False
    else : return True

# next smallest element
nxt_smallest = []
for i in height[-1::-1] :
    if isEmpty(stack) :
        nxt_smallest.insert(0, -1)
        stack.append(i)
        continue

    if stack[-1] > i :
        while stack[-1] > i :
            stack.pop()
            if isEmpty(stack) :
                nxt_smallest.insert(0, -1)
                break
        else :
            nxt_smallest.insert(0, stack[-1])
        stack.append(i)
    else :
        nxt_smallest.insert(0, stack[-1])
        stack.append(i)

print(height)
print(nxt_smallest)
