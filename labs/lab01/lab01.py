def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    # want to take any value of n and make a while loop that decreases it k times
    total = 1
    index = 0
    while index < k:
    # then/simultaneously multiple each value
        total = total * n
        index = index + 1
        n = n - 1
    return total


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    #if y is any single digit then it would be the same as adding 0 so return itself
    if y < 10:
        return y
    else:
    #want to add the results of the numbers to the left with modulus
    #and number to the right using floor divison
        numbers, last_digit = y // 10, y % 10
        return sum_digits(numbers) + last_digit

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
