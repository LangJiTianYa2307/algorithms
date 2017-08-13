def is_palindrome(n):
    if n<10:
        return True
    elif n >= 10 and n < 100:
        if n%10 == n//10:
            return True
        else:
            return False
    elif n >= 100 and n<1000:
        bai = n//100
        shi = n%100//10
        ge = n%10
        if ge*100+shi*10+bai == n:
            return True
        else:
            return False

output = filter(is_palindrome, range(1, 1000))
print(list(output))