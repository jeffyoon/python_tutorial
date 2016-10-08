# -*- coding: utf-8 -*-

def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

num_list = [1,2,3,4,5]

squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)

print(squares)
print(cubes)
print(quads)

def logger(msg):
    def log_message():
        print('Log: {0}'.format(msg))

    return log_message

log_hi = logger('Hi')
print(log_hi)
log_hi()

