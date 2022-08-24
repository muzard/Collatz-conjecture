def collatz(n: int):
    if type(n) == 'float':
        n = n // 1
        print("ha ha funny guy")
    if n <= 0:
        print("this is for positive numbers only!")

    while n != 1:
        print(n)
        if n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            n = 3*n + 1
    print("one")

def collatz_neg(n: int):
    if n >= 0:
        print("this is for negative numbers only!")
        return None

    while n != -1:
        if n == -5 or n == -17:
            print("looks like you entered a cycle")
            return None

        print(n)
        if n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            n = 3*n + 1
    print("-one")