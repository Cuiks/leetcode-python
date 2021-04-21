def isPalindrome(x: int):
    if x < 0:
        return False
    temp = x
    val = 0
    while temp:
        val = val * 10 + temp % 10
        temp = int(temp / 10)
    if val == x:
        return True
    return False


print(isPalindrome(121))
