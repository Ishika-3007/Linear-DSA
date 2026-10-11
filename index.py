# 🟢 Level 1 — Basic List Practice
# 1. Write a Python program to create a list of 8 numbers and print the first three and last three elements.===
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# print("First three elements:", numbers[:3])
# print("Last three elements:", numbers[-3:])


# 2.Write a Python program to print all elements of a list along with their indexes.===
# numbers = [10, 20, 30, 40, 50]

# for i in range(0,len(numbers)):
#     print("Index:", i, "Element:", numbers[i])


# 3.Write a Python program to find the length of a list without using len().===
# numbers = [10, 20, 30, 40, 50]

# count = 0

# for item in numbers:
#     count += 1

# print("Length of list:", count)


# 4.Write a Python program to calculate the sum of all positive numbers in a list.===
# numbers = [-5, 10, -3, 20, 0, 15]

# total = 0

# for num in numbers:
#     if num > 0:
#         total += num

# print("Sum of positive numbers:", total)


# 5.Write a Python program to calculate the sum of all negative numbers in a list.===
# numbers = [-5, 10, -3, 20, -7, 15]

# total = 0

# for num in numbers:
#     if num < 0:
#         total += num

# print("Sum of negative numbers:", total)


# 6.Write a Python program to count how many positive, negative, and zero values are present in a list====
# numbers = [-5, 10, 0, -3, 20, 0, 15]

# positive = 0
# negative = 0
# zero = 0

# for num in numbers:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1

# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zero values:", zero)


# #7. Write a Python program to find the average of only the even numbers in a list.===
# numbers = [10, 15, 20, 25, 30, 35]

# total = 0
# count = 0

# for num in numbers:
#     if num % 2 == 0:
#         total += num
#         count += 1

# if count > 0:
#     average = total / count
#     print("Average of even numbers:", average)
# else:
#     print("No even numbers found.")


# # 8.Write a Python program to find the average of only the odd numbers in a list.===
# numbers = [10, 15, 20, 25, 30, 35]

# total = 0
# count = 0

# for num in numbers:
#     if num % 2 != 0:
#         total += num
#         count += 1

# if count > 0:
#     average = total / count
#     print("Average of odd numbers:", average)
# else:
#     print("No odd numbers found.")


# # 9.Write a Python program to print the elements of a list in reverse order without using reverse().====
# numbers = [10, 20, 30, 40, 50]

# for i in range(len(numbers) - 1, -1, -1):
#     print(numbers[i])


# # W10.rite a Python program to create a new list containing the squares of all elements from an existing list.====
# numbers = [1, 2, 3, 4, 5]

# squares = []

# for num in numbers:
#     squares.append(num **2)

# print("Original list:", numbers)
# print("Squares list:", squares)


# # 🟡 Level 2 — Searching and Counting
# # 11.Write a Python program to find the first occurrence of a given number in a list.===
# numbers = [10, 20, 30, 20, 40, 20, 50]
# target =10

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print("First occurrence at index:", i)
#         break
# else:
#     print("Number not found.")


# #12. Write a Python program to find the last occurrence of a given number in a list.===
# numbers = [10, 20, 30, 20, 40, 20, 50]
# target = 50

# last_index = -1

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         last_index = i

# if last_index != -1:
#     print("Last occurrence at index:", last_index)
# else:
#     print("Number not found.")


# # 13.Write a Python program to find all indexes where a given number occurs.===
# numbers = [10, 20, 30, 20, 40, 20, 50]
# target = 20

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print("Number found at index:", i)


# # 14.Write a Python program to count how many numbers are greater than a given number.===
# numbers = [10, 25, 15, 40, 5, 30]
# target = 20

# count = 0

# for num in numbers:
#     if num > target:
#         count += 1

# print("Numbers greater than", target, ":", count)


# # 15)write pyhon program to count how many numbers are smaller than a given number.==
# numbers = [10, 25, 15, 40, 5, 30]
# target = 20

