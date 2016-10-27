# List which can be written as a list of comma-separated values (items) between square brackets.

squares = [1,4,9,16,25]
print(squares)

# Here are the many list types.
# List can has any object.
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'long']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]


# Like strings (and all other built-in sequence type), lists can be indexed and sliced:

print(squares[0])       # indexing returns the item --> 1
print(squares[-1])      # indexing returns the last item --> 25
print(squares[-3:])     # slicing returns a new list --> [9,16,25], index : [-3, Last]
print(squares[2:4])     # slicing returns a new list --> [9, 16] , index : [2,4)
print(squares[0:2])     # slicing returns a new list --> [1, 4], index : [0,2)
print(squares[:2])      # slicing returns a new list --> [1, 4], index : [0,2)
print(squares[2:])      # slicing returns a new list --> [9,16,25], index : [2, Last]


# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64
print(cubes)

# You can also add new items at the end of the list, by using the append() method.
cubes.append(216)  # add the cubes of 6
cubes.append(7 ** 3)  # and the cubes of 7
print(cubes)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)  # ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list.
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3, 4, 5]
x = [a, n]
print(x)
print(x[0])   # print(a)
print(x[1])   # print(n)
print(x[0][0])  # a
print(x[0][1])  # b
print(x[1][3])  # 4

# List operator
# List Add (+)
a = [1,2,3]
b = [4,5,6]
print(a + b)    #[1,2,3,4,5,6,]

# List repeat (*)
a = [1,2,3]
print(a * 3)    #[1,2,3,1,2,3,1,2,3]

# Mutable vs Immutable objects in Python
'''
Common immutable type:
1. numbers : int(), float(), complex()
2. immutable sequences : str(), tuple(), frozoneset(), byte()

Common mutable type (almost eveything else):
1. mutable sequences : list(), bytearray()
2. set type : set()
3. mapping type : dict()
4. classes, class instances
5. etc.
'''

# List is a mutable object.
a = [1, 2, 3]
a[2] = 4
print(a)    # [1,2,4]

a[1:2]      # [2]
a[1:2] = ['a', 'b', 'c']
print(a)    # [1, 'a', 'b', 'c', 4]

# Note : There are different results if you run following expression.
a = [1, 2, 3]
a[1] = ['a', 'b', 'c']
print(a)    # [1, ['a', 'b', 'c'], 4]
# a[1:2] = ['a', 'b', 'c']
# print(a) --> [1, 'a', 'b', 'c', 4]

# Remove the element of List by using []
a = [1, 'a', 'b', 'c', 4]
a[1:3] = []
print(a)    # [1, 'c', 4]

# Remove the element of List by del function.
a = [1, 'c', 4]
del a[1]
print(a)    # [1, 4]

# del object.



