# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:56:48 2021

@author: catal
"""

import pdb
import math
import timeit
from functools import reduce
from itertools import count, islice
import itertools
import string

"""
problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
def isPrime(n):
    """assumes n is an integer
    returns a boolean, 
    true if n is a prime number, 
    false if n is not a prime number
    """
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))

def isPandigital9digit(num):
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

def isPandigitalXdigit(num):
    """assumes num is an int or string, the number being queried for pandegital-ness
    returns a boolean, True if num is pandigital, else False
    an x digit pandigital number contains the digits 1-x in any order
    in base 10, can be pandigital from 1 to 9 digits
    """
    #convert num to list of strings of digits
    expression_string = str(num)
    expression_digits_list = [digit for digit in expression_string]
    expression_digits_list.sort()
    expression_lenght = len(expression_string)
    #build pandigital_digits_list for given expression_lenght 
    pandigital_digits_list = []
    for digit in range(1,expression_lenght+1):
        pandigital_digits_list.append(str(digit))
    return expression_digits_list == pandigital_digits_list

# print(isPandigitalXdigit(0))
# print(isPandigitalXdigit(21))
# print(isPandigitalXdigit(123))
# print(isPandigitalXdigit(1423))
# print(isPandigitalXdigit(14253))
# print(isPandigitalXdigit(156423))
# print(isPandigitalXdigit(6571423))
# print(isPandigitalXdigit(87651423))
# print(isPandigitalXdigit(198765423))
# print(isPandigitalXdigit(14423))

def largestPandigitalPrime():
    """returns an int, the largest number that is both pandigital in base 10 and a prime"""
    for num in range(100000000,1,-1):
        print(num)
        if isPandigitalXdigit(num) and isPrime(num):
            return num

# print(largestPandigitalPrime()) #largest_pandigital_prime = 7652413

"""
problem 41

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to 
its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
"""
def buildLetterValuesDict():
    """ returns a dictionary, whose keys are A-Z, whose values are 1-26"""
    letter_values_dict = {}
    num = 1
    for letter in string.ascii_uppercase :
        letter_values_dict.update({letter:num})
        num +=1
    return letter_values_dict

def calcWordValue(a_string):
    """assumes a_string_list is a string with only letters a-z (not case sensitive)
    returns an int, the word score, the value of the letters of the word
    where a word_score is the value of the letters of the word 
    where the letter values are  a=1, b=2, ... z=26
    
    example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53, 
    """
    a_string = a_string.upper()
    # get dict of letters and values 
    letter_values = buildLetterValuesDict()
    #calc word score 
    word_value = 0
    for letter in a_string:
        word_value += letter_values[letter]
    return word_value

# print(calcWordValue("AbC"))

def makeList(file_name):
    """assumes file_name.txt is a txt file,
    which is a continuous series of alphabetic charaqcters sequences (words) 
    seperated by spaces
    returns a list, where each element is a string of aphabetic characters in quotes"""
    file = open(file_name)
    file_holder = file.readlines()
    file.close()
    file_list = file_holder[0].split(",")
    file_list = [i[1:-1] for i in file_list]
    return file_list

# print(makeList("p042_words.txt"))

def triangleNumbersGenerator(size):
    """asssumes that size is an int, representing how many triangle numbers to find
    returns a list of ints, the first size triangle numbers
    where a triangular number has the form Tn=n(n+1)/2	
    """
    triangle_numbers_list = []
    for n in range(1,size+1):
        triangle_num = 0.5*n*(n+1)
        triangle_numbers_list.append(int(triangle_num))
    return triangle_numbers_list

# print(triangleNumbersGenerator(10))

def triangeWords():
    """
    returns an int, the number of triangle words in the list
    a triangle word being a word whose word value is a triangle number 
    """
    triangle_words_found = 0
    triangle_numbers_list = triangleNumbersGenerator(300)
    words_list = makeList("p042_words.txt")
    for word in words_list:
        word_score = calcWordValue(word)
        if word_score in triangle_numbers_list:
            triangle_words_found += 1 
    return triangle_words_found
    
# print(triangeWords())

