i = 20
print(f'i is {i}')
names = ['Alice', 'Bob', 'Charlie']
print(names[2])
for i in range(5):
    for j in range(i):
        for l in range(j):
            print(l)

s= set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(5)
print(s)

ages = {}
count = 0
while count < 5:
    ages[input('Enter your name: ')] = input('Enter your age:')
    print(ages)
    count +=1