# count = 0

# for num in numbers:
#     if num < target:
#         count += 1

# print("Numbers smaller than", target, ":", count)


# # 1)rite a Python program to find the number that occurs the most times in a list.===
# numbers = [10, 20, 10, 30, 20, 10, 40, 20]

# most_number = numbers[0]
# max_count = 0

# for num in numbers:
#     count = 0

#     for item in numbers:
#         if item == num:
#             count += 1

#     if count > max_count:
#         max_count = count
#         most_number = num

# print("Number occurring most times:", most_number)
# print("Number of occurrences:", max_count)

# # 17. Find the number that occurs only once==

# numbers = [10, 20, 10, 30, 40, 20, 50]

# for num in numbers:
#     count = 0

#     for item in numbers:
#         if item == num:
#             count += 1

#     if count == 1:
#         print("Number occurring only once:", num)


# # 18)ite a Python program to check whether all elements in a list are unique.====
# numbers = [10, 20, 30, 40, 50]

# unique = True

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             unique = False
#             break

# if unique:
#     print("All elements are unique.")
# else:
#     print("All elements are not unique.")


# # 19)rite a Python program to check whether a list contains two equal elements.====
# numbers = [10, 20, 30, 20, 40]

# found = False

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             found = True
#             break

# if found:
#     print("List contains two equal elements.")
# else:
#     print("List does not contain equal elements.")


# #20)ite a Python program to find the difference between the number of even and odd elements in a list.===
# numbers = [10, 15, 20, 25, 30, 35, 40]

# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# difference = even_count - odd_count

# print("Even elements:", even_count)
# print("Odd elements:", odd_count)
# print("Difference:", difference)


# # 🟠 Level 3 — Largest, Smallest and Position
# # 21)te a Python program to find the index of the largest element without using max()===
# numbers = [10, 25, 15, 40, 30]

# largest = numbers[0]
# largest_index = 0

# for i in range(1, len(numbers)):
#     if numbers[i] > largest:
#         largest = numbers[i]
#         largest_index = i

# print("Largest element:", largest)
# print("Index:", largest_index)


# #22)ite a Python program to find the index of the smallest element without using min().==
# numbers = [10, 25, 5, 40, 30]

# smallest = numbers[0]
# smallest_index = 0

# for i in range(1, len(numbers)):
#     if numbers[i] < smallest:
#         smallest = numbers[i]
#         smallest_index = i

# print("Smallest element:", smallest)
# print("Index:", smallest_index)


# # 23)te a Python program to find the second smallest element without using sort().===
# numbers = [10, 5, 20, 3, 15]


# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# for num in numbers:
#     if num != smallest:
#         second_smallest = num
#         break

# for num in numbers:
#     if num != smallest and num < second_smallest:
#         second_smallest = num

# print("Second smallest element:", second_smallest)



# # 24)te a Python program to find the third largest element without using sort().==
# numbers = [10, 30, 20, 50, 40]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# for num in numbers:
#     if num != largest:
#         second_largest = num
#         break

# for num in numbers:
#     if num != largest and num > second_largest:
#         second_largest = num

# for num in numbers:
#     if num != largest and num != second_largest:
#         third_largest = num
#         break

# for num in numbers:
#     if num != largest and num != second_largest and num > third_largest:
#         third_largest = num

# print("Third largest element:", third_largest)



# #25)ite a Python program to find the two largest distinct elements in a list.===
# numbers = [10, 30, 20, 50, 40, 50]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# for num in numbers:
#     if num != largest:
#         second_largest = num
#         break

# for num in numbers:
#     if num != largest and num > second_largest:
#         second_largest = num

# print("Largest:", largest)
# print("Second largest:", second_largest)


# #26)ite a Python program to find the two smallest distinct elements in a list===
# numbers = [10, 30, 5, 20, 5, 15]

# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# for num in numbers:
#     if num != smallest:
#         second_smallest = num
#         break

