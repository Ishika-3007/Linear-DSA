# Function to check whether a number is even, odd, or prime
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
