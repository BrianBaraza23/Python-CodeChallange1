# Challenge 2: Two numbers are positive.
# Task:
# Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

# Examples:
# (2, 4, -3) == True

# (-4, 6, 8) == True

# (4, -6, 9) == True

# (-4, 6, 0) == False

# (4, 6, 10) == False

# (-14, -3, -4) == False



def check_two_positive(num1, num2, num3):
    positive_total = 0

    if num1 > 0:
        positive_total += 1

    if num2 > 0:
        positive_total += 1

    if num3 > 0:
        positive_total += 1

    return positive_total == 2

# Input your numbers here 

print(check_two_positive(1, -2, -3))  