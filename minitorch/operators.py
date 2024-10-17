"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(a: float, b: float) -> float:
    return a*b
# - id
def id(a:float)->float:
    return a
# - add
def add(a:float,b:float)->float:
    return a+b
# - neg
def neg(a:float)->float:
    return -a
# - lt
def lt(a:float,b:float)->bool:
    return a<b
# - eq
def eq(a:float,b:float)->bool:
    return a==b
# - max
def max(a:float,b:float)->float:
    return a if a>b else b
# - is_close
def is_close(a:float,b:float)->bool:
    return abs(a-b)<1e-2
# - sigmoid
def sigmoid(a:float)->float:
    return 1.0/(1.0+math.exp(-a))
# - relu
def relu(a:float)->float:
    return a if a>0 else 0
# - log
def log(a:float)->float:
    return math.log(a)
# - exp
def exp(a:float)->float:
    return math.exp(a)
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
