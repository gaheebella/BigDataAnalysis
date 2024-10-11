import numpy as np

#배열의 요소가 16비트 정수(int16) 타입임을 나타내며, 이는 기본적인 데이터 타입을 지정
print(np.dtype(np.int16))

#하나의 필드 'f1'을 가지는 구조화된 데이터 타입을 정의합니다. 이 필드는 16비트 정수(int16) 타입
#'<i2'는 16비트 정수를 리틀 엔디안 형식으로 저장함을 의미합니다 ('<i2'에서 i는 정수, 2는 2바이트를 나타냄).
print(np.dtype([('f1', np.int16)]))

#중첩된 구조화된 데이터 타입을 정의합니다. 최상위 필드 'f1'은 하위 필드 'f1'을 포함하는 하위 구조를 가집니다. 하위 필드는 16비트 정수(int16) 타입
print(np.dtype([('f1', [('f1', np.int16)])]))

#두 개의 필드를 가지는 구조화된 데이터 타입을 정의합니다. 'f1'은 np.uint(부호 없는 정수) 타입이고,'f2'는 np.int32(32비트 부호 있는 정수) 타입
print(np.dtype([('f1', np.uint), ('f2', np.int32)]))
print(np.dtype([('a', 'f8'), ('b', 'S10')]))
print(np.dtype('i4, (2,3)f8'))
print(np.dtype([('hello',(int, 3)), ('world', np.void, 10)]))

#'x'와 'y'는 각각 8비트(i1) 정수를 나타내며, 이는 16비트 값을 바이트 단위로 분할한 형태
print(np.dtype((np.int16, {'x': (np.int8, 0), 'y': (np.int8, 1)})))
print(np.dtype({'names': ['gender','age'], 'formats': ['S1', np.uint8]}))
print(np.dtype({'surname': ('S25', 0), 'age': (np.uint8, 25)}))


#a: numpy.float32 타입의 스칼라(단일 값)로, 부동소수점 데이터 타입을 명시적으로 정의한 예제입니다.
#b: numpy.ndarray 타입의 배열로, 정수 리스트를 플랫폼 의존적인 기본 정수 타입으로 변환하여 저장한 예제입니다.
#c: numpy.ndarray 타입의 배열로, 0부터 4까지의 정수 배열을 16비트 부호 없는 정수 타입으로 생성한 예제입니다.
a = np.float32(5.0)
print(type(a))
b = np.int_([1, 2, 3])
print(type(b))
c = np.arange(5, dtype = np.uint16)
print(type(c))


# >는 빅 엔디안 -> 데이터가 메모리에 저장될 때 상위 바이트부터 저장됨
# i4 == 4byte 정수형 == int32 bit
dt = np.dtype('>i4')
print(dt.byteorder) #메모리에 저장될 때의 바이트 순서
print(dt.name)
print(dt.itemsize) #데이터크기(바이트)
print(dt.type is np.int32)

#np.dtype는 NumPy에서 사용되는 데이터 타입을 정의하는 클래스
#name이라는 필드, 문자열타입, 길이가 16인 문자열 저장
#grades라는 필드, float64타입, 크기가 (2,)인 배열(2개의 실수)을 저장 가능
#첫 번째 필드 name은 길이가 16인 유니코드 문자열이고,
#두 번째 필드 grades는 크기가 2인 float64 배열입니다.
dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
print(dt['name']) #name필드의 데이터타입 정보 출력, 리틀엔디안이고 길이가 16인 유니코드 문자열 타입
print(dt['grades']) #(2, )는 2개의 요소를 가진 배열, f8 == float64 bit, 리틀엔디안
