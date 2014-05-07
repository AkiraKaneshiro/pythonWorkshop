
# coding: utf-8

### Introduction to Python 1

# May, 2014
# 
# Chang Y. Chung

### Why Python?

# * Popular
# * Easy to lean and use
# * Open-source
# * General-purpose
# * Multi-paradigm
# * Hettinger, "What makes Python Awesome?" <cite data-cite="Hettinger2013">[2]</cite> [http:/tinyurl.com/mndd4er](http://tinyurl.com/mndd4er)

# * Did I mention _popular_?

# Running Python REPL
# -------------------
# 
# For those who are using UNIX-like systems, including the Ubuntu image running on a Virtual Box.
# 
# Type "python" at the terminal shell prompt.
# 
# ![](files/graphics/vmrepl.png)

### Running a Python Script File (.py)

# Type "python" followed by the script file name.
# 
# ![](files/graphics/vmscript.png)

### Running Python REPL on Windows

# For those who are using Windows system with Python (and IDLE) installed.
# 
# Run the IDLE application.
# 
# ![](files/graphics/winrepl.png)

### Running a Python Script File (.py) on Windows

# File > New (or Open) brings up a script window.
# 
# Run > Run Module (Output will show in IDLE shell).
# 
# ![](files/graphics/winscript.png)

### Using IPython Notebook in a Web Browser

# ![](files/graphics/ipynb.png)

### Quiz

# * Print out a "Hello" in your environment.

# In[ ]:

print "hello"


# * Print out "Hello" 20 times.

# In[ ]:

# here is one way
print "Hello " * 20


### Conceptual Hierarchy by Mark Lutz<cite data-cite="Lutz2013">[3]</cite>

# * Programs are composed of _modules_.
# * Modules contain *statements*.
# * Statements contain *expressions*.
# * Expressions create and process *objects*.

### Script File (.py)

# * A script file is a module.
# * A script is a sequence of statements, delimited by a newline (or the end of line character).
# * Python executes one statement at a time, from the top of a script file to the bottom.
# * Execution happens in *namespaces* (modules, classes, functions all have their own).

### Executable Python Script File

# On a Unix-like system, we can change the mode of the script file and make it executable:

# <pre>
# $ chmod +x hellp.py
# $ ./hello.py
# </pre>

# Just add the first line with a hashbang(#!):

# In[ ]:

#!/usr/bin/python

# say hello to the world
def main():
    print "Hello, World!"

if __name__ == "__main__":
    main()


### Comments

# Comments start with a hash (#) and end with a newline.

# In[ ]:


# this whole line is a comment

# add 10 integers.
total = 0

for i in range(10):  # 0, 1, 2, ..., 9
    total += i       # total = total + i
    
print "total =", total


### Variables

# * Variables are created when first assigned a value.

# In[ ]:

my_var = 3
answer_to_everything = 42

# also works are:
x = y = 0
a, b, c = 1, 2, 3


# * Variable names start with a letter or an underscore and can have letters, underscores, or digits.
# 
# * Variable names are case-sensitive.

### Assignment Semantics According to David Godger<cite data-cite="Godger2008">[1]</cite>

# Variables in many _other languages_ are a container that stores a value.

# <pre>
# int a = 1;
# </pre>

# ![](files/graphics/a1box.png)

# In Python, an assignment creates an object, and labels it with the variable.

# In[ ]:

a = 1


# ![](files/graphics/a1tag.png)

# If you assign another value to a, then the variable labels the new value (2).

# In[ ]:

a = 2


# ![](files/graphics/1.png)
# ![](files/graphics/a2tag.png)

# This is what happens if you assign a to a new variable b:

# In[ ]:

b = a


# ![](files/graphics/1.png)
# ![](files/graphics/ab2tag.png)

### Integers

# In[ ]:

x = 0
age = 20
size_of_household = 5

print type(age)


# In[ ]:

# can handle arbitrarily large numbers
huge = 10 ** 100 + 1
huge


### Floating-point Numbers

# In[ ]:

g = 0.1
f = 6.67384


# It is the dot (.) that makes it a float.

# In[ ]:

