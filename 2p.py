# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Introduction to Python 2
# ========================
# 
# Chang Y. Chung
# 
# Office of Population Research
# 
# 01/14/2014

# <markdowncell>

# Algorithms + Data Structures = Programs
# ---------------------------------------
# 
# Niklaus Wirth (1976)<cite data-cite="Wirth1976">[3]</cite>
# 
# ![wirth](files/graphics/wirth.png)
# 
# Python's built-in data structures include:
# 
# * Lists
# * Dictionaries
# * Tuples
#   
# We will also briefly talk about:
# 
# * Classes
# * Exception Handling

# <markdowncell>

# List
# ----
# 
# Ordered (indexed) collection of arbitrary objects.
# 
# Mutable -- may be changed in place.

# <markdowncell>

# List
# ----
# 
# Ordered collection of arbitrary objects.

# <codecell>

L = []                             # a new empty list
L = list()                         # ditto

L = [1, 2.5, "abc" , [56.7, 78.9]]
print len(L) 
print L[1] 
print L[3][0]

# <codecell>

for x in L:
    print x

# <codecell>

print "abc" in L, L.count("abc"), L.index("abc")

# <markdowncell>

# List
# ----
# 
# Mutable -- may be changed in place.

# <codecell>

L = []
L.append(5)
print L

# <codecell>

L[0] = 23
print L

# <codecell>

M = [87, 999]
L.extend(M)
print L

# <codecell>

del L[2]
print L

# <markdowncell>

# List
# ----
# 
# More examples.

# <codecell>

def squares(a_list): 
    s=[]
    for el in a_list:
        s.append(el ** 2) 
    return s
    
sq = squares([1, 2, 3, 4]) 
print sq, sum(sq)

# <markdowncell>

# Aliasing vs copying

# <codecell>

L = [1, 2, 3, 4]
M = L             # aliasing
L[0] = 87
print M

# <codecell>

L = [1, 2, 3, 4]
M = list(L)       # (shallow) copying. M = L[:] also works
L[0] = 87
print M

# <markdowncell>

# Quiz
# ----
# 
# Given a list,

# <codecell>

L = [1, 2, [3, 4], 5, "xyz"]

# <markdowncell>

# Evalute the following expressions:

# <codecell>

L[1] == 1

# <codecell>

len(L) == 5

# <codecell>

L[2] == 3, 4

# <codecell>

[3] in L

# <codecell>

L.index("xyz") == 4

# <codecell>

L[-1] == "xyz"

# <codecell>

L[-1][-1] == "z"

# <codecell>

any([1,2,3]) == True

# <codecell>

L[9] == None

# <codecell>

len([0,1,2,]) == 3

# <markdowncell>

# Quiz
# ----
# 
# Write a function that, given a list of integers, returns a _new_ list of odd numbers only. For instance, given the list, [0, 1, 2, 3, 4], this function should return a new list, [1, 3]. (Hint: Create a new empty list. Loop over the old one appending only odd numbers into the new one. Return the new one.)

# <codecell>

def only_odd(a_list):
    L = []
    for el in a_list:
        if el % 2 == 1:
            L.append(el)
    return L

# check
print only_odd([0, 1, 2, 3, 4])

# <markdowncell>

# Quiz (cont.)
# ------------
# 
# (tricky) Write a function similar to the previous one. This time, however, do not return a new list. Just modify the given list so that it has only the odd numbers. (Hint: del L[0] removes the first element of the list, L)

# <markdowncell>

# Here is an answer.

# <codecell>

def only_odd2(a_list):
    L = []                    # a temporary storage for odd numbers
    
    while len(a_list) > 0:    # loop over the given list, while not empty.
        el = a_list[0]        # get the first element. 
        if el % 2 == 1:       # save it in a local list, L, if an odd number.
            L.append(el)
        del a_list[0]         # remove the element from the input.
        
    a_list.extend(L)          # expand now empty list with the list with saved odd numbers
    
# check
L = [0, 1, 2, 3, 4]
only_odd2(L)
print L

# <markdowncell>

