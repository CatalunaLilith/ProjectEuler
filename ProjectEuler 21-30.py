# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:34:39 2021

@author: catal
"""

import pdb
import math
from functools import reduce
from itertools import count, islice
import string
import time


"""problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, 
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, 
the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. 

The proper divisors of 284 are 1, 2, 4, 71 and 142; 
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def properDivisors(n):
    """asssumes num is an int
    returns a list, composed of ints which are the proper divisors of num
    a proper divisor of n is a numbers less than n which divide evenly into n
    A positive divisor of n which is different from n is called a proper divisor 
    An integer n>1 whose only proper divisor is 1 is called a prime number. 
    """
    factors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    factors.remove(n)
    return factors

# print(properDivisors(284))
    
def dOfN(n):
    """assumes n is an int
    returns an int d(n),
    Let d(n) be defined as the sum of proper divisors of n
    the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. 
    The proper divisors of 284 are 1, 2, 4, 71 and 142; 
    so d(284) = 220.
    
    """
    proper_divisors_list = properDivisors(n)
    return sum(proper_divisors_list)
    
# print(dOfN(220))
    
def findAmicableNumbers(max_num):
    """assumes max_num is an int, the number up to which we seak amiucable numbers
    returns a list of tuples of two ints, where each tuple is a set of amicable numbers
    If d(a) = b and d(b) = a, where a ≠ b, 
    then a and b are an amicable pair and each of a and b are called amicable numbers.
    """
    #build tuples_list of tuples (n,d(n)) 2 to n = max_num
    tuples_list = []
    amicable_list = []
    for n in range(2,max_num+1):
        tuples_list.append((n,dOfN(n)))
    #if 0th elem of item 1 matches 1st elem of item 2, these are amicable numbers
    for elem1 in tuples_list:
        for elem2 in tuples_list:
            if (elem1[0]==elem2[1]) and (elem2[0]==elem1[1]):
                amicable_list.append((elem1[0], elem2[0]))
    #remove a==b from amicable_list
    amicable_list_copy = amicable_list.copy()
    for thing in amicable_list_copy:
        if thing[0] == thing[1]:
            amicable_list.remove(thing)
    #remove one of duplicate (a,b) or (b,a) from list 
    amicable_uniq=set()
    for i in amicable_list: # O(n), n=|l|
        if not (i in amicable_uniq or (i[1], i[0]) in amicable_uniq): # O(1)-Hashtable
            amicable_uniq.add(i)
    amicable_uniq = list(amicable_uniq)
    return amicable_uniq

# print(findAmicableNumbers(10000))

def sumOfAmicableNumbers(amicable_list):
    """assumes amicable_list is a list of tuples of ints
    returns an int, the sum of all the numbers in all the tuples in amicable_list"""
    amicable_sum = 0 
    for tup in amicable_list:
        for value in tup:
            amicable_sum += value
    return amicable_sum

# print(sumOfAmicableNumbers(findAmicableNumbers(10000)))

"""
not actually a Project Euler problem

find sum of (square of number)for intergers 1 to 100
"""
def sumOfSquares(num):
    """
    assumes num is an integer >=2
    returns the sum of (the square of a int), for integers 1 to num
    """
    squares_sum = 0
    for number in range(1,num+1):
        number_squared = number**2
        squares_sum += number_squared
    return squares_sum

# test_sum = sumOfSquares(5)
# assert test_sum == 55
# sumOfSquares(100)

