def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def fibonacci(limit):
    nums = []
    current = 0
    next = 1
    while current < limit:
        current, next = next, current + next
        nums.append(current)
    return nums


def fibonacci_co(limit):
    current = 0
    next = 1
    while current < limit:
        current, next = next, current + next
        # Using a yield computes one element in a sequence at a time, instead of compiling it all into a list.
        # It temporarily suspends the function and returns the current value before computing the next value.
        # It is perfect for items that turn into sequences that doesn't need to be stored in memory.
        yield current


print("5!={:,}\n10!={:,}\n25!={:,}".format(  # {:,} prints out ints as comma separated ints.
    factorial(5),
    factorial(10),
    factorial(25)
))

for n in fibonacci_co(100):
    print(n, end=", ")
