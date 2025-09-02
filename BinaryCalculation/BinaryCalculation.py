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

'''
  - Subtraction (a,b):
    - 0-0:0
    - 1-0:1
    - 0-1:1 (need borrow)
    - 1-1:0
    - The operations above represent a XOR B.
    - For Borrow it happens when a=0 and b =1 (which is not(a) AND b) , we borrow from higher placed bit, so we need to subtract the borrow till borrow is 0. For this we shift the borrow to higher bit i.e left shift and then subtract it again from the a XOR B.
    - while B != 0:
      borrow = (~A) & B # places where A has 0 and B has 1 → need borrow
      A = A ^ B # difference ignoring borrow
      B = borrow << 1
    - return A
'''
def _bitwise_not(a: str) -> str:
    return ''.join(notGate(ch) for ch in a)

def _bitwise_and(a: str, b: str) -> str:
    a, b = _pad_equal(a, b)
    return ''.join(andGate(x, y) for x, y in zip(a, b))

def _bitwise_xor(a: str, b: str) -> str:
    a, b = _pad_equal(a, b)
    return ''.join(xorGate(x, y) for x, y in zip(a, b))

# Pad two binary strings to be of equal length by adding zeros on left
def _pad_equal(a: str, b: str) -> tuple[str, str]:
    n = max(len(a), len(b))
    return a.zfill(n), b.zfill(n)

# Check if all characters in the string are '0'
def _is_all_zero(s: str) -> bool:
    return all(ch == '0' for ch in s)

def ripple_subtract_binary(a: str, b: str) -> str:
    #Ensuring both are of same length
    #Pad by the maximum length
    a,b = _pad_equal(a,b)
    borrow = 0

    while not _is_all_zero(b):
        borrow = _bitwise_and(_bitwise_not(a), b)
        a = _bitwise_xor(a, b)
        b = shiftLeft(borrow, 1)
    
    return ''.join(a).lstrip('0') or '0'

def test_logic_gates():
    assert xorGate('0', '0') == '0'
    assert andGate('1', '1') == '1'
    assert orGate('1', '1') == '1'
    assert notGate('1') == '0'
    assert shiftLeft('1101', 2) == '0100'
    assert shiftRight('1101', 2) == '0011'
    print("All logic gate tests passed.")

def test_conversions():
    assert decimal_to_binary(4) == '100' #Will give error if '0100'
    assert decimal_to_binary(-1) == '-1'
    assert binary_to_decimal('111') == '7'
    assert binary_to_decimal('-1111') == '-15'
    print("All conversion tests passed.")

def test_binary_subtraction():
    assert ripple_subtract_binary('1101', '101') == '1000'
    assert ripple_subtract_binary('1000', '1') == '111'
    assert ripple_subtract_binary('1010', '1010') == '0'
    # assert ripple_subtract_binary('1', '1000') == '-111' #Negative result not handled

    print("All binary subtraction tests passed.")

if __name__ == "__main__":
    test_logic_gates()
    test_conversions()
    test_binary_subtraction()

    # Example usage
    a = 500
    b = 3
    a_bin = decimal_to_binary(a)
    b_bin = decimal_to_binary(b)
    print(f"{a} in binary is {a_bin}")
    print(f"{b} in binary is {b_bin}")
    result_bin = ripple_subtract_binary(a_bin, b_bin)
    result_dec = binary_to_decimal(result_bin)
    print(f"Subtraction of {a} - {b} in binary is {result_bin} which is {result_dec} in decimal")
