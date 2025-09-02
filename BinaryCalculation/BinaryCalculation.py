# ============================================
# Author: Suraj Prasai
# File: BinaryCalculation.py
# Date: 2025-08-29
# Description: A module for performing basic binary calculations.
# ============================================

def xorGate(a: str, b: str) -> str:
    return '1' if a != b else '0'

def andGate(a: str, b: str) -> str:
    return '1' if a == '1' and b == '1' else '0'

def orGate(a: str, b: str) -> str:
    return '1' if a == '1' or b == '1' else '0'

def notGate(a: str) -> str:
    return '0' if a == '1' else '1'

def shiftLeft(a: str, n: int) -> str:
    return a[n:] + '0' * n

def shiftRight(a: str, n: int) -> str:
    return '0' * n + a[:-n] if n < len(a) else '0' * len(a)

def decimal_to_binary(num: int) -> str:
    sign = "" if num >= 0 else "-"
    num = abs(num)
    if num == 0:
        return '0'
    
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary # Append remainder. Binary added later as the order is reversed
        num //= 2   # Update num to quotient

    return sign + binary

def binary_to_decimal(binary: str) -> str:
    sign = "-" if binary.startswith('-') else ""
    if binary.startswith(('-', '+')):
        binary = binary[1:]

    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            decimal += 2 ** i
    return sign + str(decimal)


def test_conversions():
    assert decimal_to_binary(10) == '1010'
    assert decimal_to_binary(-10) == '-1010'
    assert decimal_to_binary(0) == '0'
    assert binary_to_decimal('1010') == '10'
    assert binary_to_decimal('-1010') == '-10'
    assert binary_to_decimal('0') == '0'
    print("All conversion tests passed.")

if __name__ == "__main__":
    a = '1101'
    b = '1011'
    print(f"XOR of {a} and {b}: {xorGate(a, b)}")
    print(f"AND of {a} and {b}: {andGate(a, b)}")
    print(f"OR of {a} and {b}: {orGate(a, b)}")
    print(f"NOT of {a}: {notGate(a)}")
    print(f"Shift left {a} by 2: {shiftLeft(a, 2)}")
    print(f"Shift right {a} by 2: {shiftRight(a, 2)}")
    test_conversions()