velocity = 1.
print velocity


# In[ ]:

type(velocity)


### Most of the arithmetic operators behave as expected

# In[ ]:

a = 10
b = 20
print a - (b **2) + 23


# In[ ]:

x = 2.0
print x / 0.1


### Watch out for integer divisions. In Python 2, it _truncates down_ to an integer.

# In[ ]:

print 10 / 3    # 3.33... (in Python 3)


# In[ ]:

print -10 / 3   # -3.33... (in Python 3)


# A solution: use floating point numbers

# In[ ]:

print 10.0 / 3.0


### Quiz

# * What is the remainder of 5 divided by 2?

# In[ ]:

dividend = 5
divisor = 2

quotient = dividend / divisor
remainder = dividend - (quotient * divisor)

print remainder


# * What is the remainder of 2837465 divided by 2834?

# In[ ]:

print 2837465 % 2834


### String Literals

# * A string is a sequence of characters.
# * Either double(`"`) or single(`'`) quotes for creating string literals.

# In[ ]:

name = "Changarilla Dingdong"
file_name = 'workshop.tex'


# * Triple-quoted strings can span multiple lines.

# In[ ]:

starwars = """
A long time ago is a galaxy far, far away...

It is a period of civil war. Rebel
spaceships, striking from a hidden
base, have won their first victory
...

What is the last character of this string?
"""
last_char = starwars[-1]
print ord(last_char), ord("\n")


### Working with strings

# * Strings are immutable.

# In[ ]:

s = "abcde"
s[0] = "x"


# * We can always create a new string instead.

# In[ ]:

t = "x" + s[1:]
print t


# * Many functions and methods are available.

# In[ ]:

s = "abcde"
print s + s   # concatenation


# In[ ]:

print len(s)


# * Index is 0-based. `find` returns -1 if not found.

# In[ ]:

print s.find("c")


### String Manipulation

# A few more string methods.

# In[ ]:

s = "abcde"
print s.upper(), "XYZ".lower()


# In[ ]:

print "     xxx  yy  ".strip()


# In[ ]:

print "a,bb,ccc".split(",")


### What are *methods* anyway?

# * Functions which are a member of a type (or class).

# * int, str, Word Document are types (or classes).

# ![](files/graphics/methods.png)

# * 2, "abcde", diary.docx" are an _instance_ (or _object_) of the respective type.

# * Types have members: properties (data) and methods (functions).

### Two ways to Format

# * `format()` method

# In[ ]:

print "The answer is {0}".format(21)


# In[ ]:

print "The real answer is {0:6.4f}".format(21.2345678)


# * formatting operator

# In[ ]:

print "The answer is %d" % 21


# In[ ]:

print "The real answer is %6.4f" % 21.2345678


### Raw Strings

# Within a string literal, escape sequences start with a backslash.

# In[ ]:

a_string = 'It\'s a great day\nto learn \\Python\\. \n 1\t 2\t 3'
print a_string


# A _raw_ string literal starts with the prefix r. In a raw string, the backslash is not special. It is great for writing reg ex patterns.

# In[ ]:

import re

p = re.compile(r"\d\d\d-\d\d\d\d")
m = p.match("123-4567")
if m is not None:
    print m.group()


### Unicode Strings

# You can create Unicode strings using the u prefix and slash-u escape sequences. Write them with: \u followed by a hexadecimal value, xxxx.

# In[ ]:

a_string = u"Euro \u20AC"
print a_string, len(a_string)


# Unicode?

# * Unicode strings are sequences of _code points_.
# * Code points are numbers, each representing a "character" e.g., U+00612 is "Latin small letter a".
# * Unicode text strings are _encoded_ into bytes. UTF-8 is one of many Unicode encodings, using one to four bytes to store a Unicode "character".
# * Once you have Unicode strings in Python, all the string functions and properties work as expected.

### Best Practices According to Thomas Wouters<cite data-cite="Wouters2012">[5]</cite>

# * Never mix Unicode and bytecode (i.e., ordinary) strings.
# * Decode bytecode strings on input.
# * Encode unicode strings on output.
# * Try automatic conversion (`codecs.open()`)
# * Pay attention to exceptions, `UnicodeDecodeError` and `UnicodeEncodeError`

