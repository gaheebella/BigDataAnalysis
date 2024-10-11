import numpy as np

arr1 = np.arange(10)
print(arr1)
print(arr1[1])
arr2 = np.arange(9).reshape(3, 3) #3x3 2차원 배열
print(arr2)
print(arr2[2]) #arr2의 3행
print(arr2[2, 1]) #arr2의 3행 2열
arr3 = np.reshape(np.arange(24), (2, 3, 4)) #2개의 3x4배열
print(arr3)
print(arr3[1,1,2]) #두 번째 3x4배열의 2행 3열
print(arr3[1][2][3]) #두 번째 3x4배열의 3행 4열

