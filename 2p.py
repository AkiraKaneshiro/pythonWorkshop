
# coding: utf-8

# # Introduction to Python 2

# May, 2015
# 
# Chang Y. Chung

# ## Algorithms + Data Structures = Programs

# Niklaus Wirth (1976)<cite data-cite="Wirth1976">[3]</cite>
# 
# ![](files/graphics/wirth.png)

# Python's built-in data structures include:
# 
# * List
# * Dictionary
# * Tuple
#   
# We will also briefly talk about:
# 
# * Class
# * Exception Handling

# ## List

# * Ordered (indexed) collection of arbitrary objects.
# * Mutable -- may be changed in place.

# Ordered collection of arbitrary objects.

# In[1]:

L = []     # an empty list
L = list() # this works too

L = [1, 2.5, "abc" , [56.7, 78.9]]
print len(L) 
print L[1] 
print L[3][0]


# * Iterating over list elements.

# In[2]:

L = [1, 2.5, "abc" , [56.7, 78.9]]
for x in L:
    print x


# * List comes equipped with lots of methods.

# In[3]:

print "abc" in L
print L.count("abc")
print L.index("abc")


# * List is mutable -- may be changed in place.

# In[4]:

L = []
L.append(5)
print L


# In[5]:

L[0] = 23
print L


# In[6]:

L = [23]
M = [87, 999]
L.extend(M)
print L


# In[7]:

del L[2]
print L


# Let's define a function that accepts a list as an argument.

# In[8]:

def squares(a_list): 
    s=[]
    for el in a_list:
        s.append(el ** 2) 
    return s
    
sq = squares([1, 2, 3, 4]) 
print sq, sum(sq)


# Aliasing vs. copying

# In[9]:

L = [1, 2, 3, 4]
M = L       # aliasing
L[0] = 87

print "M=", M


# In[10]:

L = [1, 2, 3, 4]
M = list(L) # (shallow) copying
L[0] = 87
print M


# ## Quiz

# In[11]:

L = [1, 2, [3, 4], 5, "xyz"]


# Run the above cell and create L (Select the cell and Shift+Enter). And then evalute the following expressions.

# In[12]:

L[1] == 1


# In[13]:

len(L) == 5


# In[14]:

L[2] == 3, 4


# In[15]:

[3] in L


# In[16]:

L.index("xyz") == 4


# ## Quiz (Cont.)

# In[17]:

L = [1, 2, [3, 4], 5, "xyz"]


# Evalute the following expressions:

# In[18]:

L[-1] == "xyz"


# In[19]:

L[-1][-1] == "z"


# In[20]:

any([1,2,3]) == True


# In[21]:

L[9] == None


# In[57]:

len([0,1,2,]) == 3


# ## Quiz

# Write a function that, given a list of integers, returns a _new_ list of odd numbers only. For instance, given the list, [0, 1, 2, 3, 4], this function should return a new list, [1, 3]. (Hint: Create a new empty list. Loop over the old one appending only odd numbers into the new one. Return the new one.)

# In[88]:

# an answer
L = [0, 1, 2, 3, 4]

def odd_only(a_list):
    s = []
    for el in a_list:
        if (el % 2) == 1:
            s.append(el)
    return s

# check
print odd_only(L)


# ## Quiz

# (tricky) Write a function similar to the previous one. This time, however, do not return a new list. Just modify the given list so that it has only the odd numbers. (Hint: `del L[0]` removes the first element of the list, `L`)

# Here is an answer.

# In[95]:

# an answer
L = [0, 1, 2, 3, 4]

def is_odd(n):
    return (n % 2) == 1

def odd_only(a_list):
    i = 0
    length = len(a_list)
    while i < length:
        if not is_odd(a_list[i]):
            del a_list[i]
            i -= 1
            length -= 1
        i += 1
    
# check
print "before: %r" % L
odd_only(L)
print "after: %r" % L



# Here is another answer. Looping last-to-first element -- this way, we preserve the indices as they are, even we remove some elements.

# In[105]:

