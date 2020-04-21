print('hello world')
name = input()
print(f'hello, {name}!')
#format string
i = 28
print(f'i is {i}')

x = int(input('Enter a number: '))

if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else: 
    print('x is zero')

ages ={'Alice': 22, 'Bob':27}
ages['Charlie'] = 30
ages['Alice'] +=1

print(ages)