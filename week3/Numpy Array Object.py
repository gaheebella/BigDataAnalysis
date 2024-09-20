import numpy as np

arr1 = np.array([0, 2, 5.5, 7]) #1D
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]]) #2D
#여러 리스트 전달 -> 하나의 리스트 안에 포함시켜야 함
#두 개의 리스트가 하나의 2차원 배열로 생성됨
print(arr2)

arr = np.zeros(6) #0으로 채워진 배열, 요소 6개
print(arr)
print(type(arr)) # arr의 데이터 타입
print(arr.shape) # arr배열의 형태-> 차원과 각 차원에서의 크기-> (6, )는 arr이 1차원 배열이고 그 크기가 6임을 의미
print(arr.dtype) # dtype 속성-> 배열의 요소가 저장된 데이터의 타입

arr = np.ones(shape=(6,2)) #1로 채워진 6행 2열
print(arr)
for i in range(6): #0~5까지 좌표로 채워진 6행 2열
    arr[i] = (i, i)
print(arr)

#np.empty 함수: 초기화 되지 않은 임의의 값들로 채워짐
arr = np.empty((4,2))
print(arr)

arr = np.empty((2,2), dtype = int)
print(arr)

#np.eye 함수: identity matrix 단위행렬(=주대각선이 모두 1, 나머지 요소는 모두 0인 정방행렬) 생성
arr = np.eye(3, dtype = int) #3x3크기의 단위행렬
print(arr)

#np.linspace 함수: 두 개의 숫자 사이에서 지정한 개수만큼의 균등 간격의 숫자들을 생성
#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
#endpoint: (선택, 기본값=True) True로 설정되면 stop 값을 포함. False로 설정하면 stop 값은 포함되지 않고, 그보다 작은 값이 마지막으로 생성
#retstep: (선택, 기본값=False) True로 설정하면 생성된 배열과 함께 간격(step)을 반환
arr = np.linspace(2.0, 5.0, num = 7)
print(arr)

arr = np.linspace(2.0, 5.0, 4, endpoint=False)
print(arr)

arr = np.zeros((2,3))
print(arr)
#arr.reshape(-1): reshape 함수는 배열의 형태를 변경하는 함수.
#(-1)은 NumPy에게 자동으로 배열의 크기를 계산하여 1차원 배열로 변환(평탄화 flatten)
arr = arr.reshape(-1)
print(arr)
arr = arr.reshape(3, -1) #3행으로 flatten
print(arr)
arr = arr.reshape(-1, 1) #1열로 flatten
print(arr)

arr = np.zeros((2,3))
print(arr)
#ravel : 1차원으로 flatten
arr = arr.ravel()
print(arr)

# 3차원 배열 생성
#.reshpae(block(=slice, layer), row, column) -> (z, x, y)
arr = np.arange(24).reshape(2, 3, 4)
print(arr)