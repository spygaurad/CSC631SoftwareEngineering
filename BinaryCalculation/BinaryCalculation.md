# Binary Calculation Module Documentation

This module provides functions for performing basic binary calculations, including:

- **Logic Gates:** `xorGate`, `andGate`, `orGate`, `notGate`
- **Bit Shifting:** `shiftLeft`, `shiftRight`
- **Decimal-Binary Conversion:** `decimal_to_binary`, `binary_to_decimal`
- **Binary Subtraction:** `ripple_subtract_binary`

## Logic Gates

These functions implement the basic logic gates: XOR, AND, OR, and NOT.

- `xorGate(a: str, b: str) -> str`: Returns '1' if a and b are different, '0' otherwise.
- `andGate(a: str, b: str) -> str`: Returns '1' if both a and b are '1', '0' otherwise.
- `orGate(a: str, b: str) -> str`: Returns '1' if either a or b is '1', '0' otherwise.
- `notGate(a: str) -> str`: Returns '0' if a is '1', '1' otherwise.

## Bit Shifting

These functions perform left and right bit shifts.

- `shiftLeft(a: str, n: int) -> str`: Shifts the binary string `a` to the left by `n` positions, adding '0's to the right.
- `shiftRight(a: str, n: int) -> str`: Shifts the binary string `a` to the right by `n` positions, adding '0's to the left.

## Decimal-Binary Conversion

These functions convert between decimal and binary representations.

- `decimal_to_binary(num: int) -> str`: Converts a decimal number to its binary string representation.  Handles negative numbers using two's complement.
- `binary_to_decimal(binary: str) -> str`: Converts a binary string to its decimal representation. Handles negative numbers represented in two's complement.

## Binary Subtraction

This function performs binary subtraction using the ripple borrow method.

- `ripple_subtract_binary(a: str, b: str) -> str`: Subtracts binary string `b` from binary string `a` using bitwise operations.

## Example Usage

```python
from BinaryCalculation.BinaryCalculation import decimal_to_binary, binary_to_decimal, ripple_subtract_binary

a = 500
b = 3
a_bin = decimal_to_binary(a)
b_bin = decimal_to_binary(b)
print(f"{a} in binary is {a_bin}")
print(f"{b} in binary is {b_bin}")
result_bin = ripple_subtract_binary(a_bin, b_bin)
result_dec = binary_to_decimal(result_bin)
print(f"Subtraction of {a} - {b} in binary is {result_bin} which is {result_dec} in decimal")
```

## Error Handling

The module includes basic error handling for invalid input types and values.  However, more robust error handling could be added for production use.

## Testing

The module includes unit tests to verify the correctness of the functions.  These tests can be run using the `unittest` module.

```python
python -m unittest BinaryCalculation.BinaryCalculation
