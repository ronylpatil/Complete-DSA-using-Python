import numpy as np

score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2

score = np.array(score)
print(score[np.argsort(score[:, k])[-1::-1]])