"""
problem 43 

The number, 1406357289, is a 0 to 9 pandigital number 
because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# goal: take sum of all numbers that are 9pandigital and interestingdivisible 

def isInterestingDivisible(num):
    """assumes num is an int
    returns a boolean, true if num is interesting, else false
    
    """
    #take the digits of number
    d2 = str(num)[1]
    d3 = str(num)[2]
    d4 = str(num)[3]
    d5 = str(num)[4]
    d6 = str(num)[5]
    d7 = str(num)[6]
    d8 = str(num)[7]
    d9 = str(num)[8]
    d10 = str(num)[9]
    #test each prescribed things
    d2d3d4 = int(d2 + d3 + d4)
    d3d4d5 = int(d3+d4+d5)
    d4d5d6 = int(d4+d5+d6)
    d5d6d7 = int(d5+d6+d7)
    d6d7d8 = int(d6+d7+d8)
    d7d8d9 = int(d7+d8+d9)
    d8d9d10 =  int(d8+d9+d10)
    if d2d3d4 % 2 != 0:
        return False
    if d3d4d5 % 3 != 0:
        return False
    if d4d5d6 % 5 != 0:
        return False
    if d5d6d7 % 7 != 0:
        return False
    if d6d7d8 % 11 != 0:
        return False
    if d7d8d9 % 13 != 0:
        return False
    if d8d9d10 % 17 != 0:
        return False
    return True

def isPandigital10digit(num):
    """assumes num is an int or string, the number being queried for pandegital-ness
    returns a boolean, True if num is pandigital, else False
    a 10 digit pandigital number contains the digits 0123456789 is any order
    """
    expression_string = str(num)
    expression_lenght = len(expression_string)
    if expression_lenght == 10:
        expression_digits_list = [digit for digit in expression_string]
        expression_digits_list.sort()
        return expression_digits_list == ['0','1','2','3','4','5','6','7','8','9']
    return False 
    
# print(isInterestingDivisible(1406357209))
# isInterestingDivisible(1406357299)
    
def badPandigitalDivisibilitySum():
    """returns an int, the sum of all the numbers that are both
    1. 10 digit pandigital
    2. interesting divisible
    note: HORrIBLE running time for 1 trillion numbers, 
    estimated 7 days on ryzen 7 AMD processor
    use permutations version instead
    """
    weird_list = []
    for num in range (1023456789,9876543211):
        if isPandigital10digit(num) and isInterestingDivisible(num):
            weird_list.append(num)
    return sum(weird_list)

# print(pandigitalDivisibilitySum())

# find better way to get pandigitals. digit suffling?

def get_permutations(sequence):
    '''
    Assumes sequence is an arbitrary string and non-empty
    Returns: a list of strings, all the permutations of sequence
    Example: get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    note: do not depend on order of the output list
    '''
    permutations_of_sequence = []
    permutations_of_cutdown_sequence = []
    # define recursive behaviour
    # for sequence of len(n), case is sequence[0] and sequence[1:n]
    if len(sequence) > 1:
        first_char_sequence = sequence[0]
        cutdown_sequence = sequence[1:]
        # find recursions of cutdown_sequence
        if len(cutdown_sequence) > 1:
            permutations_of_cutdown_sequence = get_permutations(sequence[1:])
        # base case
        # add first_char_sequence to all recursions of cutdown_sequence
        for i in range(len(sequence)):
            holding_string = cutdown_sequence[:i] + first_char_sequence + cutdown_sequence[i:]
            permutations_of_sequence += [holding_string]
        # loop over each item in permutations_of_cutdown_sequence
        if len(permutations_of_cutdown_sequence) > 1:
            for ele in range(len(permutations_of_cutdown_sequence)):
                new_cutdown_sequence = permutations_of_cutdown_sequence[ele]
                for i in range(len(sequence)):
                    holding_string = new_cutdown_sequence[:i] + first_char_sequence + new_cutdown_sequence[i:]
                    permutations_of_sequence += [holding_string]
    # remove duplicates from permutations_of_sequence
    return list(dict.fromkeys(permutations_of_sequence))

# print(get_permutations("cat"))

def pandigitalDivisibilitySum():
    """returns an int, the sum of all the numbers that are both
    1. pandigital for digits 0123456789
    2. interesting divisible
    """
    #get permutations
    permutations_list = get_permutations("0123456789")
    weird_list = []
    for num in permutations_list:
        if (num[0]!="0") and isInterestingDivisible(int(num)):
            weird_list.append(int(num))

    return sum(weird_list)

# print(pandigitalDivisibilitySum()) #running time 304.14516859990545

"""
problem 44

