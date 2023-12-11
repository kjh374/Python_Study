'''
* 정수형 (Integer)
- 수치형 타입 중 정수형(int)은 양수, 음수의 정수값을 표현하며
소수점 이하 자리는 표현할 수 없습니다.

- 다른 언어는 저장 범위가 타입마다 정해져 있지만,
파이썬은 메모리가 허용하는 한 무수히 많은 정수를
저장할 수 있습니다.
'''
num = -4321
print(type(num))

# 2진수(0b), 8진수(0o), 16진수(0x)를
# 접두어로 붙여서 여러 진수들을 표현할 수 있습니다.
a = 0b1011
b = 0o77
c = 0xAC00
print(a, b, c)

# 정수를 다른 진법으로 변경하려면
# 2진수 bin(), 8진수 oct(), 16진수 hex() 를 사용합니다.
print(bin(33))
print(oct(0b111001))
print(hex(8923))

'''
* 실수형 (floation point)

- 실수형 자료에는 10진수형 소수점 표현 방식과
지수형 표현방식을 사용한 실수값을 저장할 수 있습니다.
- 범위는 따로 없습니다.
'''

f = 85.432
print(type(f))

g = 9.832e13
print(g)

h = 9.832e-4
print(h)

'''
* 복소수형 (complex)

- 복소수는 제곱해서 음수가 되는 가상의 수
- 허수를 나타내는 접미사는 j를 사용합니다.
'''

i = 1 + 2j
print(type(i))

'''
* 논리형 (boolean)

- 논리형 데이터 타입은 명제가 참이면 True
거짓일 경우 False 값을 가집니다.
'''
b1 = True
b2 = False
# b3 = false (x) / 변수로 인식합니다. (앞글자 대문자로!)

# 파이썬은 문자열도 동등, 비동등 비교가 가능합니다.
# 대/소문자까지 정확하게 일치해야만 True가 리턴됩니다.
password = 'abc1234!'
print(password == 'Abc1234!')


