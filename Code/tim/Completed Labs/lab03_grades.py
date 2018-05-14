while True:
    try:
        answer = float(input('What did you get on the test? > '))
        break
    except ValueError:
        print('LIES! Try again.')
        continue

if answer > 100:
    mod_grade = 9
else:
    mod_grade = answer % 10

if answer >= 90:
    answer = 'A'
    congrats = 'Good Job!'
elif answer >= 80:
    answer = 'B'
    congrats = 'Good Job!'
elif answer >= 70:
    answer = 'C'
    congrats = ''
elif answer >= 60:
    answer = 'D'
    congrats = 'Booooo!'
else:
    answer = 'F'
    congrats = 'Booooo!'
    mod_grade = 5

if mod_grade >= 7:
    mod_grade = '+'
elif mod_grade <= 3:
    mod_grade = '-'
else:
    mod_grade = ''

print('You got a', answer + mod_grade + '.', congrats)