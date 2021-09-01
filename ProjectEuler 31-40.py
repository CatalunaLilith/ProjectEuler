# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:04:27 2021

@author: catal
"""

import pdb
import math
import timeit
import fractions
from functools import reduce
from itertools import count, islice

"""
problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

#option 2: write new code


# plan:
    #make Change object to hold change values
    #write make BritishChange
    #write WaystoMakeBritishChange

class BritishCoins(object):
    def __init__(self, p1, p2, p5, p10, p20, p50, p100, p200):
        """assumes each input value is an integer, representing how many of each coin is contained
        Represents a collection of British coins, of value 1p, 2p, 5p, 10p, 20p, 50p, 100p/1£, 200p/2£
        """
        self.p1 = p1
        self.p2 = p2
        self.p5 = p5
        self.p10 = p10
        self.p20 = p20
        self.p50 = p50
        self.p100 = p100
        self.p200 = p200
        
    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2
    
    def getP5(self):
        return self.p5
    
    def getP10(self):
        return self.p10
    
    def getP20(self):
        return self.p20
    
    def getP50(self):
        return self.p50
    
    def getP100(self):
        return self.p100
    
    def getP200(self):
        return self.p200

    def getTotalValue(self):
        """returns an int, representing the totally value in pense of the object"""
        return (self.p1*1)+(self.p2*2)+(self.p5*5)+(self.p10*10)+(self.p20*20)+(self.p50*50)+(self.p100*100)+(self.p200*200)

    def __str__(self):
        """returns a list of how many of each coin is in the object"""
        rep_string = "1P coins:" + str(self.p1) + ", 2P coins:" + str(self.p2)+ ", 5P coins:" + str(self.p5)+ ", 10P coins:" + str(self.p10) + ", 20P coins:"+ str(self.p20) + ", 50P coins:" + str(self.p50)+ ", 100P coins:"+ str(self.p100) + ", 200P coins:"+ str(self.p200)
        return rep_string
    def __repr__(self):
        rep_string = "1P coins:" + str(self.p1) + ", 2P coins:" + str(self.p2)+ ", 5P coins:" + str(self.p5)+ ", 10P coins:" + str(self.p10) + ", 20P coins:"+ str(self.p20) + ", 50P coins:" + str(self.p50)+ ", 100P coins:"+ str(self.p100) + ", 200P coins:"+ str(self.p200)
        return rep_string
    
    def valuesEqual(self,other):
        return self.getTotalValue() == other.getTotalValue()
    
    def coinsEqual(self,other):
        con1 = (self.p1 == other.p1)
        con2 = (self.p2 == other.p2)
        con5 = (self.p5 == other.p5)
        con10 = (self.p10 == other.p10)
        con20 = (self.p20 == other.p20)
        con50 = (self.p50 == other.p50)
        con100 = (self.p100 == other.p100)
        con200 = (self.p200 == other.p200)
        return con1 and con2 and con5 and con10 and con20 and con50 and con100 and con200
        
coins1 = BritishCoins(1,2,3,4,5,6,7,8) #value=2760
coins2 = BritishCoins(1,2,3,4,5,6,7,8) #value=2760
coins3 = BritishCoins(1,2,3,4,5,6,7,7) #value=2560
coins4 = BritishCoins(1,2,3,4,5,6,9,7) #value=2760
# print(coins1.getTotalValue())
# print(coins2.getTotalValue())
# print(coins3.getTotalValue())
# print(coins4.getTotalValue())
# print(coins1)
#make equals == tests
# print(coins1==coins1)
# print(coins1==coins2)
# print(coins1==coins3)
# print(coins1==coins4)
# print("---")
# print(coins1.valuesEqual(coins1))
# print(coins1.valuesEqual(coins2))
# print(coins1.valuesEqual(coins3))
# print(coins1.valuesEqual(coins4))

# print(coins1.coinsEqual(coins1))
# print(coins1.coinsEqual(coins2))
# print(coins1.coinsEqual(coins3))
# print(coins1.coinsEqual(coins4))

# print(coins1.getP1())

def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
        
