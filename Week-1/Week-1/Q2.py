# Largest and Smallest of 3 Numbers

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

