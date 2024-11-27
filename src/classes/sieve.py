import sys
from bitarray import bitarray
from classes.base_convert import BaseConvert

sys.set_int_max_str_digits(1_000_000_000)


class Sieve:
    def __init__(self, limit=1_000_000):
        self.limit = limit + 1
        self.bit_array = bitarray(self.limit)
        self.bit_array.setall(True)

    def genesis_sieve(self) -> None:
        start = 11
        stop = int(self.limit ** 0.5) + 1
        step = 2
        num = 0
        idx = 0
        self.bit_array[:2] = False
        # self.bit_array[4::2] = False
        # self.bit_array[6::3] = False
        # self.bit_array[10::5] = False
        # self.bit_array[14::7] = False
    
        # for num in range(start, stop, step):
        while num < self.limit ** 0.5:
            # if str(num)[-1] in [0,2,4,5,6,8]:
            #     continue
            # if self.bit_array[num]:
            #     self.bit_array[num * num: self.limit + 1: num] = False
            num = self.bit_array.find(1, idx)
            self.bit_array[num * num: self.limit + 1: num] = False
            idx = num + 1

        return None

    def convert_sieve(self) -> (int, str, int):
        last_idx = 0
        idx = 0
        p = 0
        gap = 0
        gap_size = 0
        s = ""
        c = ""
        last_p = 0
        # while idx <= self.limit:
        #     p = self.bit_array.find(1, idx)
        #     if p < 1:
        #         last_p = idx - 1
        #         s += f"[{BaseConvert((self.limit - 1) - idx).encode()}]"
        #         break
        #     if p == 1:
        #         p = 2
        #     gap_size = p - last_idx
        #     c = BaseConvert(gap_size).encode()
        #     s += c
        #     if gap_size > gap:
        #         gap = gap_size
        #     if gap_size > 125:
        #         d = ((idx / self.limit) * 100)
        #         print(f"Stop Prime: {p:,} - gap: {gap_size} - Converted: {c} - "
        #               f"{d:.2f}%")
        #     idx = p + 1
        #     last_idx = p
        while idx < self.limit:

            if self.bit_array[idx]:
                c = BaseConvert(gap_size).encode()
                s += c
                if gap_size > gap:
                    gap = gap_size
                if gap_size > 199:
                    d = ((idx / self.limit) * 100)
                    print(f"Stop Prime: {idx:,} - gap: {gap_size} - Converted: "
                          f"{c} - {d:.2f}%")
                gap_size = 0
            else:
                gap_size += 1
            idx += 1
        s += f"[{BaseConvert(gap_size).encode()}]"
        return gap, s, gap_size #last_p