# parts = (get_partitions(set([1,2,3])))
# for part in parts:
#     print(part)

    
def makeBritishChange(change_value):
    """assumes change_value is an int, representing the number of pense to make change for
    returns a set of Change objects, 
    each representing the number of each type of coin to make change for change_value
    """
    
    #initialize 
    change_set = set([])
    max_p1 = change_value // 1
    max_p2 = change_value // 2
    max_p5 = change_value // 5
    max_p10 = change_value // 10
    max_p20 = change_value // 20
    max_p50 = change_value // 50
    max_p100 = change_value // 100
    max_p200 = change_value // 200
    #make list
    for p1 in range(max_p1+1):
        for p2 in range(max_p2+1):
            for p5 in range(max_p5+1):
                for p10 in range(max_p10+1):
                    for p20 in range(max_p20+1):
                        for p50 in range(max_p50+1):
                            for p100 in range(max_p100+1):
                                for p200 in range(max_p200+1):
                                    a_BritishCoins = BritishCoins(p1,p2,p5,p10,p20,p50,p100,p200)
                                    if a_BritishCoins.getTotalValue() == change_value:
                                        change_set.add(a_BritishCoins)
    return change_set

# print(makeBritishChange(5))

def WaystoMakeBritishChange(change_value):
    """assumes change_value is an int, representing the number of pense to make change for
    returns an int, the number of ways to make change for the change_value
    """
    change_set = makeBritishChange(change_value)
    return len(change_set)

# print(WaystoMakeBritishChange(200))  
#note: stop program if over 1280000000 (1280 million)
#note: took 10007 time ticks to execute

"""
Problem 32

We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

hint: Some products can be obtained in more than one way 
so be sure to only include it once in your sum.
"""

def pandigitalProducts9Digits():
    """returns an int, 
    the sum of all the products of 9 digit pandigital product expressions
    such that the digits of the multiplicand, multiplier, and product is 1-9 pandigital
    e.g.  39 × 186 = 7254
    """
    pandigital_list = []
    products_list  = []
    for a in range(9999): 
        for b in range(9999): 
            product = a*b
            expression_string = (str(a)) + (str(b)) + (str(product))
            expression_lenght = len(expression_string)
            if expression_lenght == 9:
                expression_digits_list = [digit for digit in expression_string]
                expression_digits_list.sort()
                if expression_digits_list == ['1','2','3','4','5','6','7','8','9']:
                    new_tuple = (a,b,product)
                    was_found = False 
                    for old_tuple in pandigital_list:
                        if new_tuple[2] == old_tuple[2]:
                            was_found = True
                    if was_found == False:
                        pandigital_list.append(new_tuple)
    for a_tuple in pandigital_list:
        products_list.append(a_tuple[2])
    return sum(products_list)

# print(pandigitalProducts9Digits())

"""
problem 32
The fraction 49/98 is a curious fraction, 
as an inexperienced mathematician in attempting to simplify it 
may incorrectly believe that 49/98 = 4/8, which is correct, 
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""

def findCuriousFractions2Digits():
    """returns a list of tuples (int,int),
    representing the curious fractions of value <1, non-trivial, of 2 digits long. 
    e.g The fraction 49/98 is a curious fraction, 
    as an inexperienced mathematician in attempting to simplify it 
    may incorrectly believe that 49/98 = 4/8, which is correct, 
    is obtained by cancelling the 9s.
    """
    fractions_list = []
    for num in range(10,100):
        for denom in range(10,100):
            for digit in range(1,10):
                if (str(digit) in str(num)) and (str(digit) in str(denom)):
                    test_num = int(str(num).replace(str(digit), "",1))
                    test_denom = int(str(denom).replace(str(digit), "",1))
                    if (test_denom != 0) and (num != denom) and (num < denom):
                        test_fraction = test_num / test_denom
                        fraction = num/denom
                        if test_fraction == fraction:
                            fractions_list.append((num,denom))
    return fractions_list

def sumOfDenominators(fractions_list):
    """given a list tuples (int,int), 
    where each tuple represents a fractions (numerator, denomerator)
    returns an int, the denominator of the product of these four fractions,
    in its lowest common terms
    """
    num_list = []
    denom_list = []
    for a_fraction in fractions_list:
        num_list.append(a_fraction[0])
        denom_list.append(a_fraction[1])
    num_product = 1
    for num in num_list:
        num_product *= num
    denom_product = 1
    for denom in denom_list:
        denom_product *= denom
    result_fraction = fractions.Fraction(num_product,denom_product)
    return result_fraction.denominator

# print(sumOfDenominators(findCuriousFractions2Digits()))

"""
problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
def quickFactorialDigits(digit):
    """asssumes digit is an int 0-9, representing a decimal digit
    returns an int, representing digit!
    """
    if digit == 0:
        return 1
    if digit == 1:
        return 1
    if digit == 2:
        return 2
    if digit == 3:
        return 6
    if digit == 4:
        return 24
    if digit == 5:
        return 120
    if digit == 6:
        return 720
    if digit == 7:
        return 5040
    if digit == 8:
        return 40320
    if digit == 9:
        return 362880