# Here is another. Looping last-to-first -- this way, we preserve the indices as they are, even we remove some elements.

# <codecell>

def only_odd3(a_list):
    length = len(a_list)
    i = 1
    while i <= length:
        j = length - i
        if a_list[j] % 2 == 0:
            del a_list[j]
        i += 1

# check
L = [0, 1, 2, 3, 4]
only_odd3(L)
print L

# <markdowncell>

# In practive, I'd just create a new list with a comprehension.

# <codecell>

L = [0, 1, 2, 3, 4]

M = [x for x in L if x % 2 == 1]
print M

# <markdowncell>

# Slice Index
# -----------
# 
# Applies to any sequence types, including list, str, tuple, ...
# 
# Has three (optional) parts separated by a colon (:), start : end : step, indicating start through but not past end, by step; Indices point in-between the elements.

# <rawcell>

#    +−−−+−−−+−−−+−−−+−−−+−−−+ 
#    | p | y | t | h | o | n | 
#    +−−−+−−−+−−−+−−−+−−−+−−−+
#    0   1   2   3   4   5   6
#   −6  −5  −4  −3  −2  −1

# <markdowncell>

# List slicing Examples:

# <codecell>

L = ['p', 'y', 't', 'h', 'o', 'n']
print L[:2]                         # first two

# <codecell>

print L[1:3]

# <codecell>

print L[0:5:2]

# <codecell>

print L[-1]                         # the last element

# <codecell>

print L[:]                          # a (shallow) copy

# <codecell>

print L[3:]

# <codecell>

print L[-2:]                        # last two

# <codecell>

print L[::-1]                       # reversed

# <markdowncell>

# Quiz
# ----
# 
# Suppose that you collect friendship network data among six children, each of whom we identify with a number: 0, 1, ..., 5. The data are represented as a list of lists, where each element list represents the element child's friends.

# <codecell>

L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]

# <markdowncell>

# For instance, the kid 0 friends with the kids 1 and 2, since

# <codecell>

L[0] == [1, 2]

# <markdowncell>

# Calculate the average number of friends the children have. (Hint: len() function returns the list size.)

# <codecell>

# data again
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]

total = 0.0             # make total a float type

for el in L:
    total += len(el)
    
avg = total / len(L)

# check
print avg

# <markdowncell>

# With a list comprehension, this can be as simple as:

# <codecell>

print 1.0 * sum([len(x) for x in L]) / len(L)

# <markdowncell>

# Quiz (cont.)
# ------------
# 
# Write a function to check if _all_ the friendship choices are reciprocated. It should take a list like previous one and return either True or False. (Hint: You may want to use a utility function below.)

# <codecell>

def mutual(a_list, ego, alter):
    return alter in a_list[ego] and ego in a_list[alter]

# <markdowncell>

# An answer:

# <codecell>

def all_reciprocated(a_list):
    for ego in range(len(L)):
        alters = L[ego]
        for alter in alters:
            if not mutual(a_list, ego, alter):
                return False
    return True

# check
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]
print all_reciprocated(L)

# <codecell>

# another check
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3, 4]]
print all_reciprocated(L)

# <markdowncell>

# List Comprehension
# ------------------
# 
# A concise way to create a list. An example:

# <codecell>

L = [x for x in range(5) if x % 2 == 1]
print L

# <markdowncell>

# An equivalent code using the for loop:

# <codecell>

L = []
for x in range(5):
    if x % 2 == 1:
        L.append(x)
print L

# <markdowncell>

# More examples:

# <codecell>

[x - 5 for x in range(6)]

# <codecell>

[abs(x) for x in [-2,-1,0,1]]

# <codecell>

[x for x in range(6) if x==x**2]

# <codecell>

[1 for x in [87, 999, "xyz"]]

# <codecell>

[x - y for x in range(2) for y in [7, 8]]

# <markdowncell>

# Dictionary
# ----------
# 
# A collection of key-value pairs.
# 
# Indexed by keys.
# 
# Mutable.
# 
# Also known as associative array, map, symbol table, ...
# 
# Usually implemented as a hash table.

