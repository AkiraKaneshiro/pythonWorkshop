
# coding: utf-8

## Introduction to Python 2

# May, 2014
# 
# Chang Y. Chung

### Algorithms + Data Structures = Programs

# Niklaus Wirth (1976)<cite data-cite="Wirth1976">[3]</cite>
# 
# ![](files/graphics/wirth.png)

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

### List

# * Ordered (indexed) collection of arbitrary objects.
# * Mutable -- may be changed in place.

# * Ordered collection of arbitrary objects.

# In[ ]:

L = []     # an empty list
L = list() # this works too

L = [1, 2.5, "abc" , [56.7, 78.9]]
print len(L) 
print L[1] 
print L[3][0]


# * Iterating over list elements.

# In[ ]:

L = [1, 2.5, "abc" , [56.7, 78.9]]
for x in L:
    print x


# * List comes equipped with lots of methods.

# In[ ]:

print "abc" in L
print L.count("abc")
print L.index("abc")


# * List is mutable -- may be changed in place.

# In[ ]:

L = []
L.append(5)
print L


# In[ ]:

L[0] = 23
print L


# In[ ]:

L = [23]
M = [87, 999]
L.extend(M)
print L


# In[ ]:

del L[2]
print L


# Let's define a function that accepts a list as an argument.

# In[ ]:

def squares(a_list): 
    s=[]
    for el in a_list:
        s.append(el ** 2) 
    return s
    
sq = squares([1, 2, 3, 4]) 
print sq, sum(sq)


# Aliasing vs. copying

# In[ ]:

L = [1, 2, 3, 4]
M = L       # aliasing
L[0] = 87
print M


# In[ ]:

L = [1, 2, 3, 4]
M = list(L) # (shallow) copying
L[0] = 87
print M


### Quiz

# In[ ]:

L = [1, 2, [3, 4], 5, "xyz"]


# Evalute the following expressions:

# In[ ]:

L[1] == 1


# In[ ]:

len(L) == 5


# In[ ]:

L[2] == 3, 4


# In[ ]:

[3] in L


# In[ ]:

L.index("xyz") == 4


### Quiz (Cont.)

# In[ ]:

L = [1, 2, [3, 4], 5, "xyz"]


# Evalute the following expressions:

# In[ ]:

L[-1] == "xyz"


# In[ ]:

L[-1][-1] == "z"


# In[ ]:

any([1,2,3]) == True


# In[ ]:

L[9] == None


# In[ ]:

len([0,1,2,]) == 3


### Quiz

# Write a function that, given a list of integers, returns a _new_ list of odd numbers only. For instance, given the list, [0, 1, 2, 3, 4], this function should return a new list, [1, 3]. (Hint: Create a new empty list. Loop over the old one appending only odd numbers into the new one. Return the new one.)

# In[ ]:

def only_odd(a_list):
    L = []
    for el in a_list:
        if el % 2 == 1:
            L.append(el)
    return L

# check
print only_odd([0, 1, 2, 3, 4])


### Quiz

# (tricky) Write a function similar to the previous one. This time, however, do not return a new list. Just modify the given list so that it has only the odd numbers. (Hint: del L[0] removes the first element of the list, L)

# Here is an answer.

# In[ ]:

def only_odd2(a_list):
    L = []               
    
    while len(a_list) > 0:
        el = a_list[0]     
        if el % 2 == 1:   
            L.append(el)
        del a_list[0]    
        
    a_list.extend(L) 
    
# check
L = [0, 1, 2, 3, 4]
only_odd2(L)
print L


# Here is another answer. Looping last-to-first element -- this way, we preserve the indices as they are, even we remove some elements.

# In[ ]:

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


# In practive, I'd just create a new list with a comprehension.

# In[ ]:

L = [0, 1, 2, 3, 4]

M = [x for x in L if x % 2 == 1]
print M


### Slice Index

# * Applies to any sequence types, including list, str, tuple, ...
# 
# * Has three (optional) parts separated by a colon (:), start : end : step, indicating start through but not past end, by step; Indices point in-between the elements.

# <pre>
#    +−−−+−−−+−−−+−−−+−−−+−−−+ 
#    | p | y | t | h | o | n |
#    +−−−+−−−+−−−+−−−+−−−+−−−+
#    0   1   2   3   4   5   6
#   −6  −5  −4  −3  −2  −1
# </pre>

