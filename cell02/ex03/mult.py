x = int(input('Enter the first number : '))
y = int(input('Enter the second number : '))
z = x * y
print(x,'x',y,'=',z)
if z > 0:
    print ( 'The result is positive.')
elif z < 0:
    print('The result is negative.')
else:
    print('The result is both positive and negative.')