### A Unicode example:

# In[ ]:

ustr = u"Euro \u20AC"   # Euro symbol
print ustr


# Python's default encoding codec is 'ascii'.

# In[ ]:

ustr.encode()


# Encoding to UTF-8 works fine. This takes 8 bytes: 5 one-byte's and 1 three-byte.

# In[ ]:

utf_8 = ustr.encode("UTF-8")


# Now we want to decode to ascii, ignoring non-ascii characters.

# In[ ]:

print utf_8.decode("ascii", "ignore")


### Quiz

# Say hello to Abe, Betty, and Carl -- write three print statements.

# In[ ]:

template = "Hello, {0}!"
print template.format("Abe")
print template.format("Betty")
print template.format("Carl")


### None

# Is a place-holder, like NULL in other languages.

# In[ ]:

x = None


# None is s a universal object, i.e, there is only one None.

# In[ ]:

print None is None


# * None is evaluated as False.

# In[ ]:

x = None
if x:
    print "this will never print"


# None, however, is distinct from others which are False.

# In[ ]:

print None is 0, None is False, None is []


### Core Data Types

# * Basic code data types: int, float, and str
# * "Python is dynamically, but _strongly_ typed."

# In[ ]:

n = 1.0
print n + "99"


# * Use `int()` or `float()` to go from str to numeric

# In[ ]:

print n + float("99")


# * str() returns the string representation of the given object.

# In[ ]:

n = 1.0
print str(n) + "99"


### Operators

# * Python supports following types of operators:

#    * Arithmetic (`+  -  +  /  %  **  //`)
#    * Comparison (`==  !=  >  <  >=  <=`)
#    * Assignment (`=  +=  -=  *=  /=  %=  **=  //=`)
#    * Logical (`and  or  not`)
#    * Bitwise (`&  |  ^  ~  <<  >>`)
#    * Membership (`in  not in`)
#    * Identity (`is  is not`)

### A Few Surprises

# * Power operator binds more tightly than unary operators on the left.

# In[ ]:

a = -2 ** 2
print a


# * solution: parenthesize the base

# In[ ]:

print (-2)**2


# * Comparisons can be chained

# In[ ]:

x = 1
y = 3
z = 3

# y is evaluated only once below
x < y <= z

# but it is equivalent to:
x < y and y <= z


# * Logical operators (and, or) short-circuit evaluation and return an _operand_.

# In[ ]:

print 3 or 2


### Quiz

# * Demographic and Health Surveys (DHS) Century Month Code (CMC)<cite data-cite="MEASUREDHSPlus">[4,p5]</cite> provides and easy way working with year and month.
# * The CMC is an integer representing a month, taking the value of 1 in January 1900, 2 in February 1900, ..., 13 in January 1901, etc. The CMC in February 2011 is 1333.
# * What is the CMC for this month, i.e., January, 2014?

# In[ ]:

# An answer:
year = 2014
month = 1
print "CMC", (year - 1900) * 12 + month


# * What is the month (and year) of CMC 1000?

### Quiz

# * According to U.S. National Debt Clock, the current outstanding public debt, as of a day last month, was a big number:

# In[ ]:

debt = 17234623718339.96


# * Count how many times the degit 3 appears in the number. (Hint: create a string variable and use the count() method of the string type.)

# In[ ]:

# An answer:
sdebt = "17234623718339.96"
print sdebt.count("3")


# * (tricky) It feels rather silly to rewrite the value as a string. Can you think of a way to _convert_ the number into a string?

# In[ ]:

# this may or may not work. 
s1 = str(debt)
print s1.count("3")


# In[ ]:

# this should not fail.
s2 = "{0:20.2f}".format(debt)
print s2.count("3")


### Flow Control

# * Conditional Execution (`if`)
# * Iteration
#   * `while` loop
#   * `for` loop

### If Statement

# * If statement is used for conditional execution.

# In[ ]:

x = 4
if x > 0:
    print "x is positive"
else:
    print "x is zero or negative"


# * Only one suite (block of statements) under a True conditional expression is executed.

