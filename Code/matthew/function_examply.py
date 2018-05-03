




def some_stuff(**d):
    print(d)

some_stuff(a=1, b=2, c=3)



def some_stuff2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

some_stuff2(1, 2, 3, 4, e=1, c=2, d=3)





def sum(*args):
    total = 0
    for e in args:
        total += e
    return total

print(sum(5, 6, 7))



def sum2(args):
    total = 0
    for e in args:
        total += e
    return total

sum2([5, 6, 7])



def add(a, b=1):
    print(a)
    print(b)
    return a + b

c = add(5, 2)
d = add(5)
e = add(5, b=2)





