# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Introduction to Python 1
# ========================
# 
# Chang Y. Chung
# 
# Office of Population Research
# 
# 01/14/2014

# <markdowncell>

# Why Python?
# -----------
# 
# * Popular
# 
# * Easy to learn and use
# 
# * Open-source
# 
# * General-Purpose
# 
# * Multi-paradigm
# 
# * Hettinger, "What makes Python Awesome?" <cite data-cite="Hettinger2013">[2]</cite> [http:/tinyurl.com/mndd4er](http://tinyurl.com/mndd4er)
# 
# * Did I mention _popular_?

# <markdowncell>

# Running Python REPL
# -------------------
# 
# For those who are using UNIX-like systems, including the Ubuntu image running on a Virtual Box.
# 
# Type "python" at the terminal shell prompt.
# 
# ![vm repl](files/graphics/vmrepl.png)

# <markdowncell>

# Running a Python Script File (.py)
# ----------------------------------
# 
# Type "python" followed by the script file name.
# 
# ![vm script](files/graphics/vmscript.png)

# <markdowncell>

# Running Python REPL on Windows
# ------------------------------
# 
# For those who are using Windows system with Python (and IDLE) installed.
# 
# Run the IDLE application.
# 
# ![win repl](files/graphics/winrepl.png)

# <markdowncell>

# Running a Python Script File (.py) on Windows
# ---------------------------------------------
# 
# File > New (or Open) brings up a script window.
# 
# Run > Run Module (Output will show in IDLE shell).
# 
# ![win script](files/graphics/winscript.png)

# <markdowncell>

# Conceptual Hierarchy by Mark Lutz<cite data-cite="Lutz2013">[3]</cite>
# ---------------------------------
# 
# * Programs are composed of _modules_.
# * Modules contain _statements_.
# * Statements contain expressions.
# * Expressions create and process objects.

# <markdowncell>

# Script File (.py)
# -----------------
# 
# * A script file is a module.
# * A script is a sequence of statements, delimited by a newline (or the end of line character).
# * Python executes one statement at a time, from the top of a script file to the bottom.
# * Execution happens in namespaces (modules, classes, functions all have their own).
# * Everything is runtime (even def, class, and import).

# <markdowncell>

# Executable Python Script File
# -----------------------------
# 
# On a Unix-like system, we can change the mode of the script file and make it executable:

# <rawcell>

# $chmod +x hellp.py
# $./hello.py

# <markdowncell>

# Just add the first line with a hashbang(#!):

# <rawcell>

# #!/usr/bin/python
# 
# # say hello to the world
# def main():
#     print "Hello, World!"
# 
# if __name__ == "__main__":
#     main()

# <markdowncell>

# Comments
# --------
# 
# Comments start with a hash (#) and end with a newline.

# <codecell>

# this whole line is a comment

# add 10 integers.
total = 0
for i in range(10):  # i goes 0, 1, 2, ..., 9
    total += i       # shortcut for total = total + i
    
print "total=", total

# <markdowncell>

# Variables
# ---------
# 
# Variables are created when first assigned a value.

# <codecell>

my_var = 3
answer_to_everything = 42

# also works are:
x = y = 0
a, b, c = 1, 2, 3

# <markdowncell>

# Variable names start with a letter or an underscore and can have letters, underscores, or digits.
# 
# Variable names are case-sensitive.

# <markdowncell>

# Assignment Semantics According to David Godger<cite data-cite="Godger2008">[1]</cite>
# ----------------------------------------------
# 
# Variables in many _other languages_ are a container that store a value.

# <rawcell>

# int a = 1;

# <markdowncell>

# ![a1box](files/graphics/a1box.png)

# <markdowncell>

# In Python, an assignment creates an object, and labels it with the variable.

# <codecell>

a = 1

# <markdowncell>

# ![a1tag](files/graphics/a1tag.png)

# <markdowncell>

# If you assign another value to a, then the variable labels the new value (2).

# <codecell>

a = 2

# <markdowncell>

# ![1tag](files/graphics/1.png)
# ![a2tag](files/graphics/a2tag.png)

# <markdowncell>

# This is what happens if you assign a to a new variable b:

# <codecell>

b = a

# <markdowncell>

# ![1](files/graphics/1.png)
# ![ab2tag](files/graphics/ab2tag.png)