"""
problem 22
Using p022_names, 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 

Then working out the alphabetical value for each name,
 multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
#import file
def makeList(file_name):
    """assumes file_name.txt is a txt file,
    which is a continuous series of alphabetic charaqcters sequences (words) 
    seperated by spaces
    returns a list, where each element is a string of aphabetic characters"""
    file = open(file_name)
    file_holder = file.readlines()
    file.close()
    file_list = file_holder[0].split(",")
    file_list = [i[1:-1] for i in file_list]
    return file_list

# makeList("p022_names.txt")

def buildLetterValuesDict():
    """ returns a dictionary, whose keys are A-Z, whose values are 1-26"""
    letter_values_dict = {}
    num = 1
    for letter in string.ascii_uppercase :
        letter_values_dict.update({letter:num})
        num +=1
    return letter_values_dict

# buildLetterValuesDict()

def calcAllNameScores(string_list):
    """assumes string_list a list, where each element is a string of aphabetic characters
    returns an int, the total of all the name_score,
    where a single name_score is the word_score * (word index +1)
    where a word_score is the value of the letters of the word 
    where the letter values are  a=1, b=2, ... z=26
    
    example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53, 
            COLIN is the 938th name in the list
            COLIN would obtain a score of 938 × 53 = 49714.
    """
    string_list.sort()
    # get dict of letters and values 
    letter_values = buildLetterValuesDict()
    total_word_values = 0
    for i in range((len(string_list))): 
        word = string_list[i]
        word_letter_value = 0
        for letter in word:
            word_letter_value += letter_values[letter]
        word_value = word_letter_value * (i+1)
        total_word_values += word_value
    return total_word_values

# print(calcAllNameScores(makeList("p022_names.txt")))

"""
problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n.
A number n is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that 
all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def isAbundent(num):
    """assumes num is an int >= 1
    returns boolean, is num abundent
    where an abundent number is greater than the sum of its proper divisors"""
    proper_divisors = properDivisors(num)
    proper_divisors_sum = sum(proper_divisors)
    if proper_divisors_sum > num:
        return True
    return False

# print(isAbundent(12))
# print(isAbundent(13))
# print(isAbundent(89))

def isDeficient(num):
    """assumes num is an int >= 1
    returns boolean, is num deficient
    where a deficient number is less than the sum of its proper divisors"""
    proper_divisors = properDivisors(num)
    proper_divisors_sum = sum(proper_divisors)
    if proper_divisors_sum < num:
        return True
    return False

def writtenAsSumOfTwoAbundent(num):
    """assumes num is an int >= 1 
    returns boolean, can num be writen as sum of two abundent numbers
    where an abundent number is greater than the sum of its proper divisors"""
    if num < 24:
        return False
    if num >28123:
        return True
    #make list of abundent numbers < num 
    abundent_list = []
    for elem in range(1,num):
        if isAbundent(elem) == True:
            abundent_list.append(elem)
    #double iterate over abundent_list
    for elem1 in abundent_list:
        for elem2 in abundent_list:
            if ((num - elem1 -elem2) == 0):
                return True
    return False

# print(writtenAsSumOfTwoAbundent(22))
# print(writtenAsSumOfTwoAbundent(24))
# print(writtenAsSumOfTwoAbundent(25))
# print(writtenAsSumOfTwoAbundent(32))

def sumOfNonAbundentNumbers():
    """returns an int, the sum of all numbers which can not be written as the sum of two abundent numbers
    where an abundent number is greater than the sum of its proper divisors
    assumes that all integers greater than 28123 can be written as the sum of two abundant numbers"""
    start = time.time()
    the_sum = 0 
    for num in range(28123):
        if writtenAsSumOfTwoAbundent(num) == False:
            the_sum += num
    end = time.time()
    print("time to run sumOfNonAbundentNumbers() is")
    print(end - start)
    return the_sum

# print(sumOfNonAbundentNumbers())
# note: runtime for sumOfNonAbundentNumbers() is 5571.568809509277


def makeListofAbundentNumbers(max):
    """assumes max is an int >=12
    returns a list of ints, containing the abundent numbers <= max"""
    abundent_list = []
    for elem in range(1,max):
        if isAbundent(elem) == True:
            abundent_list.append(elem)
    return abundent_list

def writtenAsSumOfTwoAbundent2(num):
    """assumes num is an int >= 1 
    returns boolean, can num be writen as sum of two abundent numbers
    where an abundent number is greater than the sum of its proper divisors"""
    if num < 24:
        return False
    if num >28123:
        return True
    #find way to limit iteration to elements < num 
    #double iterate over abundent_list
    abundent_list = []
    for elem1 in abundent_list:
        if elem1 < num:
            for elem2 in abundent_list:
                if elem2 < num:
                    if ((num - elem1 -elem2) == 0):
                        return True
    return False

