"""
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""

# Using While Loop
n = int(input("input a number:"))
f = 1
i = 1

while i <= n:
    f = f * i;
    i = i + 1
print(f)

# Using For Loop
n = int(input("input a number:"))
f = 1

for i in range(1, n + 1):
    f = f * i
    i = i + 1
print(f)

# Using Lambda Function
n = int(input("input a number:"))


def fact(x): return 1 if x <= 1 else x * fact(x - 1)


print(fact(n))
