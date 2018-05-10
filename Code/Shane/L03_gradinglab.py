import math

def grading_v1(score):
    while score not in range(0,101):
        score = int(input("What's your score please?\n"))
    if score in range(90,101):
        print("A")
    elif score in range(80,90):
        print("B")
    elif score in range(70,80):
        print("C")
    elif score in range(60,70):
        print("D")
    else:
        print("F")

gradingv1=(int(input("What's your test (0-100) score please?\n")))

def roundup(num):
    if num == 100:
        return '+'
    elif num < 60:
        return ' '
    elif num % 10 < 4:
        return '-'
    elif num % 10 > 6:
        return '+'
    else:
        return ' '


def gradingv2(score):

    while score not in range(0,101):
        score = int(input("What's your score please?\n"))
    sign = roundup(score)
    if score in range(90,101):
        return f"A{sign}"
    elif score in range(80,90):
        return f"B{sign}"
    elif score in range(70,80):
        return f"C{sign}"
    elif score in range(60,70):
        return f"D{sign}"
    else:
        return "F- all F's get a minus"


print(gradingv2(int(input("What's your test (0-100) score please?\n"))))


