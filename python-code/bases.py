digits = list("0123456789abcdefghijklmnopqrstuvwxyz")

class baseNum:
    def __init__(self, base: int = 10, value: any = 0):
        self._base = base
        self._decValue = 0
        self.digits = []
        self._value = ""
        self.setValue(value)
        self.calculate()

    def __str__(self, showBase: bool = False):
        base = f"({self._base})" if showBase else ""
        return f"{self._value}{base}"

    def calculate(self):
        if 2 <= self._base <= len(digits):
            self.digits = digits[:self._base]
        else:
            raise Exception(f"Currently only bases 2-{len(digits)} are allowed, sorry")

        tempArr = []
        tempNum = self._decValue
        while tempNum > 0:
            tempArr.append(self.digits[tempNum % self._base])
            tempNum //= self._base
        tempArr.reverse()
        self._value = "".join(tempArr) or "0"

    def setValue(self, value: any):
        if isinstance(value, int):
            self._decValue = value
        elif isinstance(value, str):
            self._decValue = self.strToDec(value, self._base)
        else:
            raise ValueError("Unsupported value type")

    def strToDec(self, value: str, base: int) -> int:
        value = value.lower()
        decValue = 0
        for char in value:
            if char in digits[:base]:
                decValue = decValue * base + digits.index(char)
            else:
                raise ValueError(f"Invalid character {char} for base {base}")
        return decValue

    def format(self, val = 4):
        if len(self._value) < val:
            self._value = "".join(["0"]*(val-len(self._value)))+self._value
        else:
            self._value = self._value[-val:]
        return self._value

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base: int):
        self._base = base
        self.calculate()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: any):
        self.setValue(value)
        self.calculate()

    def __add__(self, other):
        if isinstance(other, baseNum):
            return baseNum(self._base, self._decValue + other._decValue)
        elif isinstance(other, int):
            return baseNum(self._base, self._decValue + other)
        else:
            raise ValueError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, baseNum):
            return baseNum(self._base, self._decValue - other._decValue)
        elif isinstance(other, int):
            return baseNum(self._base, self._decValue - other)
        else:
            raise ValueError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, baseNum):
            return baseNum(self._base, self._decValue * other._decValue)
        elif isinstance(other, int):
            return baseNum(self._base, self._decValue * other)
        else:
            raise ValueError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, baseNum):
            if other._decValue == 0:
                raise ZeroDivisionError("Division by zero")
            return baseNum(self._base, self._decValue // other._decValue)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return baseNum(self._base, self._decValue // other)
        else:
            raise ValueError("Unsupported operand type")
    
    def __mod__(self, other): 
        if isinstance(other, baseNum): 
            return baseNum(self._base, self._decValue % other._decValue) 
        elif isinstance(other, int): 
            return baseNum(self._base, self._decValue % other) 
        else: 
            raise ValueError("Unsupported operand type")
        
    def __pow__(self, other):
        if isinstance(other, baseNum):
            return baseNum(self._base, self._decValue ** other._decValue)
        elif isinstance(other, int):
            return baseNum(self._base, self._decValue ** other)
        else:
            raise ValueError("Unsupported operand type")


def read(name: str, base: int = 2, isInt: bool = False):
    base_nums = []
    with open(name, "rb") as file:
        bytes_data = file.read()
        for byte in bytes_data:
            if isInt:
                base_num = baseNum(base, byte).__str__()
            else:
                base_num = baseNum(base, byte)
            base_nums.append(base_num)
    return base_nums

def write(name: str, base_nums: list):
    with open(name, "wb") as file:
        bytes_data = bytearray()
        for base_num in base_nums:
            if isinstance(base_num, baseNum):
                byte_value = base_num._decValue
                if 0 <= byte_value <= 255:
                    bytes_data.append(byte_value)
                else:
                    raise ValueError(f"Value {byte_value} out of byte range (0-255)")
            else:
                raise TypeError("List must contain only baseNum objects")
        file.write(bytes_data)
