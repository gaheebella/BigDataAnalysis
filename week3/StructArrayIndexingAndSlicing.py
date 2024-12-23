import numpy as np

#Basic Slicing and Indexing
arr1 = np.arange(10) #0~9
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

#[start:stop:step]
print(arr1[:6]) #0~5 (6의 직전까지)
print(arr1[0:5]) #0~4
print(arr1[::2]) #처음부터 끝까지 2칸 간격_ 짝수
print(arr1[1::2]) #1부터 끝까지 2칸 간격_ 홀수
print(arr1[1:7:2]) #1~6까지 2칸 간격
print(arr1[-3:9]) #배열의 끝에서 3번째 요소부터 9의 직전인 8까지
print(arr1[:-3]) #처음부터 배열의 끝에서 3번째 요소 직전까지
print(arr1[-3:2:-1]) #배열의 끝에서 3번째 요소부터 시작해 역순으로 2직후인 3까지

print(arr2[:2, :2]) #첫 두 행과 첫 두 열
print(arr2[:, ::-1]) #모든 행을 선택하고 각 행의 열을 역순으로 정렬
print(arr2[:, :]) #전체 행과 열
print(arr2[1, :]) #2행의 모든 열
print(arr2[1, 2]) #2행 3열 값
print(arr3[:2, 1:, :2]) #첫 두개의 3x4 배열 선택, 각 배열에서 2행부터 모든 행, 각 배열에서 1열까지



#Advanced Indexing
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)

#arr[[0, 1, 2]]: 각 차원의 행 인덱스 의미-> 0번째, 1번째, 2번째 행 선택
print(arr[[0, 1, 2], [0, 1, 0]]) #각 행에서 지정된 열을 선택 -> 1행 1열, 2행2열, 3행1열

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(arr)
#rows와 columns 배열을 사용해 선택된 인덱스 쌍에 해당하는 요소 출력
rows = np.array([[0, 0], [3, 3]], dtype = np.intp) #1행, 4행 선택
columns = np.array([[0, 2], [0, 2]], dtype = np.intp) #1열, 3열 선택
print(arr[rows, columns]) #1행의 1열, 1행의 3열, 4행의 1열, 4행의 3열


#np.newaxis는 새로운 차원을 기존의 첫 번째 차원 앞에 추가하여 확장하는 것
np.newaxis is None #np.newaxis는 none과 동일한 역할. 배열 인덱싱 시 새로운 축 추가.
# np.newaxis가 None과 같은지 확인하는 것으로, 결과는 True
arr = np.arange(25).reshape(5, 5)
#np.arange(25)는 0~24의 정수를 포함하는 1차원 배열 ->.reshape(5,5)는 5행5열의 2차원배열로 변환
print(arr)
print(arr.shape)
arr_3d = arr[np.newaxis] #np.newaxis로 새로운 축 추가-> 배열의 첫 번째 차원 앞에 새로운 축 추가되므로 3차원 배열
print(arr_3d.shape) #(5,5)였는데 첫 번째 차원 앞에 새로운 축이 추가되었으므로 (1, 5, 5)

arr = np.arange(10)
print(arr) #1차원 배열
print(arr.shape) #(10, ) : arr이 1차원 배열이고 길이가 10

arr_row = arr[np.newaxis, :] #arr 앞에 새로운 축 추가-> 2차원 배열로 변환
# arr요소를 1x10크기의 행 벡터로 변환 -> 1개의 행과 10개의 열로 구성된 배열로 변환됨
print(arr_row)
print(arr_row.shape) #크기가 (1,10)인 행 벡터

arr_col = arr[:, np.newaxis] #arr의 요소를 열 벡터로 변환
print(arr_col)
print(arr_col.shape) #크기가 (10,1) 인 열 벡터



arr = np.array([[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [9, 10, 11]])
rows = np.array([0, 3], dtype=np.intp) #0번째, 3번째 행 선택
print(rows)
columns = np.array([0, 2], dtype=np.intp) #0번째, 3번째 열 선택
print(columns)
print(rows[:, np.newaxis]) # 배열에 새로운 축 추가. rows 배열을 열 벡터로 변환
print(arr[rows[:, np.newaxis], columns])



#Broadcasting : 브로드캐스팅은 NumPy에서 크기가 다른 배열 간의 연산을 가능하게 해주는 기능
#차원이 맞지 않으면(부족하면) 부족한 차원에 대해 자동으로 1이 채워져 크기가 같아질 수 있음
arr1 = np.array([1, 2, 3, 4, 5]) #(5, )인 1차원 배열
arr2 = np.array([11, 12, 13]) #(3, )인 1차원 배열
# print(arr1 + arr2) 차원이 맞지 않아 연산 불가
arr1_nx = arr1[:, np.newaxis] #arr1을 (5, 1)로 변환하여 열 벡터로 만듦
arr2_nx = arr2[:, np.newaxis] #arr2를 (3, 1)로 변환하여 열 벡터로 만듦
print(arr1_nx)
print(arr2_nx)
print(arr1_nx + arr2) #arr1_nx -> (5, 3), arr2 -> (5, 3)로 자동 확장됨
print(arr2_nx + arr1)


#boolean인덱싱을 사용하여 특정 조건을 만족하는 요소들을 선택
arr = np.arange(12).reshape(3, 4)
print(arr)
ind = arr > 5 #배열의 각 요소가 5보다 큰지 검사-> boolean 값 반환
print(ind)
print(arr[ind]) #boolean배열 ind를 사용하여 arr에서 조건을 만족하는 값(true)들만 선택
print(ind[:, 1]) #ind 배열의 모든 행에서 2번째 열을 선택
print(arr[ind[:, 1]]) #[False False True] 이므로 여기서 true인 행만 반환-> 3번째 행 반환

arr = np.array([[1, 0, 0], [0, 2, 0], [1, 1, 0]])
print(arr)
print(np.nonzero(arr)) #배열에서 0이 아닌 값들의 인덱스 찾기
# array([0, 1, 2, 2]) : 0이 아닌 값들이 있는 행의 인덱스
# array([0, 1, 0, 1])) : 0이 아닌 값들이 있는 열의 인덱스
#즉, (0,0): 1, (1,1): 2, (2,0): 1, (2,1): 1
print(arr[np.nonzero(arr)]) #0이 아닌 값들의 인덱스를 사용해 해당 값들을 추출
print(np.transpose(np.nonzero(arr))) #0이 아닌 값들의 좌표를 전치하여 쌍 반환


arr = np.arange(9).reshape(3, 3)
print(arr)
print(arr > 3)
print(np.nonzero(arr>3))
print((arr>3).nonzero())

arr = np.arange(4).reshape((2, 2))
print(arr)
print(np.transpose(arr))
arr1 = np.ones((1, 2, 3)) #값이 1로 채워진 1x2x3크기의 3차원 배열 생성
print(np.transpose(arr1, (1, 0, 2)).shape) #배열의 차원 순서를 (1, 0, 2)로 변경
# (2, 1, 3)-> 2개의 1x3배열로 구성됨

a = [1, 2, 3]
b = np.array(a)
print(b)
print(b.T)
arr = np.array([a])
print(arr.transpose())


#3차원 배열-> 배열의 layer, 행, 열
arr1 = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]],
                 [[8, 9, 10, 11], [12, 13, 14, 15]]])
print(arr1)
print(arr1[0, 1, 2]) #[1st layer, row, column]


#두 개 다 같은 방식으로 작동함
arr2 = np.transpose(arr1, (1, 0, 2))
print(arr2)
arr3 = arr1.transpose((1, 0, 2))
print(arr3)