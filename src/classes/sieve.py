# local imports
import math
import sys
import os

# Third party imports
import gmpy2
from bitarray import bitarray

# locally created imports


class PrimeSieve:
    def __init__(self, base: int = 2, exp: int = 2):
        # Sets the base number and exponent
        self.base = base
        self.exp = exp

        # setting up the gmpy2 context manager
        gmpy2.get_context().precision = math.floor(exp * math.log(gmpy2.mpz(self.base))) + 1

        # Calculating the big number
        self.number = (self.base ** self.exp)

        # Creating the bit array
        self.bits = bitarray(self.number)

        # setting all bits to true
        self.bits.setall(1)

    def bit_counts(self) -> int:
        return self.bits.count()