# <markdowncell>

# Dictionary
# ----------
# 
# A collection of key-value pairs, indexed by keys.

# <codecell>

D={}                     # an empty dictionary. D=dict() also works

D["one"]=1
D["two"]=2
print D

# <codecell>

print D.keys()

# <codecell>

print "three" in D.keys()

# <codecell>

D = {"Apple": 116, "Big Mac": 550}

for key in ["Apple", "Orange", "Big Mac"]:
    if key in D:
        print "{0} has {1} calories".format(key, D[key])
    else:
        print "{0} is not found in the dictionary".format(key)

# <markdowncell>

# Dictionary
# ----------
# 
# More Dictionary examples.

# <codecell>

D = {"China": 1350, "India":1221, "US":317}

for key in D.keys():
    print "Pop of {0}: {1} mil".format(key, D[key])

# <codecell>

D = {[1,2]: 23}

# <codecell>

D = {2: [2, 3], 200: [3, 4], 95: [4, 5]}
print D[2]
print D[200]

# <markdowncell>

# Data Structure
# --------------
# 
# SAT has three subsections: Critical Reading, Mathematics, and Writing. A result of taking an SAT exam is three scores.

# <codecell>

# data
SAT = {"cr": 780, "m": 790, "w": 760}

# usage
print SAT["m"]

# <markdowncell>

# You can take SAT exams more than once.

# <codecell>

# data
SAT = [{"cr": 780, "m": 790, "w": 760},
       {"cr": 800, "m": 740, "w": 790}]

# usage
print SAT[0]

# <codecell>

print SAT[0]["cr"]

# <markdowncell>

# More Complicated Data Structure
# -------------------------------
# 
# Hypothetical SAT data for two people: Jane and Mary

# <codecell>

# data
SAT = {"Jane": {"lastname" : "Thompson",
                "test": [{"cr": 700, "m": 690, "w":710}] },
       "Mary": {"lastname" : "Smith",
                "test": [{"cr": 780, "m": 790, "w": 760},
                         {"cr": 800, "m": 740, "w": 790}] } }

# usage
print SAT["Jane"]

# <codecell>

print SAT["Jane"]["lastname"]

# <codecell>

print SAT["Jane"]["test"]

# <codecell>

print SAT["Jane"]["test"][0]

# <codecell>

print SAT["Jane"]["test"][0]["cr"]

# <codecell>

mary1 = SAT["Mary"]["test"][1]
print mary1["cr"]

# <markdowncell>

# Quiz
# ----
# 
# Make a dictionary of 2012 SAT percentile ranks for the scores from 660 to 700 and for all three subsections. The full table is available at [http://tinyurl.com/k38xve8](http://tinyurl.com/k38xve8).
# 
# Given this dictionary, say D, a lookup, D[660]["cr"] should be evaluated to 91.

# <markdowncell>

# An answer:

# <codecell>

D = {700: {"cr": 95, "m": 93, "w": 96}, 
     690: {"cr": 94, "m": 92, "w": 95}, 
     680: {"cr": 93, "m": 90, "w": 94}, 
     670: {"cr": 92, "m": 89, "w": 93}, 
     660: {"cr": 91, "m": 87, "w": 92}}

# check
print D[660]["cr"]

# <markdowncell>

# Quiz (cont.)
# ------------
# 
# Write a new dictionary DD such that we look up the subsection first and then the score. That is, DD["cr"][660] should be evaluated to 91. (Hint: Start with a dictionary below.)

# <codecell>

DD = {"cr": {}, "m": {}, "w": {}}

# <codecell>

for score in D:
    subjects = D[score]        # subjects itself is a dictionary
    for subject in subjects: 
        DD[subject][score] = subjects[subject]

# check        
print DD["cr"][660]    

# <markdowncell>

# Tuples
# ------
# 
# A sequence of values separated by commas.
# 
# Immutable.
# 
# Often automatically _unpacked_.

# <markdowncell>

# Tuples
# ------
# 
# A sequence of values separated by commas. Immutable.

