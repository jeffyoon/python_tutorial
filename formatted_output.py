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
# '%' : string modulo operator

print("Art: %5d, Price per Unit: %8.2f" % (453, 59.058))
#      ----    Format String      ----
#                                     % : String Modulo operator
#                                         - Tuple with values -
# Art  453, Price per Unit:   59.06
# The general syntax for a format placeholder is
#   %[flags][width][.precision]type
# (e.g.)  %6.2f   --->   ###.##  --> 6 (Total Width) , 2 ( . following width )
# 23.789 ==> #23.79 , 0.039 ==> ##0.04 , 199.8 ==> 199.80 , 23 ==> #23.00

# d : signed integer decimal. , i : signed integer decimal, o : unsigned octal , u : unsigned decimal
# x : unsigned hexadecimal (lowercase) , X : unsigned hexadecimal (uppercase) , e : floating point exponential (lowercase)
# E : floating point exponential (uppercase)

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