def digitFactorialSum(num):
    """assumes num is an int
    returns an int, the sum of the factorials of the digits of num
    e.g. if num=2680, returns 2+720+40320+1=41043
    """
    fact_sum = 0
    for digit in str(num):
        fact_sum += quickFactorialDigits(int(digit))
    return fact_sum

# print(digitFactorialSum(145))

def curiousFactorials():
    """returns an int, the sum of all of the curious factorials,
    a curious factorial being a number where the sum of the factorials of the digits 
    is equal to the number
    e.g. 145 , as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    """
    curious_factorials_list = []
    #find all curious factorials
    for num in range(3,362880):
        if num == digitFactorialSum(num):
            curious_factorials_list.append(num)
    return sum(curious_factorials_list)

# print(curiousFactorials())

"""
problem 35
The number, 197, is called a circular prime 
because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
def getRotations(num):
    """asssumes that num is an int
    returns a list of ints, representing all the possible rotations of the digits of num
    e.g. getRotations(197) -> [197,971,719]
    """
    rotations_list = []
    rotation = str(num)
    for i in range(len(rotation)):
        rotation = rotation[1:] + rotation[0]
        rotations_list.append(int(rotation))
    return rotations_list
    
# print(getRotations(123))

def isPrime(n):
    """assumes n is an integer
    returns a boolean, 
    true if n is a prime number, 
    false if n is not a prime number
    """
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))
    
def Primes(n):
    """
    assumes n is an int
    returns a list of ints, representing the prime numbers up to n 
    Very straighforward, no optimizations."""
    prime_list = []
    num = 2
    for num in range(n):
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False 
        if is_prime == True:
            prime_list.append(num)
        num += 1
        print(num) 
    prime_list = prime_list[2:]
    return prime_list

def circularPrimes(upper_limit):
    """assumes upper_limit is an int, the max number to look for circular primes 
    returns an int, representing how many circular primes have been found
    e.g. The number, 197, is called a circular prime 
    because all rotations of the digits: 197, 971, and 719, are themselves prime.
    971 and 719 are also circular primes
    """
    circular_primes_list = []
    prime_list = Primes(upper_limit) 
    for prime in prime_list: 
        rotations_list = getRotations(prime)
        all_rotations_prime = True
        for rotation in rotations_list:
            if isPrime(rotation) == False:
                all_rotations_prime = False 
        if all_rotations_prime == True:
            circular_primes_list.append(prime)
    return len(circular_primes_list)

def fasterPrimeFinder(upper_limit):
    prime_list = []
    for num in range(upper_limit):
        if isPrime(num):
            prime_list.append(num)
        print(num)
    return prime_list

def circularPrimesAlt1(upper_limit):
    """assumes upper_limit is an int, the max number to look for circular primes 
    returns an int, representing how many circular primes have been found
    e.g. The number, 197, is called a circular prime 
    because all rotations of the digits: 197, 971, and 719, are themselves prime.
    971 and 719 are also circular primes
    """
    start = timeit.default_timer() #TODO remove
    circular_primes_list = []
    for num in range(upper_limit):
        rotations_list = getRotations(num)
        all_rotations_prime = True
        for rotation in rotations_list:
            if isPrime(rotation) == False:
                all_rotations_prime = False 
        if all_rotations_prime == True:
            circular_primes_list.append(num)
        print(num) #TODO remove
    stop = timeit.default_timer() #TODO remove
    print('Time: ', stop - start) #TODO remove
    return len(circular_primes_list)


def circularPrimesAlt2(upper_limit):
    """assumes upper_limit is an int, the max number to look for circular primes 
    returns an int, representing how many circular primes have been found
    e.g. The number, 197, is called a circular prime 
    because all rotations of the digits: 197, 971, and 719, are themselves prime.
    971 and 719 are also circular primes
    """
    start = timeit.default_timer() #TODO remove
    circular_primes_list = []
    prime_list = fasterPrimeFinder(upper_limit)
    for prime in prime_list: 
        rotations_list = getRotations(prime)
        all_rotations_prime = True
        for rotation in rotations_list:
            if isPrime(rotation) == False:
                all_rotations_prime = False 
        if all_rotations_prime == True:
            circular_primes_list.append(prime)
    stop = timeit.default_timer() #TODO remove
    print('Time: ', stop - start) #TODO remove
    return len(circular_primes_list)

def isPrimeJosh(num):
    for test_num in range(2, int(num**0.5)):
        if num % test_num == 0:
            return False
    return True
        
def circularPrimesAlt3(upper_limit):
    """assumes upper_limit is an int, the max number to look for circular primes 
    returns an int, representing how many circular primes have been found
    e.g. The number, 197, is called a circular prime 
    because all rotations of the digits: 197, 971, and 719, are themselves prime.
    971 and 719 are also circular primes
    """
    start = timeit.default_timer() #TODO remove
    circular_primes_list = []
    for num in range(upper_limit):
        rotations_list = getRotations(num)
        all_rotations_prime = True
        for rotation in rotations_list:
            if isPrimeJosh(rotation) == False:
                all_rotations_prime = False 
        if all_rotations_prime == True:
            circular_primes_list.append(num)
        print(num) #TODO remove
    stop = timeit.default_timer() #TODO remove
    print('Time: ', stop - start) #TODO remove
    return len(circular_primes_list)

# print(circularPrimes(1000000)) 
#note: runtime of circularPrimes(1000000) aproximately 15 hours to find primes, 1 minute to calc circular primes

# print(circularPrimesAlt1(100)) 
#note: runtime of circularPrimes(100) is 0.0009642000077292323
# print(circularPrimesAlt1(1000000))
#note: runtime of circularPrimesAlt1(1000000) is 155.05791779997526

# print(circularPrimesAlt2(100))
#note: runtime of circularPrimes(100) is 0.003320600022561848
# print(circularPrimesAlt2(1000000))
#note: runtime of circularPrimesAlt2(1000000) is 103.43919220002135

# print(circularPrimesAlt3(100))
#note: runtime of circularPrimesAlt3(100) is 0.004420500015839934
# print(circularPrimesAlt3(1000000))
#note: runtime of circularPrimesAlt3(1000000) is 128.98166140000103

"""
problem 36

