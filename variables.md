#Python Variables

###Python Keywords
There is no need to learn them by heart.

You can get the list of Python keywords in the interactive shell by using help.

You type in help() in the interactive, but please don't forget the parenthesis:

```
>>> help()

Welcome to Python 3.4's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>
```

What you see now is the help prompt, which allows you to query help on lots of things, especially on "keywords" as well:

```
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not
class               from                or
continue            global              pass

help>
```


###String, Unicode and Python

```
>>> s = 'I am a string enclosed in single quotes.'
>>> s2 = "I am another string, but I am enclosed in double quotes"
>>> s3 = 'It doesn\'t matter!'
>>> s3 = "It doesn't matter!"
>>> txt = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
>>> print(txt)
He said: "It doesn't matter, if you enclose a string in single or double quotes!"
>>>
```

A string in Python consists of a series or sequence of characters - letters, numbers, and special characters.

Strings can be subscripted or indexed. Similar to C, the first character of a string has the index 0.

![Position in String](http://www.python-course.eu/images/positive_and_negative_indices_of_strings.png)

```
>>> s = "Hello World"
>>> s[0]
'H'
>>> s[5]
' '
```

The last character of a string can be accessed like this:

```
>>> s[len(s)-1]
'd'
```

Yet, there is an easier way in Python.
The last character can be accessed with -1, the second to last with -2 and so on:

```
>>> s[-1]
'd'
>>> s[-2]
'l'
```

###Byte Strings
Python 3.0 uses the concepts of text and (binary) data instead of Unicode strings and 8-bit strings.
Every string or text in Python 3 is Unicode, but encoded Unicode is represented as binary data.
The type used to hold text is str, the type used to hold data is bytes.
It's not possible to mix text and data in Python 3; it will raise TypeError.
While a string object holds a sequence of characters (in Unicode), a bytes object holds a sequence of bytes, out of the range 0 .. 255, representing the ASCII values.
Defining bytes objects and casting them into strings:

```
>>> x = b"Hallo"
>>> t = str(x)
>>> u = t.encode("UTF-8")
```
