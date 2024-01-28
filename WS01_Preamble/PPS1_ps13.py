# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:14:06 2023

@author: 22pw29
"""
from math import pow

p = int(input())
r = int(input())
t = int(input())
n = int(input())
si= (p*r*t)/100
ci = p*pow((1+r/n),n*t)

print(f" {si} {ci}")