_**Background**_:

Computers do not understand decimal numbers (0–9) directly. Instead, they use **binary digits (bits)**, where each digit is either `0` (off) or `1` (on).

- The binary number `0101` equals `5` in decimal.
- Arithmetic operations such as addition and subtraction are carried out using **logic gates** inside the CPU (AND, OR, XOR, NOT).
- Subtraction is usually implemented using the **two’s complement method**, where subtraction is transformed into addition.
  example: 0101 (binary 5); 0011 (binary 3; 0010 (binary 2)

- Place Value System:

  - Similar to how decimal numbers work, 342-> (3 × 10²) + (5 × 10¹) + (2 × 10⁰),
  - Binary Works the same with base 2: e.g. 0101 -> (0×8) + (1×4) + (0×2) + (1×1)

- Computers use Binary because they only understand0 (off, low voltage)m and 1(on, high voltage).
- Logic Gates:
  - Inside CPU, arithmetic is done via Logic Gates.
  - NOT: Flips 0 <-> 1
  - AND: 1 only if both inputs are 1 else 0
  - OR: 1 if either input is 1
  - XOR: 1 if inputs are different
- Addition in Binary
  - Addition works just like Decimal
    - 0+0 = 0
    - 0+1 = 1
    - 1+0 = 1
    - 1 + 1 = 10 (0 with a carry of 1)
  - To add multi bit numbers, we use adders:
    - Half Adder: adds 2 bits (sum + carry)
    - Full Adder: adds 2 bits + an extra carry-in
  - A **Half Adder** is the simplest circuit that adds 2 bits (`a` and `b`)
  - If you add `1 + 1`, the sum is `0` and carry is `1` → together that means binary `10` (which is 2).
  - Half Adder can’t handle a **carry-in** from a previous column. That’s where **Full Adder** comes in.
  - A **Full Adder** adds 3 inputs:
    - bit `a`
    - bit `b`
    - carry-in (`c_in`)
  - **The result of the sum of binary is the XOR gate, and the carry is the output of AND gate between the bits**
- The problem of subtraction
  - Computers dont like to build extra circuits for subtraction so we use a trick to turn subtraction into addition using Two's complement.
- **Two's Complement**
  - In decimal we represent negative numbers as -5, with a sign
  - In binary, we store everything in fixed width patterns like 4bits, 8bits
  - Steps to represent -x in N bits:
    - write x in binary: 3 -> 0011 (in 4 bits)
    - invert all bits -> 1100
    - Add 1 -> 1101
    - Now 1101 means "-3" in 4 bit two's complement
  - To identify the bit width, we follow a general method. for example between -2 and +2, there are 5 number including the 2's. To represent 5 numbers we need minimum of 8 options, 2^3
  - For any negative integer x:
    - Take |x|(absolute value).
    - Find the smallest power of 2 greater than or equal to ∣x∣|x|∣x∣.
    - 2^N-1 ∣x∣
    - That N is the required bit-width.
    - to represent -123, we need 8 bits in twos complement.
- **Using Two's Complement to do Subtraction**
  - Compute `5 − 3` in 4 bits.
  - A − B`becomes`A + (−B)`.
  - Two’s complement of 3 = `1101` (this is −3)
  - Add: `0101 + 1101 = 10010`. Ignore the extra left bit → `0010` = 2.
- Overflow
  - Beware of the bit limits
  - in 4 bits, signed range is -8 to +7. The range is -8 to +7 because two's complement gives one additional -ve number. +7 -> 0111 -> bit flip -> 1000 -> -8. When you have n bits, the largest you can store is 2^n -1.
  - If results go outside, we get overflow
  - If you add 7 + 1, we get an overflow
  - if you add (-7) and (-2), we get an overflow
- CPU has flags to track these:
  - **Z (Zero)**: result = 0
  - **N (Negative)**: result is negative (MSB = 1)
  - **C (Carry)**: unsigned overflow (extra carry out)
  - **V (Overflow)**: signed overflow (wrong sign result)
- **Borrow Method of Subtraction**
  - Question: The subtraction should be computed using **binary logic operations** (XOR, AND, NOT, shifts).
  - Shifts:
    - Left Shift : Shift left, add 0: Doubles the number as a higher order is a multiple of 2. if we left shift 4, we get 8. 0100 -> 1000
    - Right Shift: halves
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

1.
