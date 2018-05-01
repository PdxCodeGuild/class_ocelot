



def factorial_iterative(n):
    r = n
    while n > 1:
        n -= 1
        r *= n
    return r

print(factorial_iterative(4))

def factorial_recursive(n):
    if n == 0:
        return 1
    print(f'{n}*factorial({n-1})')
    r = n*factorial_recursive(n-1)
    print(f'returning {r}')
    return r

print(factorial_recursive(4))


