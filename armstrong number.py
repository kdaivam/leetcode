a = 123
x = a
k = len(str(abs(a)))
s = 0
while a > 0:
    b = a%10
    a = a//10
    s = s + pow(b,k)

if x == s:
    print('equal')
