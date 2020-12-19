'''
Number Types Module By Aryansh Gupta.
(c) CPL Software Labs 2020

Use this module to quickly find whether a number belongs to a
Special Category of numbers or not

Range Based Functions return specific type of numbers in a range.
'''






def even(number):
    '''return True if number is even else false'''
    if number % 2 == 0:
        return (True)
    else:
        return (False)


def odd(number):
    '''return True if number is Odd else false'''
    if number % 2 == 1:
        return (True)
    else:
        return (False)


def composite(x):
    '''return True if number is a Composite number else false'''
    if prime(x) == False:
        return (True)
    else:
        return (False)


def prime(number):
    '''return True if number is a Prime number else false'''
    c = 0
    for i in range(1, number + 1):
        if number % i == 0:
            c += 1
    if c == 2:
        return (True)
    else:
        return (False)


def twin_prime(number1, number2):
    '''return True if two numbers are Twin Prime else false'''
    if prime(number1) == True and prime(number2) == True and (number2 - number1 == 2 or number1 - number2 == 2):
        return (True)
    else:
        return (False)


def perfect_square(number):
    '''return True if number is a Perfect Square else false'''
    y = number ** 0.5
    if int(y) == y:
        return (True)
    else:
        return (False)


def emirp(number):
    '''return True if number is a Emirp number else false'''
    v = 0
    g = prime(number)
    while number > 0:
        d = number % 10
        v = (v * 10) + d
        number //= 10
    if prime(v) == True and g == True:
        return (True)
    else:
        return (False)


def armstrong(number):
    '''return True if number is a Armstrong number else false'''
    v = 0
    y = number
    while number > 0:
        d = number % 10
        v += (d ** 3)
        number //= 10
    if y == v:
        return (True)
    else:
        return (False)


def factorion(number):
    '''return True if number is a Factorian else false'''
    v = 0
    y = number
    while number > 0:
        f = 1
        d = number % 10
        for i in range(1, d + 1):
            f *= i
        v += f
        number //= 10
    if v == y:
        return (True)
    else:
        return (False)


def palindrome(number):
    '''return True if number is a Palindrome number else false'''
    c = str(number)
    g = c[::-1]
    if g == c:
        return (True)
    else:
        return (False)


def narcissistic(number):
    '''return True if number is a Narcissistic number else false'''
    c = 0
    y = number
    m = len(str(number))
    while number > 0:
        d = number % 10
        c += d ** m
        number //= 10
    if y == c:
        return (True)
    else:
        return (False)


def neon(number):
    '''return True if number is a Neon number else false'''
    f = number ** 2
    g = 0
    while f > 0:
        d = f % 10
        g += d
        f //= 10
    if g == number:
        return (True)
    else:
        return (False)


def spy(number):
    '''return True if number is a Spy number else false'''
    c = 0
    p = 1
    v = number
    while number > 0:
        d = number % 10
        c += d
        number //= 10
    while v > 0:
        j = v % 10
        p *= j
        v //= 10
    if c == p:
        return (True)
    else:
        return (False)


def buzz(number):
    '''return True if number is a Buzz number else false'''
    if number % 7 == 0 or number % 10 == 7:
        return (True)
    else:
        return (False)


def automorphic(number):
    '''return True if number is an Automorphic number else false'''
    d = len(str(number))
    s = str(number ** 2)
    v = s[len(s) - d:]
    if str(number) == v:
        return (True)
    else:
        return (False)


# Range based type counter
def even_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Evens in a given range
    when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if even(i) == True:
            c += 1
            if shownumbers == True:  # True value
                print(i)
    return c


def odd_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Odds in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if odd(i) == True:
            c += 1
            if shownumbers == True:  # True value
                print(i)
    return c


def prime_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Primes in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if prime(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return c


def twin_prime_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Twin Primes in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if i < ending and i + 2 <= ending:
            if twin_prime(i, i + 2) == True:
                c += 1
                if shownumbers == True:
                    print(i, i + 2)
    return c


def palindrome_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Palindromes in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if palindrome(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return c


def factorion_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Factorians in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if factorion(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return c


def composite_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Composites in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if prime(i) != True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c

def armstrong_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Armstrongs in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if armstrong(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c


def narcissistic_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Narcissistic Numbers in a given range
            when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if narcissistic(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return c


def neon_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Neons in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if neon(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c


def spy_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Spy Numbers in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if spy(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c


def emirp_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Emirps in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if emirp(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c


def perfect_square_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Perfect Squares in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if perfect_square(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c


def buzz_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Buzz numbers in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if buzz(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c


def automorphic_in_range(starting, ending=0, shownumbers=False):
    '''returns number of Automorphics in a given range
        when shownumbers set to True, prints all numbers also'''
    c = 0
    for i in range(starting, ending + 1):
        if automorphic(i) == True:
            c += 1
            if shownumbers == True:
                print(i)
    return  c