# <markdowncell>

# Numbers
# -------
# 
# Integers

# <codecell>

x = 0
age = 20
size_of_household = 5

print type(age)

# <codecell>

# can handle arbitrarily large numbers
huge = 10 ** 100 + 1

# <markdowncell>

# Floating-point Numbers

# <codecell>

g = 0.1
f = 6.67384

velocity = 1.   # it is the dot(.) that makes it a float
print velocity

# <codecell>

type(velocity)

# <markdowncell>

# Numeric Expressions
# -------------------
# 
# Most of the arithmetic operators behave as expected.

# <codecell>

a = 10
b = 20
print a - (b **2) + 23

# <codecell>

x = 2.0
print x / 0.1

# <markdowncell>

# Watch out for integer divisions. In Python 2, it _truncates down_ to an integer.

# <codecell>

print 10 / 3    # 3.3333333333333335 (in Python 3)

# <codecell>

print -10 / 3   # -3.3333333333333335 (in Python 3)

# <codecell>

# a solution: use floating point numbers
print 10.0 / 3.0

# <markdowncell>

# String Literals
# ---------------
# 
# A string is a sequence of characters.

# <codecell>

# either double(") or single(') quotes for creating string literals.
name = "Changarilla Dingdong"
file_name = 'workshop.tex'

# triple-quoted string
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

# <markdowncell>

# Working with strings
# --------------------
# 
# Strings are immutable.

# <codecell>

s = "abcde"
s[0] = "x"  # trying to change the first character to "x"

# <codecell>

t = "x" + s[1:]
print t

# <markdowncell>

# Many functions and methods are available.

# <codecell>

s = "abcde"
print s + s   # concatenation

# <codecell>

print len(s)

# <codecell>

print s.find("c")    # index is 0-based. returns -1 if not found

# <markdowncell>

# String Manipulation
# -------------------
# 
# A few more string methods.

# <codecell>

s = "abcde"
print s.upper(), "XYZ".lower()

# <codecell>

print "     xxx  yy  ".strip()

# <codecell>

print "a,bb,ccc".split(",")

# <markdowncell>

# What are "Methods"?
# 
# * Functions which are a member of a type (or class).
# * int, str, Word Document are types (or classes).
# * 2, "abcde", diary.docx" are an _instance_ (or _object_) of the respective type.
# * Types have members: properties (data) and methods (functions).

# <markdowncell>

# ![methods](files/graphics/methods.png)

# <markdowncell>

# Two ways to Format
# ------------------
# 
# format() method.

# <codecell>

print "The answer is {0}".format(21)

# <codecell>

print "The real answer is {0:6.4f}".format(21.2345678)

# <markdowncell>

# Formatting operator.

# <codecell>

print "The answer is %d" % 21

# <codecell>

print "The real answer is %6.4f" % 21.2345678

# <markdowncell>

# Raw Strings
# -----------
# 
# Within a string literal, escape sequences start with a backslash.

# <codecell>

a_string = 'It\'s a great day\nto learn \\Python\\. \n 1\t 2\t 3'
print a_string

# <markdowncell>

# A _raw_ string literal starts with the prefix r. In a raw string, the backslash is not special.

# <codecell>

import re

# raw strings are great for writing regular expression patterns.
p = re.compile(r"\d\d\d-\d\d\d\d")
m = p.match("123-4567")
if m is not None:
    print m.group()

# <markdowncell>

# Unicode Strings
# ---------------
# 
# You can create Unicode strings using the u prefix and slash-u escape sequences.

# <codecell>

a_string = u"Euro \u20AC"   # \u followed by 16-bit hex value xxxx
print a_string, len(a_string)

# <markdowncell>

# * Unicode strings are sequences of _code points_.
# * Code points are numbers, each representing a "character" e.g., U+00612 is "Latin small letter a".
# * Unicode text strings are _encoded_ into bytes. UTF-8 is one of many Unicode encodings, using one to four bytes to store a Unicode "character".
# * Once you have Unicode strings in Python, all the string functions and properties work as expected.

# <markdowncell>

# Best Practices According to Thomas Wouters<cite data-cite="Wouters2012">[5]</cite>
# ------------------------------------------
# 
# * Never mix unicode and bytecode (i.e., ordinary) strings.
# * Decode bytecode strings on input.
# * Encode unicode strings on output.
# * Try automatic conversion (codecs.open())
# * Pay attention to exceptions, UnicodeDecodeError
# 
# An example:

