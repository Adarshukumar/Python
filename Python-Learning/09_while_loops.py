"""Lesson 09 — while loops. Author: Adarsh."""
# while repeats as long as the condition is True
count = 1
while count <= 5:
    print("Count is", count)
    count += 1        # forgetting this line = infinite loop!

# Countdown
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print("Lift off!")

# Accumulator pattern — total
total = 0
number = 1
while number <= 100:
    total += number
print("Sum 1..100 =", total)     # 5050

# while True + break: the "ask until valid" pattern
while True:
    answer = input("Enter 'quit' to stop: ")
    if answer == "quit":
        print("Bye!")
        break
    print("You typed:", answer)

# Practice: print the Fibonacci numbers below 100 using a while loop.
