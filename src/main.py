from bitarray import bitarray
import time
import sys
from classes.base_convert import BaseConvert


from classes.sieve import Sieve

sys.set_int_max_str_digits(1_000_000_000)

if __name__ == '__main__':
    # bit_limit = 100_000_000
    bit_limit = 2 ** 32
    bit_array = Sieve(bit_limit)
    print(len(BaseConvert.BASE))
    start = time.monotonic()
    print("Processing Sieve")
    bit_array.genesis_sieve()
    print("Sieve setup completed")
    print("Processing The Prime Counting")
    g, st, l = bit_array.convert_sieve()
    print(f"Biggest gap in {bit_limit:,} is: {g:,}")
    print(f"Total nuber of primes used: {bit_array.bit_array.count():,}")
    print(f"Length of converted: {len(st):,}")
    print(f"Percentage of compression: {100 - ((len(st) / bit_limit) * 100):,.2f}")
    print(f"completed in seconds: {time.monotonic() - start:.2f}")
    print(f"{l:,}")
    file_name = r"C:\Users\owner\Documents\Projects\Prime_numbers\database\conversion" \
                r"-2-32.txt"
    # print(st)
    with open(file_name, 'w') as f:
        f.write(st)

    # v, l = BaseConvert().read_file("conversion-2-32.txt")
    # # for idx, each in enumerate(v):
    # #     print(f"{idx} - {each}")
    # print(f"v: {len(v):,} - Bit_array: {len(bit_array.bit_array.to01()):,}")
    # print(v == bit_array.bit_array.to01())
    # step = 200
    # for i in range(17051700, bit_limit, step):
    #     if v[i: i + step] != bit_array.bit_array[i: i + step].to01():
    #         print(i)
    #         print(v[i: i + step])
    #         print(bit_array.bit_array[i: i + step].to01())
    #
    #         break
    # start_idx = l.find(":", 1094421)
    # print(start_idx, l[start_idx: start_idx + 3])
    # print(BaseConvert(l[start_idx + 1: start_idx + 3]).to_decimal())