def sumOfNonAbundentNumbers2():
    """returns an int, the sum of all numbers which can not be written as the sum of two abundent numbers
    where an abundent number is greater than the sum of its proper divisors
    assumes that all integers greater than 28123 can be written as the sum of two abundant numbers"""
    start = time.time()
    the_sum = 0 
    for num in range(28123): 
        if writtenAsSumOfTwoAbundent2(num) == False:
            the_sum += num
    end = time.time()
    print("time to run sumOfNonAbundentNumbers2() is")
    print(end - start)
    return the_sum


# abundent_list = makeListofAbundentNumbers(28123)
# print(sumOfNonAbundentNumbers2())
# print(writtenAsSumOfTwoAbundent2(20))
# note: runtime for sumOfNonAbundentNumbers() is 5571.568809509277
# note: runtime for sumOfNonAbundentNumbers2() is 2499.732594013214


"""
problem 24

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. 

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?
"""
def getPermutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  
    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''
    permutations_of_sequence = []
    permutations_of_cutdown_sequence = []
    
    #define recursive behaviour
    #for sequence of len(n), case is sequence[0] and sequence[1:n] 
        
    if len(sequence) > 1: 
        first_char_sequence = sequence[0]
        cutdown_sequence = sequence[1:]
        
        #find recursions of cutdown_sequence
        if len(cutdown_sequence) > 1: 
            permutations_of_cutdown_sequence = getPermutations(sequence[1:])
            
        #base case
        #add first_char_sequence to all recursions of cutdown_sequence 
        for i in range(len(sequence)):
             holding_string = cutdown_sequence[:i] + first_char_sequence + cutdown_sequence[i:]
             permutations_of_sequence += [holding_string]
             
        #loop over each item in permutations_of_cutdown_sequence    
        if len(permutations_of_cutdown_sequence) >1:      
            for ele in range(len(permutations_of_cutdown_sequence)):
                new_cutdown_sequence = permutations_of_cutdown_sequence[ele]
                for i in range(len(sequence)):
                    holding_string = new_cutdown_sequence[:i] + first_char_sequence + new_cutdown_sequence[i:]
                    permutations_of_sequence += [holding_string]
                    
    #remove duplicates from permutations_of_sequence   
    return list(dict.fromkeys(permutations_of_sequence)) 

def sortLexicalPermutations(permutations_list):
    """Assumes permutations_list is a list of strings of numericals, representing all the permutations of a string
    returns a list of strings, representing the lexical permitations from permutations_list, in order from smallest to largest
    """
    #sort lexical permutations
    sorted_lexical_permutations = permutations_list
    sorted_lexical_permutations.sort()
    return sorted_lexical_permutations
    

# permutations = (sortLexicalPermutations(getPermutations("0123456789")))
# print(permutations[999999])
# a_list = ['123', '213', '231', '132', '312', '321']
# a_list.sort()
# print(a_list)

