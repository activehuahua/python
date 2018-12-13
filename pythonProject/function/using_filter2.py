def is_palindrome(n):
    L1=str(n)

    return  L1[:]==L1[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))