# an answer
L = [0, 1, 2, 3, 4]

def is_odd(n):
    return (n % 2) == 1

def odd_only(a_list):
    for i in range(len(a_list) - 1, 0 - 1, -1):
        if not is_odd(a_list[i]):
            del a_list[i]

# check
print "before: %r" % L
odd_only(L)
print "after: %r" % L


# In practice, I'd just create a new list with a comprehension.

# In[106]:

# an answer
L = [0, 1, 2, 3, 4]

M = [x for x in L if x % 2 == 1]
print M


# ## Slice Index

# * Applies to any sequence types, including list, str, tuple, ...
# 
# * Has three (optional) parts separated by a colon (:), `start:end:step`, indicating `start` through but not past `end`, by `step`; Indices point in-between the elements.

# <pre>
#    +−−−+−−−+−−−+−−−+−−−+−−−+ 
#    | p | y | t | h | o | n |
#    +−−−+−−−+−−−+−−−+−−−+−−−+
#    0   1   2   3   4   5   6
#   −6  −5  −4  −3  −2  −1
# </pre>

# List slicing Examples:

# In[59]:

L = ['p', 'y', 't', 'h', 'o', 'n']


# In[60]:

print L[:2] # first two


# In[61]:

print L[1:3]


# In[62]:

print L[0:5:2]


# In[63]:

print L[-1] # the last element


# In[64]:

print L[:]  # a (shallow) copy


# In[65]:

print L[3:]


# In[66]:

print L[-2:] # last two


# In[67]:

print L[::-1] # reversed


# ## Quiz

# Suppose that you collect friendship network data among six children, each of whom we identify with a number: 0, 1, ..., 5. The data are represented as a list of lists, where each element list represents the element child's friends.

# In[68]:

L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]


# For instance, the kid 0 friends with the kids 1 and 2, since

# In[69]:

L[0] == [1, 2]


# Calculate the average number of friends the children have. (Hint: len() function returns the list size.)

# An answer:

# In[114]:

# an answer
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]

N = len(L)
total = 0
for ego in range(N):
    alters = L[ego]
    total += len(alters)
avg = float(total) / N

print "average number of friends: %f" % avg


# With a list comprehension, this can be as simple as:

# In[70]:

print 1.0 * sum([len(x) for x in L]) / len(L)


# ## Quiz (cont.)

# Write a function to check if _all_ the friendship choices are reciprocated. It should take a list like previous one and return either True or False. (Hint: You may want to use a utility function below.)

# In[115]:

def mutual(a_list, ego, alter):
    return alter in a_list[ego] and ego in a_list[alter]


# In[172]:

def all_reciprocated(a_list):
    for ego in range(len(a_list)):
        alters = a_list[ego]
        for alter in alters:
            if not mutual(a_list, ego, alter):
                return False 
    return True

# check
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3]]
print all_reciprocated(L)


# In[173]:

# another check
L = [[1, 2], [0, 2, 3], [0, 1], [1, 4, 5], [3, 5], [3, 4]]
print all_reciprocated(L)


# ## List Comprehension

# A concise way to create a list. An example:

# In[117]:

L = [x for x in range(5) if x % 2 == 1]
print L


# An equivalent code using the for loop:

# In[118]:

L = []
for x in range(5):
    if x % 2 == 1:
        L.append(x)
print L


# More list comprehension examples:

# In[119]:

[x - 5 for x in range(6)]


# In[120]:

[abs(x) for x in [-2, -1, 0, 1]]


# In[121]:

[x for x in range(6) if x == x ** 2]


# In[122]:

[1 for x in [87, 999, "xyz"]]


# In[123]:

[x - y for x in range(2) for y in [7, 8]]


# ## Dictionary

# * A collection of key-value pairs.
# * Indexed by keys.
# * Mutable.
# * Also known as associative array, map, symbol table, ...
# * Usually implemented as a hash table.

# * A collection of key-value pairs, indexed by keys.

# In[124]:

D = {}     # an empty dict
D = dict() # also works

D["one"]=1
D["two"]=2
print D


