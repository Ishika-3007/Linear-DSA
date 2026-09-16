# Calculate total, percentage, and grade
sub1 = 89
sub2 = 90
sub3 = 57
sub4 = 99
sub5 = 100
total_marks = sub1 + sub2 + sub3 + sub4 +sub5
print (" total marks", total_marks)
percentage  = sub1 + sub2 + sub3 + sub4 +sub5/5
print(percentage)
if percentage >= 90:
    if percentage >= 90:
     grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"


print(grade)    