Pentagonal numbers are generated by the formula,
 Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. 
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, 
for which their sum and difference are pentagonal 
and D = |Pk − Pj| is minimised; 
what is the value of D?
"""
def pentagonalNumberGenerator(upper_limit):
    """asssumes upper_limit is an int, how many Pentagonal numbers to find
    returns a list of ints, an upper_limit amount of pentagonal numbers
    where a pentagonal number has the form  Pn=n(3n−1)/2
    """
    pentagonal_list = []
    for n in range(1,upper_limit+1):
        pentagonal_num = int(n*(3*n-1)/2)
        pentagonal_list.append(pentagonal_num)
    return pentagonal_list

# print(calcPentagonalNums(10))

def calcPentagonalD():
    """returns an int, D, such that  D = |Pk − Pj| is minimised
    for a pair of pentagonal numbers Pj and Pk where
    Pj + Pk is Pentagonal and Pj - Pk is pentagonal
    """
    pentagonal_list = pentagonalNumberGenerator(10000)
    smallest_D = None
    i = 0
    for Pa in pentagonal_list:
        i += 1
        print(i)
        for Pb in pentagonal_list:
            if ((Pa+Pb) in pentagonal_list) and ((Pa-Pb) in pentagonal_list):
                Da= abs(Pa-Pb)
                Db= abs(Pb-Pa)
                if (smallest_D == None) or (Da < smallest_D):
                    smallest_D = Da
                if (smallest_D == None) or (Db < smallest_D):
                    smallest_D = Db
    return smallest_D

# print(calcPentagonalD())

"""
problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
# def triangleNumbersGenerator(size):
#     """asssumes that size is an int, representing how many triangle numbers to find
#     returns a list of ints, the first size triangle numbers
#     """

# def pentagonalNumberGenerator(upper_limit):
#     """asssumes upper_limit is an int, how many Pentagonal numbers to find
#     returns a list of ints, an upper_limit amount of pentagonal numbers
#     where a pentagonal number has the form  Pn=n(3n−1)/2
#     """
    
def hexagonalNumberGenerator(size):
    """asssumes that size is an int, representing how many triangle numbers to find
    returns a list of ints, the first size hexagonal numbers
    where a hexagonal number has the form Hn=n(2n−1)
    """
    hexagonal_numbers_list = []
    for n in range(1,size+1):
        hexagonal_num = n*((2*n)-1)
        hexagonal_numbers_list.append(int(hexagonal_num))
    return hexagonal_numbers_list

# print(hexagonalNumberGenerator(10))

def TriangularPentagonalHexagonal2nd():
    """returns an int, the 2nd number (other than 40755) that is triangular, pentagonal, and hehagonal
    where a triangular number has the form Tn=n(n+1)/2
    where a pentagonal number has the form  Pn=n(3n−1)/2
    where a hexagonal number has the form Hn=n(2n−1)
    """
    # pdb.set_trace()
    # #make 3 lists
    triangular_nums = triangleNumbersGenerator(1000000)
    pentagonal_nums = pentagonalNumberGenerator(1000000)
    hexagonal_nums = hexagonalNumberGenerator(1000000)
    found_40755 = False
    for num in triangular_nums[1:]:
        if (num in pentagonal_nums) and (num in hexagonal_nums):
            if found_40755 == False:
                print("found 40755")
                print(num)
                found_40755 = True
            else:
                print("found next")
                return num
# print(TriangularPentagonalHexagonal2nd())