# <codecell>

ustr = u"Euro \u20AC"   # Euro symbol

# Python's default encoding codec is 'ascii'
ustr.encode()

# <codecell>

utf_8 = ustr.encode("UTF-8") # encoding to UTF-8 works fine
# this takes 8 bytes. five one-byte's and one three-byte.

# now we want to decode to ascii, ignoring non-ascii characters
print utf_8.decode("ascii", "ignore")

# <markdowncell>

# None
# ----
# 
# Is a place-holder, like NULL in other languages.

# <codecell>

x = None

# <markdowncell>

# None is s a universal object, i.e, there is only one None.

# <codecell>

print None is None

# <markdowncell>

# None is evaluated as False.

# <codecell>

x = None
if x:
    print "this will never print"

# <markdowncell>

# None, however, is distinct from others which are False.

# <codecell>

print None is 0, None is False, None is []

# <markdowncell>

# Core Data Types
# ---------------
# 
# * Basic code data types: int, float, and str
# * "Python is dynamically, but _strongly_ typed."

# <codecell>

n = 1.0
print n + "99"

# <markdowncell>

# * Use int() or float() to go from str to numeric.

# <codecell>

print n + float("99")

# <markdowncell>

# * str() returns the string representation of the given object.

# <codecell>

n = 1.0
print str(n) + "99"

# <markdowncell>

# Operators
# ---------
# 
# * Python supports following types of operators:

# <rawcell>

#    * Arithmetic (+ - + / % ** //)
#    * Comparison (== != > < >= <=)
#    * Assignment (= += -= *= /= %= **= //=)
#    * Logical (and or not)
#    * Bitwise (& | ^ ~ << >>)
#    * Membership (in  not in)
#    * Identity (is  is not)

# <markdowncell>

# A Few Surprises
# ---------------
# 
# * Power operator binds more tightly than unary operators on the left.

# <codecell>

a = -2 ** 2
print a

# <codecell>

# solution: parenthesize the base
print (-2)**2

# <markdowncell>

# * Comparisons can be chained.

# <codecell>

x = 1
y = 3
z = 3

x < y <= z    # y is evaluated only once here
# is equivalent to
x < y and y <= z

# <markdowncell>

# * Logical operators (and, or) short-circuit evaluation and return an _operand_.

# <codecell>

print 3 or 2

# <markdowncell>

# Quiz
# ----
# 
# * Demographic and Health Surveys (DHS) Century Month Code (CMC)<cite data-cite="MEASUREDHSPlus">[4,p5]</cite> provides and easy way working with year and month.
# * The CMC is an integer representing a month, taking the value of 1 in January 1900, 2 in February 1900, ..., 13 in January 1901, etc. The CMC in February 2011 is 1333.
# * What is the CMC for this month, i.e., January, 2014?

# <codecell>

# An answer:
year = 2014
month = 1
print "CMC", (year - 1900) * 12 + month

# <markdowncell>

# * What is the month (and year) of CMC 1000?

# <markdowncell>

# Quiz
# ----
# 
# * According to U.S. National Debt Clock, the current outstanding public debt, as of a day last month, was a big number:

# <codecell>

debt = 17234623718339.96

# <markdowncell>

# * Count how many times the degit 3 appears in the number. (Hint: create a string variable and use the count() method of the string type.)

# <codecell>

# An answer:
sdebt = "17234623718339.96"
print sdebt.count("3")

# <markdowncell>

# * (tricky) It feels rather silly to rewrite the value as a string. Can you think of a way to _convert_ the number into a string?

# <codecell>

# this may or may not work. 
s1 = str(debt)
print s1.count("3")

# <codecell>

# this should not fail.
s2 = "{0:20.2f}".format(debt)
print s2.count("3")

# <markdowncell>

# Flow Control
# ------------
# 
# * Conditional Execution (if)
# * Iteration
#   * while loop
#   * for loop

# <markdowncell>

# If Statement
# ------------
# 
# * If statement is used for conditional execution.

# <codecell>

x = 4
if x > 0:
    print "x is positive"
else:
    print "x is zero or negative"