# List slicing Examples:

# In[ ]:

L = ['p', 'y', 't', 'h', 'o', 'n']


# In[ ]:

print L[:2] # first two


# In[ ]:

print L[1:3]


# In[ ]:

print L[0:5:2]


# In[ ]:

print L[-1] # the last element


# In[ ]:

L = ['p', 'y', 't', 'h', 'o', 'n']


# In[ ]:

print L[:]  # a (shallow) copy


# In[ ]:

print L[3:]


# In[ ]:

print L[-2:] # last two


# In[ ]:

print L[::-1] # reversed


### Quiz

# Suppose that you collect friendship network data among six children, each of whom we identify with a number: 0, 1, ..., 5. The data are represented as a list of lists, where each element list represents the element child's friends.

# In[ ]:

L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]


# For instance, the kid 0 friends with the kids 1 and 2, since

# In[ ]:

L[0] == [1, 2]


# Calculate the average number of friends the children have. (Hint: len() function returns the list size.)

# An answer:

# In[ ]:

# data again
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]

total = 0.0 
for el in L:
    total += len(el)
    
avg = total / len(L)

# check
print avg


# With a list comprehension, this can be as simple as:

# In[ ]:

print 1.0 * sum([len(x) for x in L]) / len(L)


### Quiz (cont.)

# Write a function to check if _all_ the friendship choices are reciprocated. It should take a list like previous one and return either True or False. (Hint: You may want to use a utility function below.)

# In[ ]:

def mutual(a_list, ego, alter):
    return alter in a_list[ego] and ego in a_list[alter]


# In[ ]:

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


# In[ ]:

# another check
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3, 4]]
print all_reciprocated(L)


### List Comprehension

# A concise way to create a list. An example:

# In[ ]:

L = [x for x in range(5) if x % 2 == 1]
print L


# An equivalent code using the for loop:

# In[ ]:

L = []
for x in range(5):
    if x % 2 == 1:
        L.append(x)
print L


# More list comprehension examples:

# In[ ]:

[x - 5 for x in range(6)]


# In[ ]:

[abs(x) for x in [-2,-1,0,1]]


# In[ ]:

[x for x in range(6) if x==x**2]


# In[ ]:

[1 for x in [87, 999, "xyz"]]


# In[ ]:

[x - y for x in range(2) for y in [7, 8]]


### Dictionary

# * A collection of key-value pairs.
# * Indexed by keys.
# * Mutable.
# * Also known as associative array, map, symbol table, ...
# * Usually implemented as a hash table.

# * A collection of key-value pairs, indexed by keys.

# In[ ]:

D = {} # an empty dict
D = dict() # also works

D["one"]=1
D["two"]=2
print D


# In[ ]:

print D.keys()


# In[ ]:

print "three" in D.keys()


# In[ ]:

D = {"Apple": 116, "Big Mac": 550}

for key in ["Apple", "Orange", "Big Mac"]:
    if key in D:
        print "{0} has {1} calories".format(key, D[key])
    else:
        print "{0} is not found in the dictionary".format(key)


# More Dictionary examples.

# In[ ]:

D = {"China": 1350, "India":1221, "US":317}

for key in D.keys():
    print "Pop of {0}: {1} mil".format(key, D[key])


# * Mutables cannot be keys.

# In[ ]:

D = {[1,2]: 23}


# * Values can be almost of any type.

# In[ ]:

D = {2: [2, 3], 200: [3, 4], 95: [4, 5]}
print D[2]
print D[200]


### Data Structure

# SAT has three subsections: Critical Reading, Mathematics, and Writing. A result of taking an SAT exam is three scores.

# In[ ]:

# data
SAT = {"cr": 780, "m": 790, "w": 760}


# In[ ]:

# usage
print SAT["m"]


# You can take SAT exams more than once.

# In[ ]:

# data
SAT = [{"cr": 780, "m": 790, "w": 760},
       {"cr": 800, "m": 740, "w": 790}]


# In[ ]:

# usage
print SAT[0]


# In[ ]:

print SAT[0]["cr"]


### More Complicated Data Structure

# In[ ]:

SAT = {"Jane": {"lastname" : "Thompson",
                "test": [{"cr": 700, "m": 690, "w":710}] },
       "Mary": {"lastname" : "Smith",
                "test": [{"cr": 780, "m": 790, "w": 760},
                         {"cr": 800, "m": 740, "w": 790}] } }


