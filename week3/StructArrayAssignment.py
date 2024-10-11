import numpy as np

# #튜플 2개가 각각 필드별로 저장됨
# a = np.array([(1, 2, 3), (4, 5, 6)], dtype = 'i8, f4, f8')
# a[1] = (7, 8, 9)
# print(a)
#
# #?는 boolean, s1은 1byte문자열
# #크기가 2인 배열 생성, 모든 필드를 0으로 초기화.
# a = np.zeros(2, dtype= 'i8, f4, ?, S1')
# print(a)

#출력값 중에서
#첫 번째 필드: 0.0 (부동 소수점)
#두 번째 필드: b'0.0' (바이트 문자열 '0.0')
#세 번째 필드: b'' (빈 바이트 문자열)
a = np.zeros(3, dtype=[('a', 'i8'), ('b', 'f4'), ('c', 'S3')])
b = np.ones(3, dtype=[('x', 'f4'), ('y', 'S3'), ('z', 'O')])
b[:] = a #배열 a의 데이터를 배열b에 할당
print(b)




