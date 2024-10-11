import numpy as np

#Tuple: (name, datatype, shape)
print(np.dtype([('a', 'f4'), ('b', np.float32), ('c','f4', (2,2))]))
print(np.dtype([('a', 'f4'), ('', 'i4'), ('c', 'i8')]))

#comma-seperated dtype string
print(np.dtype('i8, f4, S3'))
print(np.dtype('3int8, float32, (2,3)float64'))

#Dictionary
#offsets: 메모리에서 각 필드가 저장되는 위치-> 각 필드가 데이터의 시작 지점에서 몇 바이트 떨어져 있는지 지정
#itemsize: 전체 아이템 크기
print(np.dtype({'names': ['col1', 'col2'], 'formats': ['i4', 'f4']}))
print(np.dtype({'names': ['col1', 'col2'], 'formats': ['i4', 'f4'], 'offsets': [0, 4], 'itemsize': 12}))

#if field name is dictionary
#key: field name, value: (datatype, value)
print(np.dtype({'col1': ('i1', 0), 'col2': ('f4', 1)}))

c = np.dtype([('a', 'i8'), ('b', 'f4')])
print(c.names)
print(c.fields)

def print_offsets(d):
    print("offsets: ", [d.fields[name][1] for name in d.names])
    #name필드의 1번째 인덱스에 해당하는 값이 바이트 위치(=메모리 오프셋)
    #d.names(각 필드의 이름 목록-> 여기선 튜플을 반환)에 포함된 필드 이름을 하나씩 꺼내서 name이라는 변수에 할당하여 루프를 실행
    print("itemsize: ", d.itemsize)

print_offsets(np.dtype('u1, u1, i4, u1, i8, u2'))
d = np.dtype('u1, u1, i4, u1, i8, u2')
print(d)
print(d.itemsize)
print(d.fields)
print(d.names)
print(d.fields['f0'])
print(d.fields['f0'][1])
print_offsets(np.dtype('u1, u1, i4, u1, i8, u2', align = True))


x = np.dtype([(('my title', 'name'), 'f4')]) #my title은 필드의 의미를 설명하기 위한 메타데이터
print(x.fields) #각 필드에 대한 데이터타입, 오프셋, 제목정보를 딕셔너리로 반환
print(x.names) #필드 이름 반환

print(np.dtype({'name': ('i4', 0, 'my title')})) #필드 이름, 데이터타입, 오프셋, 제목지정
