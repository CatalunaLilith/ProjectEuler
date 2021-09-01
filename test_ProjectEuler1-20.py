# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:25:37 2021

@author: catal
"""

import unittest 
from testKittens import testKittens
from ProjectEuler1_20 import SumOf3Or5


"""problem 1""" 
class EulerTest(unittest.TestCase):
    
    def testProblem1(self):
        self.assertAlmostEqual(ProjectEuler1_20.SumOf3Or5(1000),233168)
    
    def testTestKittens(self):
        self.assertAlmostEqual(testKittens(), "kittens")

if __name__ == '__main__':
    unittest.main()