"""
problem 46

It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
# goal: int, odd, composite
# is not = Prime + 2(n**2)

def sumOfPrimeAndTwiceSquare(num):
    """assumes num is an int
    returns a boolean, True is num can be written as the sum of a price and twice a square,
    else false 
    e.g. 9 = 7 + 2(1**2) --> True
    """
    prime_list = []
    for num_a in range (2,num):
        if isPrime(num_a):
            prime_list.append(num_a)
    twice_squares_list = []
    for num_b in range (1,int(num**0.5)):
        twice_squares_list.append(2*(num_b**2))
    for a_prime in prime_list:
        for a_twice_square in twice_squares_list:
            if num == a_prime + a_twice_square:
                return True 
    return False 

# for num in range(34):
#     print(sumOfPrimeAndTwiceSquare(num))
# print(sumOfPrimeAndTwiceSquare(33))

def antiGoldbach():
    """returns the first anti-Goldbach number, 
    smallest odd composite that cannot be written as the sum of a prime and twice a square
    """
    
    for num in range (33,6000,2):
        if (isPrime(num) == False) and (sumOfPrimeAndTwiceSquare(num) == False):
            return num

# print(antiGoldbach())

"""
Problem 47

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2**2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
"""


def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# print(primeFactors(3766))

def distinctPrimeFactors(num):
    """asssumes num is an int
    returns a list of ints, the distinct prime factors of num"""
    return list(set(primeFactors(num)))

# print(distinctPrimeFactors(25))

def doListsIntersect(list_a, list_b):
    """asssumes list_a and list_b are lists of objects that have equality defined
    returns a boolean, True if any elements are shared between list_a and list_b, else false
    """
    return ((len(list_a)+len(list_b)) != len(set(list_a + list_b)))

# print(doListsIntersect([1,2,3], [1,4,5]))
# print(doListsIntersect([1,2,3], [9,4,5]))
    
def fourConsecutiveFourDistinctPrimeFactors():
    """returns an int, the first number of the sequence 
    of the first four consecutive integers to have four distinct prime factors each
    """
    # iterate over numbers until find first set
    num = 1
    while True:
        if len(distinctPrimeFactors(num)) == 4: 
            if len(distinctPrimeFactors(num+1)) == 4: 
                if len(distinctPrimeFactors(num+2)) == 4: 
                    if len(distinctPrimeFactors(num+3)) == 4: 
                        print("___")
                        return num
                    else: 
                        num += 1
                else: 
                    num += 1
            else: 
                num += 1
        else: 
            num += 1

# print(fourConsecutiveFourDistinctPrimeFactors())

"""
problem 48 

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
""" 

def selfPowers(num):
    """assumes num is an int
    returns an int, the sum of the series 1**1 + 2**2 +  ... + num**num
    """
    # pdb.set_trace()
    self_powers_sum = 0 
    for n in range(1,num+1):
        self_powers_sum += n**n
    print("---")
    return self_powers_sum

# print(str(selfPowers(1000))[-10:])

"""
problem 49 

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, 
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def sortConcatenateList(a_list):
    """assumes that a_list is a list of objects
    returns a string, the concatenation of the string representation of the sorted a_list"""
    concat_string = ""
    a_list.sort()
    for elem in a_list:
        concat_string += str(elem)
    return concat_string

# print(sortConcatenateList([4817,1487,8147]))

def numsHaveSameDiffrence(num_list):
    """asssumes num_list is a list of numbers
    returns a boolean, True if all the numbers in the list have the same diffrence as all the other numbers in the list,
    else False"""
    
    first_diffrence = abs(num_list[0] - num_list[1])
    for num in num_list[1:]:
        a_diffrence= abs(num_list[0] - num)
        if first_diffrence != a_diffrence:
            return False 
    return True 

# print(numsHaveSameDiffrence([4817,1487,8147]))
# print(numsHaveSameDiffrence([4817,1487,8157]))

def primePermutations():
    """returns a list of lists of ints, 
    each list of list representing an arithmetic sequence where the elements are 4 digit ints which
    are prime and permutations of eachother
    """
    #test each combo for prime permutation properties 
    for num in range(1000,10000): 
        if isPrime(int(num)):
            permutations_list = get_permutations(str(num))
            sequence_list = []
            for permutation in permutations_list:
                if isPrime(int(permutation)):
                    sequence_list.append(permutation)
            if len(sequence_list) >= 3:
                sequence_combos = (itertools.combinations(sequence_list, 3))
                for truple in sequence_combos:
                    if numsHaveSameDiffrence([int(i) for i in truple]):
                        concat_truple = sortConcatenateList(list(truple))
                        return concat_truple

# print(primePermutations())

"""
problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def primeGenerator(max_prime):
    """assumes max_prime is an int, the value up to which to look for primes
    returns a list of ints, all the primes less than max_prime"""
    primes_list = []
    for num in range (2,max_prime):
        if isPrime(num):
            primes_list.append(num)
    return primes_list

# primes_under_million = primeGenerator(1000000)
# print(primes_under_million)

def primeSumOfConsecutivePrimes():
    """returns an int, the prime below 1 million,
    that can be written as the sum of the most consecutive primes"""
    #generate prime list
    primes_list = []
    for num in range (2,1000000): #TODO 1000000
        if isPrime(num):
            primes_list.append(num)
    #initialize 
    max_lenght = 0
    max_sum = 0 
    sum_list = []
    i=0
    j=0
    #test elems of slice primes_list 
    #with outer loop over begining of slice, inner loop indexing over slice
    # pdb.set_trace()
    while i < len(primes_list[j:]):
        if (isPrime(sum(sum_list))) and (len(sum_list) > max_lenght) and (sum(sum_list) < 1000000):
            max_lenght = len(sum_list)
            max_sum = sum(sum_list)
        if sum(sum_list) < 1000000: #TODO 1000000
            sum_list.append((primes_list[j:])[i])
            i+=1
        else:
            #reset inner loop
            sum_list = []
            i=0
            #increment outer loop
            j+=1
            print(max_sum)
    print(max_lenght, max_sum)
    return max_sum 
        

print(primeSumOfConsecutivePrimes())





















































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    