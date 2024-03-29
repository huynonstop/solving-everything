class Solution:
    def hammingWeight(self, n: int) -> int:
        return count_bit_1(n)


def count_bit_1(n):
    cur = n
    count = 0
    while cur > 0:
        count += (cur & 1)
        cur = cur >> 1
    return count


# n & (n - 1) drops the lowest set bit. It's a neat little bit trick.

# Let's use n = 00101100 as an example. This binary representation has three 1s.

# If n = 00101100, then n - 1 = 00101011, so n & (n - 1) = 00101100 & 00101011 = 00101000. Count = 1.

# If n = 00101000, then n - 1 = 00100111, so n & (n - 1) = 00101000 & 00100111 = 00100000. Count = 2.

# If n = 00100000, then n - 1 = 00011111, so n & (n - 1) = 00100000 & 00011111 = 00000000. Count = 3.

# n is now zero, so the while loop ends, and the final count (the numbers of set bits) is returned.

def count_bit_1_2(n):
    count = 0
    cur = n
    while cur > 0:
        count += (cur & 1)
        cur = cur & (cur - 1)
    return count