"""
problem 25 

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
#recursively find fibonacci terms
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
# print(fib(3))

def fib_efficient(n, d):
    """asssumes n is an int, the nth fibonacy
    assumes d is a dictionary of key int, value int, 
    representing the 0th to nth fibonacci number and its value
    returns int, the value of the nth fibonacci number
    """
    # pdb.set_trace()
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
    
# print(fib_efficient(12,{1:1, 2:2}))
    
def findIndex3DigitFib():
    n_fib = 1
    fib_value = 1
    fib_list = {1:1, 2:2}
    while (len(str(fib_value)) < 3): 
        fib_value = fib_efficient(n_fib, fib_list)
        if (len(str(fib_value)) == 3):
            return (n_fib + 1)
        n_fib += 1
        
def findIndex4DigitFib():
    n_fib = 1
    fib_value = 1
    fib_list = {1:1, 2:2}
    while (len(str(fib_value)) < 4): 
        fib_value = fib_efficient(n_fib, fib_list)
        if (len(str(fib_value)) == 4):
            print(n_fib)
            print(fib_value)
            return (n_fib + 1)
        n_fib += 1
        
def findIndexXDigitFib(x):
    """assumes x is an int, representing how many digits long of a fibonacci number we want
    returns an int, the index of the first fibonacci number to be x digits long
    """
    n_fib = 1
    fib_value = 1
    fib_list = {1:1, 2:2}
    while (len(str(fib_value)) < x): 
        fib_value = fib_efficient(n_fib, fib_list)
        if (len(str(fib_value)) == x):
            return (n_fib + 1)
        n_fib += 1

# print(findIndexXDigitFib(1000))

"""
problem 26
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains 
the longest recurring cycle in its decimal fraction part.
"""
def simplifyDecimalToInt(num):
    """assumes num is a float
    returns an int, a simplification of the digits without decimal points or zeros
    e.g. 5.000000 -> 5
    e.g. 0.00050 -> 5
    e.g. 0.0420 -> 42
    """
    num_string = str(num)
    reduced_num_str = num_string.replace(".", "")
    reduced_num_str.strip("0")
    return int(reduced_num_str)
    
# print(simplifyDecimalToInt(0.2500007))
    
def RecuringCycleLenght(num):
    """assumes num is an int, the number whose recurring cycle lenght is needed
    a recuring cycle lenght is the minimun digits requires to represent a an irrational fraction
    returns an int, the lenght of the recuring cycle
    e.g. RecuringDecimalLenght(7) -> 1/7 -> 0.(142857) -> returns 6
    """
    dividend = 1
    divisor = num
    #result represents the result of the long division such that 0.125 is [0,1,2,5], and 1.4327 is [1,4,3,2,7]
    result = []
    reminder_dict = {}
    decimal_place = 0 
    found_cycle = False 
    found_end = False
    times_loop = 0
    # pdb.set_trace()
    
    while (found_cycle == False) and (found_end == False):
        times_loop +=1
        div_result = dividend / divisor
        if div_result == 0:
            found_end = True
        elif div_result < 1:
            dividend = dividend*10

        else: #div_result > 1
            digit = int(div_result)
            result.append(digit)
            reminder = dividend - (divisor*digit)
            if reminder in reminder_dict:
                #find out whre cycle starts?
                    #at (index of result) associated with the (value reminder of reminder_list) 
                found_cycle = True
            else:
                reminder_dict[int(reminder)] = len(result)-1
                dividend = reminder
                
    print(reminder_dict)
    print(result)
    print("-------")

    if found_end == True:
        return 0 
    if found_cycle == True:
        pass
        #find out whre cycle starts?
        # pull representation from result
        #return len(repeating sequence)



    
# RecuringCycleLenght(2) #0.5
# RecuringCycleLenght(3) #0.(3)
# RecuringCycleLenght(4) #0.25
# RecuringCycleLenght(6) #0.1(6)
# RecuringCycleLenght(7) #0.(142857)
# RecuringCycleLenght(8) #0.125
# RecuringCycleLenght(9) #0.(1)
# RecuringCycleLenght(11) #0.(09)
# RecuringCycleLenght(12) #0.0(83)

def MaxRecuringCycle(max_num):
    """assumes max_num is an int, the maximum number to look up to
    returns an int, the number whose fraction 1/number's decimal representation 
    has the longest recuring cycle, of the ints 2 to max_num
    """
    max_recuring_cycle_lenght = 0
    max_recuring_cycle_num = 0
    for num in range(2,1000):
        recuring_cycle_lenght = RecuringCycleLenght(num)
        if recuring_cycle_lenght > max_recuring_cycle_lenght:
            max_recuring_cycle_lenght = recuring_cycle_lenght
            max_recuring_cycle_num = num
    return max_recuring_cycle_num


"""
problem 27