# In[ ]:

me = "rock"
wins = 0

you = "scissors"

if you == "paper":
    print "You win!"
    
elif you == "scissors":
    print "I win!"
    wins += 1
    
else:
    print "draw"


### Compound Statements

# * If, while, and for are _compound_ statements, which have one or more _clauses_. A clause, in turn, consists of a _header_ that ends with a colon and a _suite_.
# * A suite, a block of statements, is identified by _indentation_.

# In[ ]:

a = 1                      # 1 
if a > 0:                  # 2
    desc = "a is positive" # 3
    print a, desc          # 4
                           # 5
print "done"               # 6


# * Lines 3 and 4 being "in-dented" signals a suite (or a block).
# * Line 5, a blank line, is ignore.
# * Line 6 being "de-dented" signals the end of the block of lines 3 and 4.

# The following raises an `IndentationError`.

# In[ ]:

print "another"         # 1
                        # 2
    if a > 0:           # 3
desc = "a is positive"  # 4


# Below is syntactically OK, just not so stylish.

# In[ ]:

if a > 0:               # 1
        desc = "a > 0"  # 2
        print desc      # 3
else:                   # 4
    print "a <= 0"      # 5


### More on indentation

# * The amount of indentation does not matter (as long as the same within a level). Four spaces (per level) and no tabs are the convention.
# * Use editor's python mode, which prevents/converts TAB to (four) spaces.
# * Why indentation? A good answer at: [http://tinyurl.com/kxv9vts](http://tinyurl.com/kxv9vts).
# * For an empty suite, use pass statement, which does nothing.

### While

# * Repeats a block of statements as long as the condition remains True.

# In[ ]:

total = 0
n = 0
while n < 5:
    print n, total
    n += 1
    total += n


# * `break` terminates a loop immediately.
# * `continue` skips the remainder of the block and goes back to the test condition at the top.

### For

# * `for` is used to iterate over a sequence.

# In[ ]:

days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]

for day in days:
    if day == "Friday":
        print "I am outta here."
        break
    print "Happy" + " " + day + "!"


# * Another example:

# In[ ]:

numbers = range(5)
print numbers


# In[ ]:

for n in numbers:
    print n,
    if n % 2 == 0:
        print "is even"
    else:
        print "is odd"


### File I/O

# * The built-in function, `open()`, returns a file type object, unless there is an error opening the file.

# In[ ]:

in_file = open("code/yourfile.txt", "r")
out_file = open("code/myfile.txt", "w")


# * Once we get the file type object, then use its methods to read from, write to, or close a file.

# In[ ]:

content = in_file.read()

out_file.write("hello?\n")

in_file.close()
out_file.close()


### Reading a file one line at a time

# * with ensures that the file is closed when done.

# In[ ]:

with open("code/lorem.txt", "r") as f:
    for line in f:
        print line


# * Creating a file and writing three lines.

# In[ ]:

with open("code/small.txt", "w") as f:
    f.write("first\n")
    f.write("second\n")
    f.write("third")    


# * Read line inclues the newline character.

# In[ ]:

with open("code/small.txt", "r") as f:
    for line in f:
        print line


### Function

# * Defined with `def` and called by name followed by `()`.

# In[ ]:

def the_answer():
    return 42

print the_answer()


# * Argument(s) can be passed.

# In[ ]:

def shout(what):
    print what.upper() + "!"
    
shout("hello")


# * If the function returns nothing, then it returns None.

# In[ ]:

def shout(what):
    print what.upper() + "!"
    
r = shout("hi")
print r


### CMC again

# In[ ]:

def cmc(year, month):
    ''' returns DHS Century Month Code '''   # doc string
    
    if year < 1900 or year > 2099:
        print "year out of range"
        return

    if month < 1 or month > 12:
        print "month out of range"
        return

    value = (year - 1900) * 12 + month 
    return value

print cmc(2014, 1) 
print cmc(2014, 15)


### Local and Global Variables

# Within your function:
# 
# * A new variable is _local_, and independent of the global variable with the same name, if any.

# In[ ]:

x = 1     # global

