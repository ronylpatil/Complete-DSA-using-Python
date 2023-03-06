nums = [1,4,6,2,3,8,7,5]

stack = []

def isEmpty(stack):
    if len(stack) == 0 : return True
    else : return False

for i in nums[-2::-1] :
    if isEmpty(stack) :
        stack.append(i)
    else :
        if stack[-1] <= i :
            while stack[-1] <= i :
                stack.pop()
                if isEmpty(stack) : break
        stack.append(i)

next_greatest = []
for i in nums[-1::-1] :
    if isEmpty(stack) :
        next_greatest.append(-1)
    else :
        if stack[-1] <= i :
            while stack[-1] <= i :
                stack.pop()
                if isEmpty(stack) :
                    next_greatest.append(-1)
                    break
            else :
                next_greatest.append(stack[-1])
        else :
            next_greatest.append(stack[-1])
    stack.append(i)

print(next_greatest[-1::-1])