# In[125]:

print D.keys()


# In[126]:

print "three" in D.keys()


# In[127]:

D = {"Apple": 116, "Big Mac": 550}

for key in ["Apple", "Orange", "Big Mac"]:
    if key in D:
        print "{0} has {1} calories".format(key, D[key])
    else:
        print "{0} is not found in the dictionary".format(key)


# More Dictionary examples.

# In[128]:

D = {"China": 1350, "India":1221, "US":317}

for key in D.keys():
    print "Pop of {0}: {1} mil".format(key, D[key])


# * Mutables cannot be keys.

# In[129]:

D = {[1, 2]: 23}


# * Values can be almost of any type.

# In[130]:

D = {2: [2, 3], 200: [3, 4], 95: [4, 5]}
print D[2]
print D[200]


# ## Data Structure

# SAT has three subsections: Critical Reading, Mathematics, and Writing. A result of taking an SAT exam is three scores.

# In[131]:

# data
SAT = {"cr": 780, "m": 790, "w": 760}


# In[132]:

# usage
print SAT["m"]


# You can take SAT exams more than once.

# In[133]:

# data
SAT = [{"cr": 780, "m": 790, "w": 760},
       {"cr": 800, "m": 740, "w": 790}]


# In[134]:

# usage
print SAT[0]


# In[135]:

print SAT[0]["cr"]


# ## More Complicated Data Structure

# In[136]:

SAT = {"Jane": {"lastname" : "Thompson",
                "test": [{"cr": 700, "m": 690, "w":710}] },
       "Mary": {"lastname" : "Smith",
                "test": [{"cr": 780, "m": 790, "w": 760},
                         {"cr": 800, "m": 740, "w": 790}] } }


# In[137]:

print SAT["Jane"]


# In[138]:

print SAT["Jane"]["lastname"]


# In[139]:

print SAT["Jane"]["test"]


# In[140]:

SAT = {"Jane": {"lastname" : "Thompson",
                "test": [{"cr": 700, "m": 690, "w":710}] },
       "Mary": {"lastname" : "Smith",
                "test": [{"cr": 780, "m": 790, "w": 760},
                         {"cr": 800, "m": 740, "w": 790}] } }


# In[141]:

print SAT["Jane"]["test"]


# In[142]:

print SAT["Jane"]["test"][0]


# In[143]:

print SAT["Jane"]["test"][0]["cr"]


# In[144]:

mary1 = SAT["Mary"]["test"][1]
print mary1["cr"]


# ## Quiz

# * Make a dictionary of 2012 SAT percentile ranks for the scores from 680 to 700 and for all three subsections. The full table is available at [http://tinyurl.com/k38xve8](http://tinyurl.com/k38xve8).
# 
# * Given this dictionary, say D, a lookup, D[680]["cr"] should be evaluated to 93.

# In[175]:

# an answer
D = {700: {"cr":95, "m":93, "w":96},
     690: {"cr":94, "m":92, "w":95},
     680: {"cr":93, "m":90, "w":94}}

# check
print D[680]["cr"]


# ## Quiz (cont.)

# Write a new dictionary DD such that we look up the subsection first and then the score. That is, DD["cr"][680] should be evaluated to 93. (Hint: Start with a dictionary below.)

# In[176]:

# an answer
DD = {"cr": {700: 95, 690: 94, 680: 93}, 
      "m": {700: 93, 690: 92, 680: 90},
      "w": {700: 96, 690: 95, 680: 94}}

# check        
print DD["cr"][680]    


# ## Tuples

# * A sequence of values separated by commas.
# * Immutable.
# * Often automatically _unpacked_.

# * A sequence of values separated by commas. Immutable.

# In[177]:

T = tuple()
T = () # also works

N = (1) # not a tuple
T = (1, 2, "abc") # a tuple
print T[0]


# In[148]:

T[0] = 9 # immutable


# * Often automatically unpacked.

# In[178]:

T = (2, 3)
a, b = T
print a, b


# In[179]:

a, b = b, a # swap
print a, b