def my_func():
    x = 2 # local
    
my_func()
print x


# * Both local and global variables can be read.
# * Global variables can be written to once _declared_ so.

# In[ ]:

x = 1

def my_func():
    global x
    x = 2
    
my_func()
print x


### Quiz

# * Wirte a function that returns Body Mass Index (BMI) of an adult given weight in kilograms and height in meters. (Hint: BMI = weight(kg) / (height(m) squared). For instance, if a person is 70kg and 1.80m, then BMI is about 21.6)

# In[ ]:

def bmi(kg, m):
    return float(kg) / (m ** 2)

print bmi(70, 1.80)


# * Re-write the bmi function so that it accepts height in feet and inches, and the weight in pounds. (Hint. Make foot, inch, and pound arguments. Convert them into local variables, kg and m, before calculating bmi to return.)

# In[ ]:

def bmi2(pound, foot, inch):
    kg = 0.453592 * pound
    m = 0.0254 * (12 * foot + inch)
    return bmi(kg, m)

print bmi2(154.324, 5, 10.8661)


### Importing a module

# * `import` command reads in a module, runs it (top-to-bottom) to create the module object.
# * Via the module object, you get access to its variables, functions, classes, ...
# * We've already seen an example of importing a standard regular expression module:

# In[ ]:

import re

p = re.compile(r"\d\d\d-\d\d\d\d")
m = p.match("123-4567")
if m is not None:
    print m.group()


### Another Example

# There are many standard modules that come already installed, and be ready to be imported.

# In[ ]:

import math

s = math.sqrt(4.0)
print "square root of 4.0 is {0:.2f}".format(s)


# * You can selectively import as well.

# In[ ]:

from math import sqrt

print sqrt(9.0)


# * You can import your own Python script file (.py) the same way.

# In[ ]:

import sys

sys.path.append('code/')
import hello

hello.main()


### Quiz

# Write a function such that, given a BMI value, returns the BMI category as a string. Recall the categories are:
# * Underweight: less than 18.5
# * Normal weight: 18.5 upto but not including 25
# * Overweight: 25 upto but not including 30
# * Obesity: 30 or greater
# For instance, the function should return a string "Normal weight", when it is called with an argument of, say 20. (Hint: use conditional statements, i.e., if ... elif ...)

# In[ ]:

def BMI_category(bmi):
    cat = ""
    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal weight"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obesity"
    return cat

# check
print BMI_category(20)


# * Print out a BMI table showing several lines of a pair: a BMI value and its category. BMI value may start at 15 and go up by 3 up to 36. (Hint: use a loop.)

# In[ ]:

def BMI_table():
    print "bmi", "category"
    print "-" * 17
    bmi = 15
    while bmi <= 36:
        print "", bmi, BMI_category(bmi)
        bmi += 3
        
# check
BMI_table()


### Quiz

# * Create a comma-separated values (.csv) file of the BMI table.

# In[ ]:

import csv

with open("code/test.csv", "wb") as f:
    my_writer = csv.writer(f)
    bmi = 15
    while bmi < 36:
        cat = BMI_category(bmi)
        my_writer.writerow([bmi, cat])
        bmi += 3

with open("code/test.csv", "r") as f:
    for line in f:
        print line,


### Summary

# * Using Python interactively or by running a script.
# * Comments.
# * Variables and assignment semantics.
# * Core data types (int, float, str, None)
# * Operators.
# * Conditionals and looping.
# * Defining and calling functions.
# * Basic File I/O.
# * Importing a module.

### References

# * Godger, D. Code like a pythonista: Idiomatic python. http://tinyurl.com/2cv9kg.
# * Hettinger, R. What makes Python Awesome? http://tinyurl.com/mndd4er.
# * Lutz, M. Learning Python, fifth ed. O’Reilly Media, Sebastopol, CA, 2013.
# * MEASURE DHS Plus. Description of the Dempgraphic and Health Surveys Individual Recode Data File, version 1.0 ed., March 2008.
# * Wouters, T. Advanced python: (or understanding python) google tech talks. feb 21, 2007. http://www.youtube.com/watch?v=uOzdG3lwcB4.
