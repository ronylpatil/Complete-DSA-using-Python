nums = [5,9,2,7,6,5,1,3,4,8,1]

def isEmpty(stack) :
    if len(stack) == 0 : return True
    else : return False

def top() : return stack[-1]

stack = []
next_grestest = []
for i in nums[-1::-1] :
    if isEmpty(stack) :
        next_grestest.append(-1)
        stack.append(i)
        continue

    if top() <= i :
        while top() <= i :
            stack.pop()
            if isEmpty(stack) :
                next_grestest.append(-1)
                break
        else : next_grestest.append(top())
    else :
        next_grestest.append(top())
    stack.append(i)
        
print(next_greatest[-1::-1])