# In[180]:

D = {"x": 23, "y": 46}
D.items() # returns a list of tuples


# In[181]:

for k, v in D.items():
    print "%s ==> %d" % (k, v)


# ## Class

# * Class defines a (user-defined) type, a grouping of some data (properties) and functions that work on the data (methods).
# 
# * An object is an _instance_ of a type.

# Examples:

#   - `int` is a type; `23` is an object.
#   - `str` a type; `"abc"` an object.
#   - `word document file` a type; `my_diary.docx` is an object.
#   - We have been using objects.

# ## Examples of Built-in Types

# `str` type has a bunch of methods.

# In[182]:

"abc".upper()


# In[183]:

"abc".find("c")


# In[184]:

"abc".split("b")


# * `open()` function returns a `file` object (representing an opened file).

# In[185]:

with open("code/test.txt", "w") as my_file:
    my_file.write("first line\n")
    my_file.write("second line\n")
    my_file.write("third line")


# In[186]:

print type(my_file)


# In[154]:

print dir(my_file)


# In[187]:

my_file.write("something")  # this errors due to indentation!


# ## Class

# In[188]:

class BankAccount:
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount): 
        self.balance += amount
        
    def withdraw(self, amount): 
        self.balance -= amount


# In[189]:

my_account = BankAccount(100)
my_account.withdraw(5)
print my_account.balance


# In[190]:

your_account = BankAccount()
your_account.deposit(100)
your_account.deposit(10)
print your_account.balance


# ## Quiz

# Implement a Person type (or class) which has three properties (first_name, last_name, and birth_year); and two methods: full_name() and age(). The age() method should take the current year as an argument. You may use the template below.

# In[191]:

class Person:
    
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth_year


# In[192]:

mr_park = Person("jae-sang", "Park", 1977)
print mr_park.full_name()


# In[193]:

print mr_park.age(2015)


# ## Inheritance

# * A subtype is more specialized basetype.

# In[194]:

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


# In[199]:

psy = CoolPerson("PSY", 1977, "rX372ZwXOEM")
print psy.full_name()


# In[200]:

print psy.age(2015)


# In[201]:

# uncomment the line below and run (Shift+Enter) to see the style. 
#psy.show_off()


# ## Exception Handling

# * An exception is raised when a (run-time) error occurs. By default, the script stops running immediately.

# In[202]:

L = [0, 1, 2, 3]
print L[5]


# `try`: ... `except`: ... let us catch the exception and handle it the way we want.

# In[167]:

L = [0, 1, 2, 3]

try:
    print L[5]
    
except IndexError:
    print "no such element"
    
print "next"


# ## Throwing Exception

# We can `raise` (or throw) an exception as well.

# In[168]:

def fetch(a_list, index):
    if index >= len(a_list):
        raise IndexError("Uh, oh!")
    return a_list[index]

print fetch(L, 5)


# Script can keep going if you catch and handle the exception.

# In[203]:

L = [0, 1, 2, 3]

try:
    print fetch(L, 5)
    
except IndexError:
    print "an exception occurred"
    
print "next"


# ## Another Example

# `ulropen()` in `urllib2` module raises an exception when the web page is not found.

# In[204]:

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


# ## Summary

# List -- An ordered collection of objects. Mutable.
# 
# Dictionary -- A collection of key-value pairs. Mutable.
# 
# Tuple -- A sequence of values separated by commas. Immutable.
# 
# Class -- Defines a type, a grouping of properties and methods.
# 
# `try`: ... `except`: ...  -- Catch and handle exceptions.

# ## References

# * Stan project team site. http://mc-stan.org/team.html.
# * Andrew Gelman, John B. Carlin, H. S. S. D. B. R. Bayesian Data Analysis, 2nd ed. Chapman & Hall/CRC Texts in Statistical Science. Chapman and Hall/CRC, July 2003.
# * Wirth, N. Algorithms + Data Structures = Programs, 1st ed. Prentice Hall Series in Automatic Computation. Prentice-Hall, February 1976.
