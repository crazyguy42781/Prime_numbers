class BaseConvert:

    NUMERAL = "0123456789"
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    EXTRAS = "!@#$%^&*-_=+<,.>/?"
    ABOVE_EXTRAS = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    BASE = NUMERAL + UPPER + LOWER + EXTRAS + ABOVE_EXTRAS
    FOLDER_PATH = r'C:\\Users\\owner\\Documents\\Projects\\Prime_numbers\\database\\'

    def __init__(self, value=1):
        self.value = value

    def __lt__(self, other):
        return self.to_decimal() < other.to_decimal()

    def __le__(self, other):
        return self.to_decimal() <= other.to_decimal()

    def __eq__(self, other):
        return self.to_decimal() == other.to_decimal()

    def __ne__(self, other):
        return self.to_decimal() != other.to_decimal()

    def __ge__(self, other):
        return self.to_decimal() >= other.to_decimal()

    def __gt__(self, other):
        return self.to_decimal() > other.to_decimal()

    def to_decimal(self):
        base = len(self.BASE)
        result = 0

        for char in self.value:
            result = result * base + self.BASE.index(char)
        return result

    def __repr__(self):
        return f"Base62Number({self.value})"

    def encode(self):
        if self.value == 0:
            return self.BASE[0]

        result = ""
        base = len(self.BASE)
        while self.value > 0:
            self.value, remainder = divmod(self.value, base)
            result = self.BASE[remainder] + result
        if len(result) > 1:
            result = ":" + result
        if len(result[1:]) > 2:
            result = result + "|"
        return result

    def read_file(self, filename="conversion-2-32.txt"):
        decode_value = ""
        with open(self.FOLDER_PATH + filename, "r") as f:
            line_input = f.readline()
            # line_input = f.read(10_000)
            idx = 0
            while idx < len(line_input):
                if line_input[idx] == "[":
                    start_idx = idx + 1
                    end_idx = line_input.find("]", start_idx)
                    self.value = line_input[start_idx: end_idx]
                    # print(self.value, start_idx, end_idx)
                    decode_value += (self.to_decimal() * "0")
                    break
                elif line_input[idx] == ":":
                    start_idx = idx + 1
                    end_idx = line_input.find("|", start_idx)
                    if end_idx == -1 or end_idx - start_idx > 6:
                        end_idx = start_idx + 2
                    self.value = line_input[start_idx:end_idx]
                    idx += (end_idx - start_idx)
                else:
                    self.value = line_input[idx]

                d = self.to_decimal()
                decode_value += (d * "0") + "1"
                idx += 1
        return decode_value, line_input