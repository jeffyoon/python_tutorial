# The easiest way, but not the most elagant one
q = 459
p = 0.098

print(q, p, p * q)
print(q, p, p * q, sep=",")
print(q, p, p * q, sep=":")

# Alternatively, we can construe out of the values a new string by using the string concatenation operator:
print(str(q) + " " + str(p) + " " + str(p * q))

# The second method is inferior to the first one in this example.

# The Old Way or the non-existing printf and sprintf
# '%' operator : string modulo operator

print("Art: %5d, Price per Unit: %8.2f" % (453, 59.058))
#      ----    Format String      ----
#                                     % : String Modulo operator
#                                         - Tuple with values -
# Output : Art  453, Price per Unit:   59.06

print('I am using %s %d.%d' % ('Python', 3, 2))
# Output : 'I am using Pyhon 3.2'

'''
Format specification
b : Binary format. Outputs the number in base 2.
c : Character.
d : Decimal integer. Outputs the number in base 10.
e, E : Exponent nation.
f, F : Fixed point.
g : General format.
n : Number.
o : Octal format.
s : String format.
x,X : Hex format. Outputs the number in base 16.
% : Percentage.
'''

# The general syntax for a format placeholder is
#   %[flags][width][.precision]type
# (e.g.)  %6.2f   --->   ###.##  --> 6 (Total Width) , 2 ( . following width )
# 23.789 ==> #23.79 , 0.039 ==> ##0.04 , 199.8 ==> 199.80 , 23 ==> #23.00

# d : signed integer decimal. , i : signed integer decimal, o : unsigned octal , u : unsigned decimal
# x : unsigned hexadecimal (lowercase) , X : unsigned hexadecimal (uppercase) , e : floating point exponential (lowercase)
# E : floating point exponential (uppercase)

n = 6789
a = "...%d...%-6d...%06d" % (n, n, n)
print(a)
# Output : '...6789...6789  ...006789'
# (-) : left justification and zero (0) fills. %-6d, %06d

m = 9.876543210
'%e | %E | %f | %g' % (m, m, m, m)
# Output : '9.876543e+00 | 9.876543E+00 | 9.876543 | 9.87654'

# Formatting dictionary strings
'''
Targets on the left can refer to the keys in a dictionary on the right so that they can fetch the
corresponding values. In the example below, the (m) and (w) in the format string refers to the keys
in the dictionary on the right abd fectch their corresponding values.
'''
'%(m)d %(w)s' % {'m': 101, 'w': 'Freeway'}
# Output : '101 Freeway'

'''
We can build a dictionary of values and substitue them all at once with a sing formatting expression
that uses key-based references. This technique can be used to generate text:
'''
greetings = '''
Hello %(name)s!
Merry Christmas.
I hope %(year)d will be a good year.
'''
replace = {'name': 'Jeff', 'year': 2017}
print(greeting % replace)

'''
* String formatting by method calls.
Unlike formatting using expression which is based on C's printf, string formatting using method call
is regared as more Python-specific.

* Template basics
This new string object's format method uses the subject string as a template and takes any number of
arguments that represent values to the substitued accroding to the template.
Within the subject string, curly braces designate substitution targets and arguments to be inserted
either by position such s {1} or keyward such as language.
'''
#By position
t = '{0}, {1}, {2}'
t.format('Dec', '29', '2016')
# --> 'Dec, 29, 2016'

#By keyword
t = '{Month}, {Day}, {Year}'
t.format(Month='Dec', Day='29', Year='2016')
# --> 'Dec, 29, 2016'

#Mixed
t = '{Year}, {Month}, {0}'
t.format('29', Year='2016', Month='Dec')
# --> '2016, Dec, 29'

# Arbitrary object type can be substitued from a temporary string
'{Month}, {Year}, {0}'.format('29', Month=['Nov', 'Dec'], Year='2016')
# --> "['Nov', 'Dec'], 2016, 29"


# The Pythonic Way : The string method "format"
# "Art: {0:5d}, Price per Unit: {1:8.2f}".format(453, 59.058)
#        0 : argument0 (453)     1 : argument1 (59.058)
print("Art: {0:5d}, Price per Unit: {1:8.2f}".format(453, 59.058))

# In the following example we demonstrate how keyword parameters can be used with the format method:
# "Art: {a:5d}, Price: {p:8.2f}".format(a=453, p=59.058)
print("Art: {a:5d}, Price: {p:8.2f}".format(a=453, p=59.058))

# It's possible to left or right justify data with the format method.
# To this end, we can precede the formatting with a "<" (left justify) or ">" (right justify).
# We demonstrate this with the following examples:
print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
