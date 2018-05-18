grade_score = input("What score did you receive? > ")
grade_score = int(grade_score)
if grade_score >= 90:
  print('A')
elif grade_score >= 80:
  print('B')
elif grade_score >= 70:
    print('C')
elif grade_score >= 60:
    print('D')
elif grade_score <= 59:
    print("F")