# <markdowncell>

# * Only one suite (block of statements) under a True conditional expression is executed.

# <codecell>

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

# <markdowncell>

# Compound Statements
# -------------------
# 
# * If, while, and for are _compound_ statements, which have one or more _clauses_. A clause, in turn, consists of a _header_ that ends with a colon and a _suite_.
# * A suite, a block of statements, is identified by _indentation_.

# <markdowncell>

# Compound Statements
# -------------------
# 
# * The amount of indentation does not matter (as long as the same within a level). Four spaces (per level) and no tabs are the convention.
# * Use editor's python mode, which prevents/converts TAB to (four) spaces.
# * Why indentation? A good answer at: [http://tinyurl.com/kxv9vts](http://tinyurl.com/kxv9vts).
# * For an empty suite, use pass statement, which does nothing.

# <markdowncell>

# While
# -----
# 
# * Repeats a block of statements as long as the condition remains True.

# <codecell>

total = 0
n = 0
while n < 10:
    print n, total
    n += 1
    total += n

# <markdowncell>

# * break terminates a loop immediately.
# * continue skips the remainder of the block and goes back to the test condition at the top.

# <markdowncell>

# For
# ---
# 
# * for is used to iterate over a sequence.

# <codecell>

days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]

for day in days:
    if day == "Friday":
        print "I am outta here."
        break
    print "Happy" + " " + day + "!"

# <markdowncell>

# For
# ---
# 
# * Another example:

# <codecell>

numbers = range(5)
print numbers

# <codecell>

for n in numbers:
    print n,
    if n % 2 == 0:
        print "is even"
    else:
        print "is odd"

# <codecell>

a = 1
if a > 0:
    desc = "a is positive"           # these two lines form a suite
    print a, desc                    #
                                     # (blank line ignored)
print "done"                         # This line being started "dedented"
                                     # signals the end of the block.
    
    if a > 0:                        # indentation error
desc = "a is positive"               # indentation error

if a > 0:                            # OK
            desc = "a is positive"   # OK
            print a, desc            # OK
else:                                # OK
        print a                      # OK

# <markdowncell>

# File I/O
# --------
# 
# * The built-in function, open(), returns a file type object, unless there is an error opening the file.

# <codecell>

in_file = open("code/yourfile.txt", "r")
out_file = open("code/myfile.txt", "w")

# <markdowncell>

# * Once we get the file type object, then use its methods.

# <codecell>

# read all the contents from the input file
content = in_file.read()

# write out a line to the output file
out_file.write("hello?\n")

# close it when done
in_file.close()
out_file.close()

# <markdowncell>

# Reading a file one line at a time
# ---------------------------------
# 
# * with ensures that the file is closed when done.

# <codecell>

with open("code/lorem.txt", "r") as f:
    for line in f:
        print line

# <markdowncell>

# * Another example.

# <codecell>

# creating a file and writing three lines.
with open("code/small.txt", "w") as f:
    f.write("first\n")
    f.write("second\n")
    f.write("third")
    
with open("code/small.txt", "r") as f:
    for line in f:
        print line       # line includes the newline char

# <markdowncell>

# Defining and Calling a Function
# -------------------------------
# 
# * Defined with def and called by name followed by ().

# <codecell>

def the_answer():
    return 42

print the_answer()

# <markdowncell>

# * Argument(s) can be passed.

# <codecell>

def shout(what):
    print what.upper() + "!"
    
shout("hello")

# <markdowncell>

# * If the function returns nothing, then it returns None.

# <codecell>

r = shout("hi")
print r

# <markdowncell>

# Another Example
# ---------------
# 
# * CMC again

# <codecell>

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

# <markdowncell>

# Local and Global Variables
# --------------------------
# 
# Within your function:
# 
# * A new variable is _local_, and independent of the global variable with the same name, if any.

# <codecell>

x = 1                   # global (or module)

def my_func():
    x = 2               # local
    
my_func()
print x

# <markdowncell>

# * Both local and global variables can be read.
# * Global variables can be written to once _declared_ so.

# <codecell>

x = 1

def my_func():
    global x
    x = 2                # global
    
my_func()
print x

# <markdowncell>

