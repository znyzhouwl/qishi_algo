def isPowerOfTwo(n: int) -> bool:
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        else:
            n = int(n/2)
    return True