# for num in numbers:
#     if num != smallest and num < second_smallest:
#         second_smallest = num

# print("Smallest:", smallest)
# print("Second smallest:", second_smallest)


# #27)ite a Python program to find the difference between the largest and smallest elements==
# numbers = [10, 25, 5, 40, 30]

# # Find largest
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# # Find smallest
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# difference = largest - smallest

# print("Difference:", difference)


# #28)ite a Python program to find the sum of the largest and smallest elements.===
# numbers = [10, 25, 5, 40, 30]

# # Find largest
# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# # Find smallest
# smallest = numbers[0]

# for num in numbers:
#     if num < smallest:
#         smallest = num

# total = largest + smallest

# print("Sum:", total)


# # 29)te a Python program to find the largest even number in a list===
# numbers = [15, 22, 8, 35, 40, 17]

# for num in numbers:
#     if num % 2 == 0:
#         largest_even = num
#         break

# for num in numbers:
#     if num % 2 == 0 and num > largest_even:
#         largest_even = num

# print("Largest even number:", largest_even)


# # 30)te a Python program to find the smallest odd number in a list.=====
# numbers = [10, 15, 8, 25, 30, 7]

# for num in numbers:
#     if num % 2 != 0:
#         smallest_odd = num
#         break

# for num in numbers:
#     if num % 2 != 0 and num < smallest_odd:
#         smallest_odd = num

# print("Smallest odd number:", smallest_odd)


# 🔵 Level 4 — Modifying Lists
# #31) Write a Python program to move all negative numbers to the beginning of a list.==
# numbers = [10, 15, 8, 25, -30, -7,52,-8,55]
# negative= []
# length = len(numbers)
# for i in range(0,length):
#     if numbers[i] < 0:
#         negative.append(numbers[i])
#         # numbers .append(negative)
#         # print(numbers)
# print("Negative numbers:", negative)
# print ( negative +numbers )




# #32 Write a Python program to move all even numbers to the beginning and odd numbers to the end.===
# l1 =[1,5,4,74,88,55,20,3,6,7,9,13,25,66]
# even =[]
# odd =[]
# for i in range (0,len(l1)):
#     if l1[i ]% 2 == 0:
#         even.append(l1[i])
#     else:
#         odd.append(l1[i])
# print(even +odd )           

# # 33)Write a Python program to move all zeros to the beginning of a list.==
# l1 =[1,23,0,4,44,0,4,56,0,78,0,7,9,0,]
# zeros =[]
# non_zero = []
# for i in range (0,len(l1)):
#     if l1 [i] == 0:
#         zeros.append(l1[i])
#     else:
#           non_zero.append(l1[i])  
# print( zeros + non_zero)        

# # 34)Write a Python program to remove all occurrences of a given number without using remove().===
# l1 =[1,23,0,4,44,0,4,56,0,78,0,7,9,0,]


# #35) Write a Python program to replace every negative number with 0.===
# l1 =[1,23,80,4,44,0,4,-56,-40,78,-20,7,-9,520,]
# for i in range(0,len(l1)):
#     if l1[i] <0:
#         l1[i] = 0
# print (l1)        

# # 36)Write a Python program to replace every even number with its square.==
# l1 = [2,3,4,6,55,78,9,10]
# for i in range (0,len(l1)):
#     if l1[i] % 2 == 0:
#         l1[i] =  l1[i]**2
# print(l1)        

# # 37)Write a Python program to create a new list containing only numbers greater than 10==
# l1 = [2,30,4,67,55,78,9,10]
# no =[]
# for i in range(0,len(l1)):
#     if l1[i] > 10 :
#         no.append(l1[i])
# print(no)        


#38) Write a Python program to create a new list containing only numbers that occur exactly once.==
# l1 = [2,2,30,4,30,67,55,40,78,9,10]
# new =[]
# for i in range(0,len(l1)):
#     if l1.count(l1[i]) == 1:
#         new.append(l1[i])



