# if, elif, else Statements

# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for Statements
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)

for i in range(5):
    print(i)

# The given end point is never part of the generated sequence;
# range(5, 10)  --> 5 through 9  : [5:10)
# range(0, 10, 3)  --> 0, 3, 6, 9
# range(-10, -100, -30)  --> -10, -40, -70

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(range(10))   # print 'range(0, 10)'

print(list(range(5)))  # [0,1,2,3,4]

# break and continue Statements, and else Clauses on Loops.
# Loop statements may have an else clause;
#it is executed when the loop terminates through exhaustion of the list (with for) or
# when the condition becomes false (with while), but not when the loop is terminated by a break statement.
for n in range(2, 10):
    print(n, "n is 1st for loop")
    for x in range(2, n):
        print(x, "x is 2nd for loop")
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# pass Statements
# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl-C)

# creating minimal classes:
class MyEmptyClass:
    pass


def initlog(*args):
    pass    # Remember to implement this!

# Defining Functions
# """xxxxx""" is the function's document string or docstring
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

# print docstring
print(fib.__doc__)
print(fib(0))   #  Print None

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib(100)
print(fib2.__doc__)

# Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)








