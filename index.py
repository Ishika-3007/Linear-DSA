# Q1. Check whether a number is positive, negative, or zero

num = 10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


    # Q2. Largest and Smallest of 3 Numbers

a= 10
b =20
c = 62

#3 Find largest
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

# Find smallest
if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c

print("Largest:", largest)
print("Smallest:", smallest)


# Q4. Calculate total, percentage, and grade
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


# Q5. Calculate the sum of all digits of a number
n = 1
sum =0
for i in range ( 1,11,1):
 sum = sum +n
 print (sum)


# Q6. Function taking two numbers and an operator


def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1* n2
    
    elif op == "*":
        return n1% n2
    else:
        return n1 / n2



print( ( calculate(10,30,"+")))
print( ( calculate(10,30,"-")))
print( ( calculate(10,30,"/")))
print( ( calculate(10,30,"*")))
print( ( calculate(10,30,"%")))


# Q7. Function to check whether a number is even, odd, or prime
def check_number(num):
    if num < 2:
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        return "Prime"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"



print(check_number(15))

# Q8. Check whether a number is prime
num = 3

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")


# Q9. Calculate factorial using a loop

factorial = 1

for i in range(1, 6):
    factorial = factorial * i

print("Factorial:", factorial)        