Euler discovered the remarkable quadratic formula: n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39
However, when n = 40, 40**2 + 40 + 41 = 40(40+1)+ 41 is divisible by 41, 
and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 + 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values 0 <= n <= 79 . 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n**2 + an + b
, where |a| <1000 and |b| <= 1000
where |n| is the modulus/absolute value of n
e.g.  |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
starting with n=0 
where |a| <1000 and |b| <= 1000
"""

def isPrime(n):
    """assumes n is an integer
    returns a boolean, 
    true if n is a prime number, 
    false if n is not a prime number
    """
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))

def findRemarcableFormula():
    """returns an int, a * b, such that
    y = n**2 + an + b
    where |a| <1000, |b| <= 1000, and n is an integer >= 1
    such that y has the longest sequence of prime numbers
    """
    max_prime_lenght = 0
    max_a = None
    max_b = None
    for a in range (-1000, 1001): 
        for b in range (-1000, 1001): 
            prime_lenght = -1
            y = None
            n = 1 
            while ((y is None) or (isPrime(y))):
                y = (n**2) + (a*n) + b
                prime_lenght += 1
                n += 1 
            if prime_lenght > max_prime_lenght :
                max_prime_lenght = prime_lenght
                max_a = a
                max_b = b 
    return (max_a * max_b) 

# print(findRemarcableFormula())

"""
problem 28 
Starting with the number 1 
and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
# build the 1001x1001 filled with spiral values 
def fillSpiralGrid(grid_size):
    """assumes grid_size is an odd int representing how many rows or columns a square grid has
    returns a list of lists of ints, representing a square grid,
    where the external list has the same lenght as each of the internal lists,
    where the int values are filled in from the center in clockwise spiral
    e.g. grid_size of 5 would return 
    [[21,22,23,23,25],[20,7,8,9,10],[19,6,1,2,11],[18,5,4,3,12],[17,16,15,14,13]]
    which represents the grid 
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    """    
    #initialize empty grid
    grid = []
    row = []
    for size in range(grid_size):
        row.append([])
        size +=1
    for size in range(grid_size):
        grid.append(row.copy()) #change to copy of row
        size +=1
    #fill grid with values
    x = grid_size//2 
    y = grid_size//2 
    value = 1
    step = 1
    grid[x][y] = value
    value +=1
    while step < grid_size:
        for i in range(step):
            y += 1
            grid[x][y] = value
            value +=1
        for i in range(step):
            x += 1
            grid[x][y] = value
            value +=1
        step += 1
        for i in range(step):
            y -= 1
            grid[x][y] = value
            value +=1
        for i in range(step):
            x -= 1
            grid[x][y] = value
            value +=1
        step +=1
    #fill in last row 
    for i in range(step-1):
            y += 1
            grid[x][y] = value
            value +=1
    return grid
    
# fillSpiralGrid(5)
# print(fillSpiralGrid(7))

def calcGridDiagonalSum(a_grid):
    """assumes a_grid represents a square grid, it is a list of lists of ints 
    where the external list has the same lenght as each of the internal lists
    returns an int, the sum of all the ints on both diagonal of the grid"""
    # make list of values on the diagonal
    grid_size = len(a_grid)
    sum_list = []
    j = grid_size -1
    # pdb.set_trace()
    #take left diagonal
    for i in range(grid_size):
        sum_list.append(a_grid[i][i])
        #take right diagonal
        sum_list.append(a_grid[i][j]) 
        j -= 1
    #remove the double counting of the center tile 
    return (sum(sum_list)-a_grid[(grid_size//2)][(grid_size//2)])

# print(calcGridDiagonalSum(fillSpiralGrid(1001)))

"""
problem 29

Consider all integer combinations of a**b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

2**2=4, 2**3=8, 2**4=16, 2**5=32
3**2=9, 3**3=27, 3**4=81, 3**5=243
4**2=16, 4**3=64, 4**4=256, 4**5=1024
5**2=25, 5**3=125, 5**4=625, 5**5=3125
If they are then placed in numerical order, with any repeats removed, 
we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""

def distinctPowers(upper_limit):
    """assumes upper_list is an int, representing the highest possible values of a and b
    returns an int, the number of distinct values of a**b 
    for 2 ≤ a ≤ upper_limit and 2 ≤ b ≤ upper_limit
    """
    squares_list = []
    for a in range(2, upper_limit+1):
        for b in range(2, upper_limit+1):
            squares_list.append(a**b)
    squares_set = set(squares_list)
    return (len(squares_set))

# print(distinctPowers(100))

"""
problem 30 

There are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
# pick arbitrary upper_limit (100000?)

def digitFifthPowers(upper_limit):
    """assumes upper_limit is an int, the number up to which to look for 
    numbers that can be written as the sum of fifth powers of their digits
    returns an int, the sum of the numbers that can be written as the sum of fifth powers of their digits
    """
    digit_fifth_powers_list = []
    for num in range(10,upper_limit):
        print(num)
        num_string = str(num)
        fifth_power_sum = 0 
        for digit in num_string:
            fifth_power_sum += int(digit)**5
        if num == fifth_power_sum:
            digit_fifth_powers_list.append(num)
    return sum(digit_fifth_powers_list)

# print(digitFifthPowers(1000000))






