# <codecell>

T = tuple()                     # empty tuple. T = () works also.
N = (1)                         # not a tuple
T = (1, 2, "abc")               # a tuple (1, 2, "abc")
print T[0]

# <codecell>

T[0] = 9                        # immutable

# <markdowncell>

# Often automatically unpacked.

# <codecell>

T = (2, 3)
a, b = T
print a, b

# <codecell>

a, b = b, a                     # swap
print a, b

# <codecell>

D = {"x": 23, "y": 46}
D.items()                       # returns a list of tuples (key,value)

# <codecell>

for k, v in D.items():
    print "%s ==> %d" % (k, v)

# <markdowncell>

# Class
# -----
# 
# Class defines a (user-defined) type, a grouping of some data (properties) and functions that work on the data (methods).
# 
# An object is an _instance_ of a type.
# 
# Examples:
# 
# * int is a type; 23 is an object.
# * str a type; "abc" an object.
# * "word document file" a type; "my_diary.docx" is an object.
# * We have been using objects.

# <markdowncell>

# Examples of Built-in Types
# --------------------------
# 
# str type has a bunch of methods.

# <codecell>

"abc".upper()

# <codecell>

"abc".find("c")

# <codecell>

"abc".split("b")

# <markdowncell>

# open() function returns a file object (representing an opened file).

# <codecell>

with open("code/test.txt", "w") as my_file:
    my_file.write("first line\n")
    my_file.write("second line\n")
    my_file.write("third line")
    
    print type(my_file)

# <codecell>

    print dir(my_file)              # properties and methods

# <codecell>

my_file.write("something")

# <markdowncell>

# Class
# -----
# 
# Let's create a bank account type.

# <codecell>

class BankAccount:
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount): 
        self.balance += amount
        
    def withdraw(self, amount): 
        self.balance -= amount

# <markdowncell>

# Usage examples.

# <codecell>

my_account = BankAccount(100)
my_account.withdraw(5)
print my_account.balance

# <codecell>

your_account = BankAccount()
your_account.deposit(100)
your_account.deposit(10)
print your_account.balance

# <markdowncell>

# Quiz
# ----
# 
# Implement a Person type (or class) which has three properties (first_name, last_name, and birth_year); and two methods: full_name() and age(). The age() method should take the current year as an argument. You may use the template below.

# <codecell>

class Person:
    
    def __init__(self, first_name, last_name, birth_year):
        pass
    
    def full_name(self):
        pass
    
    def age(self, current_year):
        pass

# <markdowncell>

# An answer.

# <codecell>

class Person:
    
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
# check
mr_park = Person("jae-sang", "Park", 1977)
print mr_park.full_name()

# <codecell>

print mr_park.age(2014)

# <markdowncell>

# Inheritance
# -----------
# 
# A subtype is more specialized basetype.

# <codecell>

import webbrowser

class CoolPerson(Person):
    
    def __init__(self, name, birth_year, video):
        Person.__init__(self, name, None, birth_year)
        self.video = video
        
    def full_name(self):
        return self.first_name
    
    def show_off(self):
        url = "http://www.youtube.com/watch?v={0}"
        webbrowser.open(url.format(self.video))
        
# check
psy = CoolPerson("PSY", 1977, "9bZkp7q19f0")
print psy.full_name()

# <codecell>

print psy.age(2012)

# <codecell>

# uncomment the line below and run (Shift+Enter) to see the style. 
# psy.show_off()

# <markdowncell>

# Exception Handling
# ------------------
# 
# An exception is raised when a (run-time) error occurs. By default, the script stops running immediately.

# <codecell>

L = [0, 1, 2, 3]
print L[5]

# <markdowncell>

# try: ... except: ... let us catch the exception and handle it.

# <codecell>

L = [0, 1, 2, 3]

try:
    print L[5]
    
except IndexError:
    print "no such element"
    
print "next"

# <markdowncell>

# Throwing Exception
# ------------------
# 
# We can raise (or throw) an exception as well.

# <codecell>

