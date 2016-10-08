# This is the first comment

# Strings
# Besides numbers, Python can also manipulates string, which can be expressed in several ways.
# They can be enclosed in signle quotes ('...') or dobule quotes ("...") with the same result.

s1 = 'spam eggs'    # single quotes
s2 = 'doesn\'t'     # use \' to escape the string quote...
s3 = "doesn't"      # ... or use double quotes instead
s4 = '"Yes," he said.'
s5 = "\"Yes,\" he said."

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

s6 = 'First line.\nSecond line.'    # \n means new line
print(s6)   # with print(), \n produces a new line

# You can use raw strings by adding an r before the first quote.
print('C:\some\name')   # here \n means newline!
print(r'C:\some\name')  # note the r before the quote.

# String literals can span multiple lines.
# One way is using the triple-quoutes : """...""" or '''...'''
print("""\
      Usage: thing [OPTIONS]
        -h              Display this usage message
        -H hostname     Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *
# 3 times 'un', following by 'ium'
s7 = 3 * 'un' + 'ium'
print(s7)

# Tow or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
# This only works with two literals though, not with variable ot expression.
s8 = 'Py' 'thon'
print(s8)

# If you want to concatenate variables or a variable and a literal, use +
prefix = 'Py'
s9 = prefix + 'thon'
print(s9)

# This feature is particularly useful when you want to break long strings
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# String can be indexed (subscripted), with the first character having index 0.
word = "Python"
print(word[0])      # index 0 is first character
print(word[-1])     # index -1 is last character
print(word[-2])     # index -2 is second-last character
print(word[-6])     # first character in this case.

# Note that since -0 is the same as 0, negative indices start from -1.
s10 = word[0:2]     # characters from position 0 (included) to 2 (excluded) [0:2) == 'Py'
s11 = word[2:5]     # characters from position 2 (included) to 5 (excluded) [2:5) == 'tho'

print(s10)
print(s11)

# Note that the start is always included and the end always excluded.
# This make sure that s[:i] + s[i:] is always equal to s:
s12 = word[:2] + word[2:]
print(s12)

# Slice indices have useful defaults; an omitted first index defaults to zero,
# an omitted second index defaults to the size of the string being sliced.

s13 = word[:2]      # character from the beginning to position 2 (excluded) [0:2) == 'Py'
s14 = word[4:]      # characters from position 4 (included) to the end [4:end] == 'on'
s15 = word[-2:]     # characters from second-last (included) to the end  == 'on'


# One way to remember how slices work is to think of the indices as pointing between characters,
# withe the left edge of the first character numbered 0.
# Then the right edge of the last character of a string of n characters has index n, for example
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6 -5  -4  -3  -2  -1

# Python strings cannot be changed — they are immutable.
# Therefore, assigning to an indexed position in the string results in an error:
# word[0] = 'J'       # Error
# word[2:] = 'py'     # Error

# str class
# str object
print(str('aaaa!'))

# bytes-like object
print(str(b'aaaa!'))

# Strings also support two styles of string formatting
# one providing a large degree of flexibility and customization : str.format()
# The other based on C printf style formatting that handles a narrower range of types.

# Formatting String Syntax
# Format strings contain “replacement fields” surrounded by curly braces {}.
# Anything that is not contained in braces is considered literal text, which is copied unchanged to the output.
# If you need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.
# https://docs.python.org/3/library/string.html#formatstrings

# The positional argument specifiers can be omitted, so '{} {}' is equivalent to '{0} {1}'.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# "First, thou shalt count to {0}"  # References first positional argument
# "Bring me a {}"                   # Implicitly references the first positional argument
# "From {} to {}"                   # Same as "From {0} to {1}"
# "My quest is {name}"              # References keyword argument 'name'
# "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
# "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Three conversion flags are currently supported: '!s' which calls str() on the value,
# '!r' which calls repr() and '!a' which calls ascii().

# "Harold's a clever {0!s}"        # Calls str() on the argument first
# "Bring out the holy {name!r}"    # Calls repr() on the argument first
# "More {!a}"                      # Calls ascii() on the argument first

# Accessing arguments by position:
s16 = '{0}, {1}, {2}'.format('a', 'b', 'c')
s17 = '{}, {}, {}'.format('a', 'b', 'c')        # ver3.1+ only
s18 = '{2}, {1}, {0}'.format('a', 'b', 'c')
s19 = '{2}, {1}, {0}'.format(*'abc')            # unpacking argument sequence
s20 = '{0}, {1}, {0}'.format('abra', 'cad')     # arguments' indices can be repeated

# Accessing arguments by name:
s21 = 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
s22 = 'Coordinates: {latitude}, {longitude}'.format(**coord)    # ** kwargs (keyward arguments)

# Accessing arguments’ attributes:
c = 3-5j
s23 = ('The complex number {0} is formed from the real part {0.real} '
 'and the imaginary part {0.imag}.').format(c)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

print(str(Point(4, 2)))


# Accessing arguments’ items:
coord = (3, 5)
s24 = 'X: {0[0]}; Y:{0[1]}'.format(coord)


# printf-style string format
# String objects have one unique built-in operation: the % operator (modulo).
# This is also known as the string formatting or interpolation operator.
# Given format % values (where format is a string), % conversion specifications in format are replaced with zero or more elements of values.

# conversion specifications in format
# A conversion specifier contains two or more characters and has the following components, which must occur in this order:
# 1. The '%' character, which marks the start of the specifier.
# 2. Mapping key (optional), consisting of a parenthesised sequence of characters (for example, (somename)).
# 3. Conversion flags (optional), which affect the result of some conversion types.
# 4. Minimum field width (optional). If specified as an '*' (asterisk), the actual width is read from the next element
#    of the tuple in values, and the object to convert comes after the minimum field width and optional precision.
# 5. Precision (optional), given as a '.' (dot) followed by the precision. If specified as '*' (an asterisk),
#    the actual precision is read from the next element of the tuple in values, and the value to convert comes after
#    the precision.
# 6. Length modifier (optional).
# 7. Conversion type.

print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
#      %(language->mapping key)s->(converion type)
#                       %(number->mapping key)0(conversion flag)3(minimum field with)d(convserion type)
#                                                  % (string formatting operator)
#                                                    {'key': 'value'} --> Tupple

print(str("aaaa").capitalize())     # 'Aaaa'
print(str('aaaa').center(10, '*'))  # '***aaaa***'
print(str('aaaa').center(11, '*'))  # '****aaaa***'
print(str('aaaa').center(3, '*'))   # 'aaaa'
print(str('aaa').count('a'))        # 3
print(str('aaa').count('aaa'))      # 1
print(str('My name is Jeff Yoon').count('o'))  # 2