# In[ ]:

print SAT["Jane"]


# In[ ]:

print SAT["Jane"]["lastname"]


# In[ ]:

print SAT["Jane"]["test"]


# In[ ]:

SAT = {"Jane": {"lastname" : "Thompson",
                "test": [{"cr": 700, "m": 690, "w":710}] },
       "Mary": {"lastname" : "Smith",
                "test": [{"cr": 780, "m": 790, "w": 760},
                         {"cr": 800, "m": 740, "w": 790}] } }


# In[ ]:

print SAT["Jane"]["test"]


# In[ ]:

print SAT["Jane"]["test"][0]


# In[ ]:

print SAT["Jane"]["test"][0]["cr"]


# In[ ]:

mary1 = SAT["Mary"]["test"][1]
print mary1["cr"]


### Quiz

# * Make a dictionary of 2012 SAT percentile ranks for the scores from 660 to 700 and for all three subsections. The full table is available at [http://tinyurl.com/k38xve8](http://tinyurl.com/k38xve8).
# 
# * Given this dictionary, say D, a lookup, D[660]["cr"] should be evaluated to 91.

# In[ ]:

D = {700: {"cr": 95, "m": 93, "w": 96}, 
     690: {"cr": 94, "m": 92, "w": 95}, 
     680: {"cr": 93, "m": 90, "w": 94}, 
     670: {"cr": 92, "m": 89, "w": 93}, 
     660: {"cr": 91, "m": 87, "w": 92}}

# check
print D[660]["cr"]


### Quiz (cont.)

# Write a new dictionary DD such that we look up the subsection first and then the score. That is, DD["cr"][660] should be evaluated to 91. (Hint: Start with a dictionary below.)

# In[ ]:

DD = {"cr": {}, "m": {}, "w": {}}


# In[ ]:

for score in D:
    subjects = D[score]
    for subject in subjects: 
        DD[subject][score] = subjects[subject]

# check        
print DD["cr"][660]    


### Tuples

# * A sequence of values separated by commas.
# * Immutable.
# * Often automatically _unpacked_.

# * A sequence of values separated by commas. Immutable.

# In[ ]:

T = tuple()
T = () # also works

N = (1) # not a tuple
T = (1, 2, "abc") # a tuple
print T[0]


# In[ ]:

T[0] = 9 # immutable


# * Often automatically unpacked.

# In[ ]:

T = (2, 3)
a, b = T
print a, b


# In[ ]:

a, b = b, a # swap
print a, b


# In[ ]:

D = {"x": 23, "y": 46}
D.items() # returns a list


# In[ ]:

for k, v in D.items():
    print "%s ==> %d" % (k, v)


### Class

# * Class defines a (user-defined) type, a grouping of some data (properties) and functions that work on the data (methods).
# 
# * An object is an _instance_ of a type.

# Examples:

#   - int is a type; 23 is an object.
#   - str a type; "abc" an object.
#   - "word document file" a type; "my_diary.docx" is an object.
#   - We have been using objects.

### Examples of Built-in Types

# `str` type has a bunch of methods.

# In[ ]:

"abc".upper()


# In[ ]:

"abc".find("c")


# In[ ]:

"abc".split("b")


# * `open()` function returns a `file` object (representing an opened file).

# In[ ]:

with open("code/test.txt", "w") as my_file:
    my_file.write("first line\n")
    my_file.write("second line\n")
    my_file.write("third line")


# In[ ]:

print type(my_file)


# In[ ]:

print dir(my_file)


# In[ ]:

my_file.write("something")


### Class

# In[ ]:

class BankAccount:
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount): 
        self.balance += amount
        
    def withdraw(self, amount): 
        self.balance -= amount


# In[ ]:

my_account = BankAccount(100)
my_account.withdraw(5)
print my_account.balance


# In[ ]:

your_account = BankAccount()
your_account.deposit(100)
your_account.deposit(10)
print your_account.balance


### Quiz

# Implement a Person type (or class) which has three properties (first_name, last_name, and birth_year); and two methods: full_name() and age(). The age() method should take the current year as an argument. You may use the template below.

# In[ ]:

class Person:
    
    def __init__(self, first_name, last_name, birth_year):
        pass
    
    def full_name(self):
        pass
    
    def age(self, current_year):
        pass


# An answer.

# In[ ]:

class Person:
    
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year


# In[ ]:

mr_park = Person("jae-sang", "Park", 1977)
print mr_park.full_name()


# In[ ]:

print mr_park.age(2014)


### Inheritance

# * A subtype is more specialized basetype.

# In[ ]:

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


# In[ ]:

psy = CoolPerson("PSY", 1977, "9bZkp7q19f0")
print psy.full_name()


# In[ ]:

print psy.age(2012)


# In[ ]:

# uncomment the line below and run (Shift+Enter) to see the style. 
# psy.show_off()


### Exception Handling

# * An exception is raised when a (run-time) error occurs. By default, the script stops running immediately.

# In[ ]:

L = [0, 1, 2, 3]
print L[5]


# `try`: ... `except`: ... let us catch the exception and handle it.

# In[ ]:

L = [0, 1, 2, 3]

try:
    print L[5]
    
except IndexError:
    print "no such element"
    
print "next"


### Throwing Exception

# We can `raise` (or throw) an exception as well.

# In[ ]:

def fetch(a_list, index):
    if index >= len(a_list):
        raise IndexError("Uh, oh!")
    return a_list[index]

print fetch(L, 5)


# Script can keep going if you catch and handle the exception.

# In[ ]:

L = [0, 1, 2, 3]

try:
    print fetch(L, 5)
    
except IndexError:
    print "an exception occurred"
    
print "next"


### Another Example

# `ulropen()` in `urllib2` module raises an exception when the web page is not found.

# In[ ]:

import urllib2

L = ["http://yahoo.com",
     "http://somethingfantastic",
     "http://bing.com"]

# we want to open each page in turn
for url in L:
    try:
        page = urllib2.urlopen(url, None, 1)
        print page.getcode()
    except:
        print "failed to open: {0}".format(url)


### A Data Structure Usage Example

# * STAN ([http://mc-stan.org](http://mc-stan.org)) is a C++ library / language implementing Markov chain Monte Carlo sampling (NUTS, HMC).
# 
# * STAN provides three interfaces (or API's): R, Python, and shell
# 
# * This is an example of using the Python API, which is provided in a Python module, PyStan <cite cite-data="STANSite">[1]</cite>.
# 
# * In order to run this, you need to install: Cython ([http://cython.org](http://cython.org)), NumPy ([http://www.numpy.org](http://www.numpy.org)), and STAN itself.
# 
# * From PyStan doc ([http://tinyurl.com/olap8sx](http://tinyurl.com/olap8sx), fiting the eight school model in Gelman et al. <cite cite-data="GelmanEtAl2003">[2, sec 5.5]</cite>

### Data Structure Usage Example (cont.)

# Import PyStan module and put STAN code in a string.

# In[ ]:

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


### Data Structure Usage Example (cont.)

# In[ ]:

schools_dat = {
    'J': 8,
    'y': [28,  8, -3,  7, -1,  1, 18, 12],
    'sigma': [15, 10, 16, 11,  9, 11, 10, 18]}

fit = pystan.stan(
    model_code=schools_code, 
    data=schools_dat, iter=1000, chains=4)

la = fit.extract(permuted=True)
mu = la['mu']

print str(fit)
get_ipython().magic(u'matplotlib inline')
fit.plot()


# * Input data are supplied in a dictionary
# * stan() function in the module runs the model.
# * The function returns a fit type object, which has several methods including extract() and plot().

### Summary

# List -- An ordered collection of objects. Mutable.
# 
# Dictionary -- A collection of key-value pairs. Mutable.
# 
# Tuple -- A sequence of values separated by commas. Immutable.
# 
# Class -- Defines a type, a grouping of properties and methods.
# 
# `try`: ... `except`: ...  -- Catch and handle exceptions.

### References

# * Stan project team site. http://mc-stan.org/team.html.
# * Andrew Gelman, John B. Carlin, H. S. S. D. B. R. Bayesian Data Analysis, 2nd ed. Chapman & Hall/CRC Texts in Statistical Science. Chapman and Hall/CRC, July 2003.
# * Wirth, N. Algorithms + Data Structures = Programs, 1st ed. Prentice Hall Series in Automatic Computation. Prentice-Hall, February 1976.