def fetch(a_list, index):
    if index >= len(a_list):
        raise IndexError("Uh, oh!")
    return a_list[index]

# check
print fetch(L, 5)

# <markdowncell>

# Script can keep going if you catch and handle the exception.

# <codecell>

L = [0, 1, 2, 3]

try:
    print fetch(L, 5)
    
except IndexError:
    print "an exception occurred"
    
print "next"

# <markdowncell>

# An Example

# <markdowncell>

# ulropen() in urllib2 module raises an exception when the web page is not found.

# <codecell>

import urllib2

L = ["http://google.com",
     "http://google.com/somethingfantastic",
     "http://yahoo.com"]

# we want to open each page in turn
for url in L:
    try:
        page = urllib2.urlopen(url)
        print page.getcode()
    
    except:
        print "failed to open: {0}".format(url)

# <markdowncell>

# A Data Structure Usage Example
# ------------------------------
# 
# STAN([http://mc-stan.org](http://mc-stan.org)) is a C++ library / language implementing Markov chain Monte Carlo sampling (NUTS, HMC).
# 
# STAN provides three interfaces (or API's): R, Python, and shell
# 
# This is an example of using the Python API, which is provided in a Python module, PyStan<cite cite-data="STANSite">[1]</cite>.
# 
# In order to run this, you need to install: Cython ([http://cython.org](http://cython.org)), NumPy([http://www.numpy.org](http://www.numpy.org)), and STAN itself.
# 
# From PyStan doc ([http://tinyurl.com/olap8sx](http://tinyurl.com/olap8sx), fiting the eight school model in Gelman et al.<cite cite-data="GelmanEtAl2003">[2, sec 5.5]</cite>

# <markdowncell>

# Data Structure Usage Example (cont.)
# ------------------------------------
# 
# Import PyStan module and put STAN code in a string.

# <codecell>

import pystan
import matplotlib

schools_code = """
data {
    int<lower=0> J; // number of schools
    real y[J]; // estimated treatment effects
    real<lower=0> sigma[J]; // s.e. of effect estimates
}
parameters {
    real mu;
    real<lower=0> tau;
    real eta[J];
}
transformed parameters {
    real theta[J];
    for (j in 1:J)
    theta[j] <- mu + tau * eta[j];
}
model {
    eta ~ normal(0, 1);
    y ~ normal(theta, sigma);
}
"""

# <markdowncell>

# Data Structure Usage Example (cont.)
# ------------------------------------
# 
# Cont.

# <codecell>

schools_dat = {'J': 8,
               'y': [28,  8, -3,  7, -1,  1, 18, 12],
               'sigma': [15, 10, 16, 11,  9, 11, 10, 18]}

# this will take some time to run!
fit = pystan.stan(model_code=schools_code, 
                  data=schools_dat, iter=1000, chains=4)

la = fit.extract(permuted=True)
mu = la['mu']
# do something with mu here

print str(fit)           # (nicely) print fit object

%matplotlib inline
fit.plot()               # requires matplotlib

# <markdowncell>

# Notice that:
# 
# * Input data are supplied in a dictionary
# * stan() function in the module runs the model.
# * The function returns a fit type object, which has several methods including extract() and plot().

# <markdowncell>

# Summary
# -------
# 
# List -- An ordered collection of objects. Mutable.
# 
# Dictionary -- A collection of key-value pairs. Mutable.
# 
# Tuple -- A sequence of values separated by commas. Immutable.
# 
# Class -- Defines a type, a grouping of properties and methods.
# 
# try: ... except: ...  -- Catch and handle exceptions.

# <markdowncell>

# References
# ----------
# 
# * Stan project team site. http://mc-stan.org/team.html.
# * Andrew Gelman, John B. Carlin, H. S. S. D. B. R. Bayesian Data Analysis, 2nd ed. Chapman & Hall/CRC Texts in Statistical Science. Chapman and Hall/CRC, July 2003.
# * Wirth, N. Algorithms + Data Structures = Programs, 1st ed. Prentice Hall Series in Automatic Computation. Prentice-Hall, February 1976.

# <codecell>


