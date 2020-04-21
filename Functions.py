#Defining a Function
def cube(x):
    return x**3

def main():
    for i in range(int(input('Enter a value: '))):
        print("{} cubed is {}". format(i, cube(i)))

if __name__ == '__main__':
    main()