The decimal number, 585 (decimal) = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isPalindrome(input_string):
    """assumes input_string is a string
    returns a boolean, true if input_string is a palindrome, else false
    """
    original_string  = (input_string[:])
    reversed_string =(input_string[::-1])
    return (original_string == reversed_string)
    
# isPalindrome("cat")
# isPalindrome("tacocat")
# isPalindrome("1221")

def doublePalindromesSum(upper_limit):
    """assumes upper_limit is an int, representing the number up to which to look for double palindromes
    returns an int, the sum of all the double palindromes under upper_limit
    a double palindrome is a palindrome in both base 10 (decimal) and base 2 (binary)
    e.g.585 (decimal) = 1001001001 (binary), is palindromic in both bases.
    """
    double_palindrome_list = []
    for num in range(upper_limit):
        decimal_string = str(num)
        binary_string = format(num, "b")
        if isPalindrome(decimal_string) and isPalindrome(binary_string):
            double_palindrome_list.append(num)
    return sum(double_palindrome_list)

# print(doublePalindromesSum(1000000))

"""
problem 37

The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. (b/c single digit)
"""


#find truncatable primes until find 11

#initialize truncatable_primes_list = []
#num = 11
#while len(truncatable_primes_list)< 12
    #if isPrime
        #trucate from right
        #truncate from left 
        #if left and right isPrime
            #if truncate is <10
                #append to truncatable_primes_list
            #repeat
            
        #else
            #break
    #num += 1
#return sum(truncatable_primes_list)

def leftTruncate(num):
    return int(str(num)[1:])

def rightTruncate(num):
    return int(str(num)[:-1])
        
def doubleTruncatablePrimes(): 
    """returns an int, the sum of all 11 truncatable primes
    a truncatable prime is a number that,
    Being prime itself, it is possible to continuously remove digits from left to right, 
    and remain prime at each stage: 3797, 797, 97, and 7. 
    Similarly we can work from right to left: 3797, 379, 37, and 3.
    note: single digit primes (2,3,5,7) are not considered truncatable 
    """
    # pdb.set_trace()
    truncatable_primes_list = []
    num = 11
    while len(truncatable_primes_list) < 11:
        right_truncate = num
        left_truncate = num
        while isPrime(right_truncate) and isPrime(left_truncate) and (right_truncate  >=10) and (left_truncate  >=10):
            right_truncate = rightTruncate(right_truncate)
            left_truncate = leftTruncate(left_truncate)
            if (right_truncate  <10) and (left_truncate <10) and isPrime(right_truncate) and isPrime(left_truncate):
                truncatable_primes_list.append(num)
        num += 1 
    return sum(truncatable_primes_list)