# Quiz
# ----
# 
# Wirte a function that returns Body Mass Index (BMI) of an adult given weight in kilograms and height in meters. (Hint: BMI = weight(kg) / (height(m) squared). For instance, if a person is 70kg and 1.80m, then BMI is about 21.6)

# <codecell>

# An answer:
def bmi(kg, m):
    return float(kg) / (m ** 2)

# check
print bmi(70, 1.80)

# <markdowncell>

# Re-write the bmi function so that it accepts height in feet and inches, and the weight in pounds. (Hint. Make foot, inch, and pound arguments. Convert them into local variables, kg and m, before calculating bmi to return.)

# <codecell>

def bmi2(pound, foot, inch):
    kg = 0.453592 * pound
    m = 0.0254 * (12 * foot + inch)
    return bmi(kg, m)

# check
print bmi2(154.324, 5, 10.8661)

# <markdowncell>

# Importing a module
# ------------------
# 
# import command reads in a module, runs it (top-to-bottom) to create the module object.
# 
# Via the module object, you get access to its variables, functions, classes, ...
# 
# We've already seen an example of importing a standard regular expression module:

# <codecell>

import re

# compile() is a function defined within the imported re module.

p = re.compile(r"\d\d\d-\d\d\d\d")
m = p.match("123-4567")
if m is not None:
    print m.group()

# <markdowncell>

# Another Example
# ---------------
# 
# There are many standard modules that come already installed, and be ready to be imported.

# <codecell>

import math

s = math.sqrt(4.0)
print "4.0 squared is {0:.2f}".format(s)

# <markdowncell>

# * You can selectively import as well.

# <codecell>

from math import sqrt # import sqrt alone

print sqrt(9.0)     # no "math."

# <markdowncell>

# * You can import your own Python script file (.py) the same way. The default import path includes the current working directory and its sub-direcgtories.

# <codecell>

import sys
sys.path.append('code/')  # just to make sure that import searches ./code sub directory

import hello              # suppose that hello.py defines a main() function

hello.main()

# <markdowncell>

# Quiz
# ----
# 
# Write a function such that, given a BMI value, returns the BMI category as a string. Recall the categories are:
# 
# * Underweight: less than 18.5
# * Normal weight: 18.5 upto but not including 25
# * Overweight: 25 upto but not including 30
# * Obesity: 30 or greater
# 
# For instance, the function should return a string "Normal weight", when it is called with an argument of, say 20. (Hint: use conditional statements, i.e., if ... elif ...)

# <codecell>

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

# <markdowncell>

# Print out a BMI table showing several lines of a pair: a BMI value and its category. BMI value may start at 15 and go up by 3 up to 36. (Hint: use a loop.)

# <codecell>

def BMI_table():
    print "bmi", "category"
    print "-" * 17
    bmi = 15
    while bmi <= 36:
        print "", bmi, BMI_category(bmi)
        bmi += 3
        
# check
BMI_table()

# <markdowncell>

# Quiz (cont.)
# ------------
# 
# * Create a comma-separated values (.csv) file of the BMI table.

# <codecell>

import csv

with open("code/test.csv", "wb") as f:
    my_writer = csv.writer(f)
    bmi = 15
    while bmi < 36:
        cat = BMI_category(bmi)
        my_writer.writerow([bmi, cat])
        bmi += 3
        
# check
with open("code/test.csv", "r") as f:
    for line in f:
        print line,

# <markdowncell>

# Summary
# -------
# 
# * Using Python interactively or by running a script.
# * Comments.
# * Variables and assignment semantics.
# * Core data types (int, float, str, None)
# * Operators.
# * Conditionals and looping.
# * Defining and calling functions.
# * Basic File I/O.
# * Importing a module.

# <markdowncell>

# References
# ----------
# 
# * Godger, D. Code like a pythonista: Idiomatic python. http://tinyurl.com/2cv9kg.
# * Hettinger, R. What makes Python Awesome? http://tinyurl.com/mndd4er.
# * Lutz, M. Learning Python, fifth ed. O’Reilly Media, Sebastopol, CA, 2013.
# * MEASURE DHS Plus. Description of the Dempgraphic and Health Surveys Individual Recode Data File, version 1.0 ed., March 2008.
# * Wouters, T. Advanced python: (or understanding python) google tech talks. feb 21, 2007. http://www.youtube.com/watch?v=uOzdG3lwcB4.

# <codecell>


