height = [4,2,0,3,2,5]
lmax = []
rmax = []

LMAX = 0
RMAX = 0


for i in range(0, len(height)) :
    if i == 0 :
        lmax.append(0)
        if LMAX < height[i] :
            LMAX = height[i]
        continue

    if height[i] > LMAX :
        lmax.append(0)
        LMAX = height[i]
    else :
        lmax.append(LMAX)

for i in range(-1, -len(height) - 1, -1) :
    if i == -1 :
        rmax.insert(0, 0)
        if height[i] > RMAX :
            RMAX = height[i]
        continue

    if height[i] >= RMAX :
        rmax.insert(0, 0)
        RMAX = height[i]
    else :
        rmax.insert(0, RMAX)

total = 0
for ht, lmx, rmx in zip(height, lmax, rmax) :
    if lmx == 0 or rmx == 0 :
        continue
    else :
        total += min(lmx, rmx) - ht

print(total)


# Time Complexity - O(n)
# Space Complexity - O(n)
