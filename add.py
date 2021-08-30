# python add ,sub

a = int(input("enter first number: "))
b = int(input("Enter second number: "))

add = a+b
print('addition:', add)

multi = a*b
print('Multiplication:', multi)

a, b = b, a

print('a: after swap', a)
print('b after swap: ', b)

# swap with temp

temp = x
x = a
a = b

print('a: with temp', b)
print('b with temp: ', x)
