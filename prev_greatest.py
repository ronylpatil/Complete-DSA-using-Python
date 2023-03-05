nums = [1,2,3,4,3]
prev_greatest = []
stack = []

for i in nums :
    if isEmpty(stack) :
        prev_greatest.append(-1)
        stack.append(i)
        continue

    if i >= top() :
        while i >= top() :
            stack.pop()
            if isEmpty(stack) :
                prev_greatest.append(-1)
                break
        else :
            prev_greatest.append(top())
    else :
        prev_greatest.append(top())
    stack.append(i)

print('prev : ', prev_greatest)
