# numerical dataset sort
list1 = ['12', '14', '23', '2', '44']

print(list1)

list2 = [int(x) for x in list1]

print(sorted(list2))


# sequence polindrom
seq = 'MOM'
seq = seq.casefold()
rev_seq = reversed(seq)

print('seq is polindrome' if list(seq) ==
      list(rev_seq) else 'seq not polindrome')


# numeric polindrome
num = 555
temp = num
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num = num // 10

if temp == rev_num:
    print(temp, 'is polindrome ')
else:
    print(temp, 'not a polindrome')

# prime number given
num = 31

if num > 2:
    for x in range(2, int(num/2)+1):
        if num % x == 0:
            print(num, "not a prime")
            break
    else:
        print(num, 'is prime')
else:
    print(num, 'not a prime')

# primes btw two numbers
list1 = []
for num in range(100, 150):
    if all(num % x != 0 for x in range(2, int(num/2)+1)):
        list1.append(num)

print(list1)


# factorial of a number
def fact(num):
    return 1 if (num <= 0 or num == 1) else num * fact(num - 1)


print('fact - ', fact(6))


def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact


print(factorial(6))

# amstrong number

num = 153

for num in range(300, 500):

    temp = num
    sum = 0
    times = len(str(num))

    while num > 0:
        digit = num % 10
        sum += (digit ** times)
        num = num // 10

    if temp == sum:
        print(temp, 'is amstrong')
    else:
        print(temp, 'is not amstrong')


# fibonacci series

a, b = 0, 1
num = 10

while num > 0:
    print(a)
    a, b = b, a+b
    num -= 1