# # 39)Write a Python program to remove duplicate elements while preserving their original order.
# l1 = [2, 2, 30, 4, 30, 67, 55, 40, 78, 9, 10]
# new = []
# for i in range(0,len(l1)):
#     if l1[i] not in new:
#         new.append(l1[i])
# print(new)

# # 40)Write a Python program to rotate a list one position to the right without using built-in rotation functions.==
# l1 = [1, 2, 3, 4, 5]

# l1 = l1[-1:] + l1[:-1]

# print(l1)



# 🔴 Level 5 — Prefix Sum and Array Algorithms
# 41)Write a Python program to create a prefix-sum array from a given list.

# Example:

# Input:  [3, 5, 2, 7]
# Output: [3, 8, 10, 17]

l1 =  [3, 5, 2, 7]
prefix_sum = []
sum = 0
for i in range (0, len(l1)):
    sum = sum + l1[i]
    prefix_sum.append(sum)
print(" the output is ",prefix_sum)    



# 43)Write a Python program to find the maximum prefix sum of a list.==
l1 =  [3, 5, 2, 7]
prefix_sum = []
sum = 0

for i in range (0, len(l1)):
    sum = sum + l1[i]
    prefix_sum.append(sum)
print(" the output is ",prefix_sum) 
max_sum = prefix_sum[0] 
for j in range ( 0,len(l1)):  
    if prefix_sum[j] > max_sum: 
        max_sum = prefix_sum[j] 
print("The maximum prefix sum is:", max_sum)


#44) Write a Python program to find the minimum prefix sum of a list.

l1 =  [3, 5, 2, 7]
prefix_sum = []
sum = 0

for i in range (0, len(l1)):
    sum = sum + l1[i]
    prefix_sum.append(sum)
print(" the output is ",prefix_sum) 
min_sum = prefix_sum[0] 
for j in range ( 0,len(l1)):  
    if prefix_sum[j] < min_sum: 
        min_sum = prefix_sum[j] 
print("The minimum prefix sum is:", min_sum)


# 45)Write a Python program to create a prefix-product array.

# Example:

# Input:  [2, 3, 4]
# Output: [2, 6, 24]

l1 =   [2, 3, 4]
prefix_product = []
prod = 1

for i in range (0, len(l1)):
    prod = prod * l1[i]
    prefix_product.append(prod)
print(" the output is ",prefix_product) 

# 47)Write a Python program to find the product of all elements except the current element without using division.===
a = [1, 2, 3, 4]

for i in range(len(a)):
    product = 1
    for j in range(len(a)):
        if i != j:
            product *= a[j]
    print(product)

#48) Write a Python program to find the maximum sum of any two elements in a list.==
a = [10, 20, 5, 8, 15,585]

max_sum = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] > max_sum:
            max_sum = a[i] + a[j]

print(max_sum)



# 49)Write a Python program to find the maximum sum of any three elements without using sort()===
l= [10, 20, 5, 858, 15]

max_sum = 0

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            if l[i] + l[j] + l[k] > max_sum:
                max_sum = l[i] + l[j] + l[k]

print(max_sum)

# 50)Write a Python program to find whether there exists a pair of numbers whose sum is equal to a given target.===
a = [10, 20, 5, 8, 15]
target = 25

is_found = False

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            is_found = True

print(is_found)

# Example:

# List:   [2, 7, 11, 15]
# Target: 9

# Output: True

#51) Write a Python program to find the longest consecutive sequence of 1s in a list containing only 0 and 1.

# Example:

# Input:  [1, 1, 0, 1, 1, 1, 0, 1]


a = [1, 1, 0, 1, 1, 1]
count = 0
max_count = 0

for i in range(len(a)):
    if a[i] == 1:
        count += 1
    else:
        count = 0

    if count > max_count:
        max_count = count

print(max_count)

# Output: 3