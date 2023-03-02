height = [1,1]

stack = []
prev_smallest = []

def isEmpty(stack) :
    if stack : return False
    else : return True

# next smallest element
nxt_smallest = []

l = len(height)

for i in range(-1, -len(height) - 1, -1) :
    if isEmpty(stack) :
        nxt_smallest.insert(0, l - 1)
        stack.append(i)
        continue

    if height[stack[-1]] >= height[i] :
        while height[stack[-1]] >= height[i] :
            stack.pop()
            if isEmpty(stack) :
                nxt_smallest.insert(0, l - 1)
                break
        else :
            nxt_smallest.insert(0, l + stack[-1] - 1)
        stack.append(i)
    else :
        nxt_smallest.insert(0, l + stack[-1] - 1)
        stack.append(i)

stack.clear()
for i in range(len(height)) :
    if isEmpty(stack) :
        prev_smallest.append(0)
        stack.append(i)
        continue

    if height[i] <= height[stack[-1]] :
        while height[i] <= height[stack[-1]] :
            stack.pop()
            if isEmpty(stack) :
                prev_smallest.append(0)
                break
        else :
            prev_smallest.append(stack[-1] + 1)
        stack.append(i)
    else :
        prev_smallest.append(stack[-1] + 1)
        stack.append(i)

print(prev_smallest)
print(height)
print(nxt_smallest)

MAX = 0
for ps, ht, ns in zip(prev_smallest, height, nxt_smallest) :
    area = ((abs(ps - ns) + 1) * ht)
    if area > MAX : MAX = area

print(MAX)
