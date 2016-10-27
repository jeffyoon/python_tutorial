# Object Types - Numbers, Strings, and None
Object Type        | Example literals/creation
------------------ | -------------------------
Numbers            | 1234, 3.1415, 3+4j, Decimal
Strings            | 'python', "Jupiter", b'a\x01c'
Lists              | [1,[2,'three'], 4]
Dictionaries       | {'Apple': 'iPhone', 'Google': 'Android'}
Tuples             | (1, 'php', 3, 'Y')
Files              | myFile = open('test', 'r')
Sets               | set('xyz'), {'x', 'y', 'z'}
Other core types   | Booleans, types, None
Program unit types | Functions, modules, classes

## What is an Object?
Everything in Python is an object, and eveything can have attributes and methods.
All functions have a built-in attribute **__doc__**, which returns the **docstring** defined in the function's source code.
For example, **sys** module is an object which has an attribute called **path** , and so forth.

What is an object?
Different programming languages define object in different ways.
In some, it means that all objects must have **attribute** and **methods**;
in others, it means that all objects are **subclassable**.
In Python, the definition is looser. Some objects have neither attribute or methods, but they could.
Not all objects are subclassable. But everything is an object in the sense that it can be assigned to a variable or passed an argument to a function.

You may have heard the term **first-class obejct** in other programming contexts. In Python, functions are first-class objects.
You can pass a function as an argument to another function.
Modules are first-class objects. You can pass an entire module as an argument to a function.
Classes are first-class objects, and individual instances of a class are also first-class objects.

This is important, so I'm going to repeat it in case you missed it the first few times: everything in Python is an object. Strings are objects. Lists are objects. Functions are objects. Classes are objects. Class instances are objects. Even modules are objects.

## Help
To get more information about object methods, we can always call the built-in **dir** function. It returns a list of all the attributes available for a given object.
Because methods are function attributes, they will show up in this list.
Assuming **S** is still the string, here are its attributes on Python 3.2:
```
>>> S = 'Picasso'
>>> dir(S)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__',
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'_formatter_field_name_split', '_formatter_parser', 'capitalize',
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
```

Here, the names with underscores in the list represent the implementation of the string object and are available to support customization.

In general, leading and trailing double underscores is the naming pattern Python uses for implementation details. The names without the underscores in the list are the callable methods on string objects.

The **dir** function simply gives the methods' names. To get the information about what they do, we can pass them to the **help** function:

```
>>> help(S.replace)
Help on built-in function replace:

replace(...)
    S.replace(old, new[, count]) -> str

    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

>>>
```

## NoneType object - None
**None** is a special constant in Python. It is a null value. None is not the same as **False**. None is not **0**. None is not **an empty string**. Comparing None to anything other than None will always return **False**.

None is the only null value. It has its own datatype (NoneType). We can assign None to any variable, but you can not create other NoneType objects. All variables whose value is None are equal to each other.

```
>>> type(None)

>>> None == 0
False
>>> None == ''
False
>>> None == False
False
>>> None == None
True
>>> a = None
>>> a == None
True
>>> b = None
>>> a == b
True
```

Another thing to note is when we use **None** in a **boolean context**:
```
>>> def None_in_a_boolean_context(None_Input):
    if None_Input:
        print("It is True")
    else:
        print("It is False")


>>> None_in_a_boolean_context(None)
It is False
>>> None_in_a_boolean_context(not None)
It is True
```



