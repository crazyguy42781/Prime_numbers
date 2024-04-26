# local imports
import math
import sys
import os

# Third party imports
import gmpy2
from bitarray import bitarray

# locally created imports
from classes.sieve import PrimeSieve


if __name__ == '__name__':
    bits = PrimeSieve(base=10, exp=5)
    print(bits.bits[0:20])
    print("hi")
