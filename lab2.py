
# Task 1 

n = int(input("Please enter a positive integer greater than 9: "))

while n <= 9:
    n = int(input("Please enter a positive integer greater than 9: "))

current = n
steps = 0

print(current, end="")

while current >= 10:
    temp = current
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    current = digit_sum
    steps += 1
    print(" →", current, end="")

print()
print("Final value:", current)
print("Total steps:", steps)


print("\n-------------------------------\n")


# Task 2 


n = int(input("Please enter a number between 10 and 100: "))

while n < 10 or n > 100:
    print("Invalid input. Please enter a number between 10 and 100:", end=" ")
    n = int(input())

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n + 1):

    if i % 7 == 0:
        print(f"({i} is skipped)")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1

    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1

    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1

    else:
        print(i)

print("--- Summary ---")
print("Fizz count :", fizz_count)
print("Buzz count :", buzz_count)
print("FizzBuzz count:", fizzbuzz_count)


print("\n-------------------------------\n")



# Task 3


n = int(input("Please enter a number between 3 and 9: "))

while n < 3 or n > 9:
    n = int(input("Please enter a number between 3 and 9: "))

for i in range(1, 2 * n):

    if i <= n:
        k = i
    else:
        k = 2 * n - i

    for j in range(1, k + 1):
        print(j, end="")

    print()