# print(doubleTruncatablePrimes())
#started at 5:28 pm, ended at 5:31

"""
problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number 
that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def isPandigital(num):
    """assumes num is an int or string, the number being queried for pandegital-ness
    returns a boolean, True if num is pandigital, else False
    a 9 digit pandigital number contains the digits 123456789 is any order
    """
    expression_string = str(num)
    expression_lenght = len(expression_string)
    if expression_lenght == 9:
        expression_digits_list = [digit for digit in expression_string]
        expression_digits_list.sort()
        return expression_digits_list == ['1','2','3','4','5','6','7','8','9']
    return False 

# print(isPandigital(12345789))
# print(isPandigital(123456789))
# print(isPandigital(123556789))

def largestConcatenatedPandigital():
    """returns an int, the largest 9 digit pandigital 
    that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1
    """
    largest_pandigital = None
    for num in range (9999):  #b/c concatenation must be 9 digit 
        products_list = []
        concatenated_products = ""
        for digit in range(1,10):
            products_list.append(num*digit)
        for product in products_list:
            concatenated_products += str(product)
            if isPandigital(concatenated_products):
                new_pandigital = int(concatenated_products)
                if (largest_pandigital == None) or (new_pandigital > largest_pandigital):
                    largest_pandigital = new_pandigital
    return largest_pandigital

# largestConcatenatedPandigital()
# print(isPandigital(932718654))

"""
problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
def intRightAngleSolutions(p):
    """assumes p is an integer, representing the perimeter of a right triangle
    returns a list of tuples lenght three of ints, 
    each tuple representing (a,b,c), the lenghts of the legs a and b and hypothenus c of a right triangle of perimeter p
    the list of tuples representing all the possible integer solutions for a right triangle of perimeter p 
    
    """
    perimeter_list = []
    for a in range(1,p-1):
        for b in range(1,p-1):
            if a+b < p:
                c = ((a**2)+(b**2))**0.5
                if (a+b+c == p):
                    if ((a,b,int(c)) in perimeter_list) or ((b,a,int(c)) in perimeter_list):
                        pass
                    else:
                        perimeter_list.append((a,b,int(c)))
    return perimeter_list

# print(intRightAngleSolutions(120))

def bestIntRightTriangle(max_p):
    """assumes max_p is an int, representing the maximum perimeter to search for
    returns an int, representing the perimeter p with the most integer solutions 
    for a right triangle
    """
    p_with_max_solutions = None
    lenght_p_with_max_solutions = None
    for p in range(1,max_p+1):
        print(p)
        lenght_p = len(intRightAngleSolutions(p))
        if (p_with_max_solutions == None) or (lenght_p > lenght_p_with_max_solutions):
            lenght_p_with_max_solutions = lenght_p
            p_with_max_solutions = p 
    return p_with_max_solutions

# print(bestIntRightTriangle(1000))

"""
problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def buildIrrationalDecimalFraction(lenght):
    """assumes lenght is an int, how long of a IDF to build
    builds an IDF from concatenating the positive integers such that 
     buildIrrationalDecimalFraction(33) = 0.123456789101112131415161718192021
    returns a string, representing the IDF
    """
    IDF = "0."
    num = 1
    while len(IDF) < lenght+2: 
        IDF += str(num)
        num +=1
    return IDF
    

# (buildIrrationalDecimalFraction(1000000))

def IDFProduct():
    """returns a float, the product d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    such that d1 = IDF[0], d10 =IDF[9], etc
    """
    IDF = buildIrrationalDecimalFraction(1000000) 
    IDF1 = float(IDF[2])
    IDF10 = float(IDF[11])
    IDF100 = float(IDF[101])
    IDF1000 = float(IDF[1001])
    IDF10000 = float(IDF[10001])
    IDF100000 = float(IDF[100001])
    IDF1000000 = float(IDF[1000001])
    return IDF1*IDF10*IDF100*IDF1000*IDF10000*IDF100000*IDF1000000

# print(IDFProduct())











