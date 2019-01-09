#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Jan  9 16:17:30 2019

@author: astoned
"""

# A = P (1+ r/n)**nt
# Where P = principal, r = annual nominal interest rate in decimals,
# n = number of time r is compounded per year, t = number of years

# Write a Python program that assigns the principal amount of $10000 
# to variable P, assign to n the value 12, and assign to r the interest
# rate of 8%. Then have the program prompt the user for the number of 
# years t that the money will be compounded for. Calculate and print 
# the final amount after t years.

p = 10000
n = 12
r = 0.08
t = int(input('Number of years? '))

a = p*(1 + r/n)**(n*t)

print('Final ammount (A) after', t, 'is', a)