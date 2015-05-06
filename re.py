
# coding: utf-8

# # Introduction to Regular Expressions

# ![caption](files/graphics/re.png)

# <small>Note: Image by <a href="https://wiki.python.org/moin/LionKimbro">Lion Kimbro</a> downloaded from <a href="https://wiki.python.org/moin/RegularExpression">Python Wiki</a> on Apr. 14, 2015.</small>

# ## What is RegEx?

# - Regular expressions (REs, regex or regex patterns) are an essential tool for processing text data.
# - It is a tiny, specialized (programming) language embedded inside other general purpose languages like Perl, Python, R, and Stata.
# - The *re* module in Python provides regex related functions and objects.

# ## What can we do with a RegEx?

# - To search _text_ for a part that matches a regex _pattern_

# You can also do:
# 
# - To match the beginning of the _text_ with a _pattern_  (`re.match()`)
# - To get all that match a _pattern_  (`re.findall()`, `re.finditer()`)
# - To substitute matches with replacement (`re.sub()`)
# - To split _text_ at the matches (`re.split()`)

# ## An Example

# In[1]:

# show the opr faculty page
from IPython.display import HTML

url = "http://opr.princeton.edu/faculty/"
HTML('<iframe src=' + url + ' width=700 height=350></iframe>')


# In[2]:

# get the html for the page
import urllib2

url = "http://opr.princeton.edu/faculty/"
text = urllib2.urlopen(url).read()
print text[:8000], "\n\n ... (many more lines) ... \n"


# In[3]:

# extracting names of the faculty, visitors, and postdocs
import re

pattern = r"<span class='em'>(.*?)</span>"
for name in re.findall(pattern, text):
    print name


# ## Another Example

# In[4]:

import re

text = """
 AAA  AAC  AAG  AAT  ACA  ACC  ACG  ACT  AGA  AGC  AGG  AGT  ATA 
 CAA  CAC  CAG  CAT  CCA  CCC  CCG  CCT  CGA  CGC  CGG  CGT  CTA 
 GAA  GAC  GAG  GAT  GCA  GCC  GCG  GCT  GGA  GGC  GGG  GGT  GTA 
 TAA  TAC  TAG  TAT  TCA  TCC  TCG  TCT  TGA  TGC  TGG  TGT  TTA 
"""

# mach and highlight any DNA codons that code for Arginine
pattern = r"\s(CG\S|AG[AG])\s"
replacement = r"<\g<1>>"

text = re.sub(pattern, replacement, text)
print text


# ## Basic Search

# In[5]:

import re

text = "Most letters and characters will match themselves"
pattern = r"mat\w\w"

match = re.search(pattern, text) # returns a match obj or None

if match:
    print "found:", match.group()
else:
    print "not found"


# - `re.search(pattern, text)` returns a match object if found or `None` if not.
# - It is a good habit to put your regex pattern in a raw string
# - The pattern matches "mat" followed by any two *word characters*. A word character is a letter, digit, or an underscore character.

# ## Simple Patterns

# * Letters and characters will match themselves
# * Meta-characters (i.e., `.` `^` `$` `*` `+` `?` `{` `}` `[` `]` `(` `)` `\` `|`) don't match themselves -- they have special meanings

# ## Matches a Single Character

# * Basic patterns that match a single character:
#     
#     <table>
#         <tr><th>Pattern</th><th>(Description)</th><th>Matches</th></tr>
#         <tr><th>.</th><td>(dot)</td><td nowrap>any single character except newline</td></tr>
#         <tr><th>\d</th><td>(\ lower case d)</td><td nowrap>a digit, [0-9]</td></tr>
#         <tr><th>\D</th><td>(\ upper case D)</td><td nowrap>a non-digit</td></tr>
#         <tr><th>\s</th><td>(\ lower case s)</td><td nowrap>a "whitespace" character, [\n\r\t\f]</td></tr>
#         <tr><th>\S</th><td>(\ upper case S</td><td nowrap>a non-writespace character</td></tr>
#         <tr><th>\w</th><td>(\ lower case w)</td><td nowrap>a "word" character</td></tr>
#         <tr><th>\W</th><td>(\ upper case W)</td><td nowrap>a non-word character</td></tr>
#         <tr><th>[abc]</th><td></td><td>matches character a, b or c</td></tr>
#         <tr><th>[a-z]</th><td></td><td>matches any single lower-cased characater</td></tr>
#         <tr><th>[2468]</th><td></td><td>matches one digit which is either 2, 4, 6, or 8</td></tr>
#     </table>
# 
# * The following matches not a character, but a boundary:
# 
#     <table>
#         <tr><th>Pattern</th><th>(Description)</th><th>Matches</th></tr>
#         <tr><th>\b</th><td>\ lower case b</td><td>a boundary between a word and a non-word character</td></tr>
#         <tr><th>^</th><td>(caret)</td><td>the beginning of a text string</td></tr>
#         <tr><th>\$</th><td></td><td>the end of a text string</th></tr>
#     </table>
# 

# In[6]:

import re

text = "This is my phone number 555-1234. Call me at 9:00am!"
pattern = r"\d\d\d-\d\d\d\d"

match = re.search(pattern, text)

if match:
    print "found:", match.group()
else:
    print "not found"


# ## Quiz. Write a regex pattern that matches 9:00 am

# In[7]:

import re

text = "This is my phone number, 555-1234. Call me at 9:00 am!"
pattern = r"" # replace this with your pattern

match = re.search(pattern, text)

if match:
    print "found:", match.group()
else:
    print "not found"


# ## Examples

# In[8]:

import re

text = "Lunch will be served at 12:00 pm."

match = re.search(r"..nch", text)           # match.group() == "Lunch"
match = re.search(r".unc[a-z]", text)       # match.group() == "Lunch"
match = re.search(r"lunch", text)           # match == None
match = re.search(r"L\w\w\w\w", text)       # match.group() == "Lunch"

match = re.search(r"\d\d:\d\d [ap]m", text) # match.group() == "12:00 pm"
match = re.search(r"s...ed", text)          # match.group() == "served"

match = re.search(r"^...", text)            # match.group() == "Lun"
match = re.search(r".e\b", text)            # match.group() == "be"
match = re.search(r"....\W$", text)         # match.group() == "0 pm."


# In[9]:

# let's just take a break. unquote to open the web page
import webbrowser
# webbrowser.open("http://tinyurl.com/mh9olpo")


# ## Repetition

# <table>
#     <tr><th>pattern</th><th>matches</th><th>equivalent to</th></tr>
#     <tr><th>*</th><td>0 or more occurrences of the pattern to its left</td><td>{0,}</td></tr>
#     <tr><th>+</th><td>1 or more occurrences of the pattern to its left</td><td>{1,}</td></tr>
#     <tr><th>?</th><td>0 or 1 occurrences of the pattern to its left</td><td>{0,1}</td></tr>
# </table>
# 
# The search finds the earliest (leftmost) matching sub-text for the pattern then it tries to use up as many characters as possible for the repetition. (The + and * are said to be _greedy_.)
# 
# You can also specify repetitions with curly brackets ({  })
# <table>
#     <tr><th>pattern</th><th>matches</th></tr>
#     <tr><th>{m}</th><td>exactly m occurrences of the pattern to its left</td>
#     <tr><th>{m,n}</th><td>from m occurrences (default $0$) to n times (default $+\infty$) of the pattern to its left</td></tr>
# </table>

# In[10]:

import re

text = "Vroooooooom Vrooom   Vroom"
pattern = r"o+"

match = re.search(pattern, text)
if match:
    print "match:", match.group()
else:
    print "no match"


# ## Repetition Examples

# In[11]:

import re

text = "Vroooooooom Vrooom   Vroom"

match = re.search(r"Vro+m", text)     # match.group() == "Vroooooooom"
match = re.search(r"A+", text)        # match == None
match = re.search(r"\w+\s+\w+\s+\w+", text) # three words separated by 1+ spaces

match = re.search(r"A*", text)        # len(match.group()) == 0
match = re.search(r"\w*m", text)      # match.group() == "Vroooooooom"
match = re.search(r"\w*$", text)      # match.group() == "Vroom"

match = re.search(r"Vroo?m", text)    # match.group() == "Vroom"
match = re.search(r"\s\s+\w+", text)  # match.group() == "Vroom"
match = re.search(r"\s\s*\w+", text)  # match.group() == "Vrooom"

match = re.search(r"\b\w+", text)     # match.group() == "Vroooooooom"
match = re.search(r"^\b\w+", text)    # match.group() == "Vroooooooom"

match = re.search(r"Vro{3}m", text)   # match.group() == "Vrooom"
match = re.search(r"Vro{0,7}m", text) # match.group() == "Vrooom"
match = re.search(r"Vro{4,7}m", text) # match == None


# ## Character Classes or Square Brackets

# - matches a single character
# - you can list a set of characters to match. `[aeiou]` matches any vowel
# - complement set can be specified by a caret (`^`). For example, `[^aeiou]` matches anything but a vowel. Notice that the caret should be the first character in within the brackets. Outside the brackets, the caret (`^`) matches the beginning of the text.
# - ranges can be specified. `[0-9]` matches a digit
# - you can use special sequences like `\w`, `\d`, `\s` and the like.
# - dot (`.`) within the brackets represents a dot, not any character.
# - in fact, there are very few special characters within the character classes, including: `^` (complement), `-` (range), and `]` (signals the end of the character class)
# - an example of matching email addresses.

# In[12]:

import re

text = "This is my email address: funny.changarilla@princeton.edu"
pattern = r"[\w.]+@[\w.]+"

match = re.search(pattern, text)

if match:
    print "match:", match.group()
else:
    print "no match"


# ## Groups or parentheses

# - Groups let you pick out parts of the matching string
# - Use parentheses to make groups
# - Let's group the email pattern by username and hostname. See below example

# In[13]:

import re

text = "This is my email address: funny.changarilla@princeton.edu"
pattern = r"([\w.]+)@([\w.]+)"

match = re.search(pattern, text)

if match:
    print "match.group():", match.group()
    print "match.group(1):", match.group(1)
    print "match.group(2):", match.group(2)
else:
    print "no match"


# ## What Else Does the Match Object Return?

# In[14]:

import re

text = "This is my email address funny.changarilla@princeton.edu, email me!"
        #----+----1----+----2----+----3----+----4----+----5----+-
pattern = r"([\w.]+)@([\w.]+)"

match = re.search(pattern, text)
#print dir(match)

if match:
    print "match.start():", match.start()
    print "match.end():", match.end()
    print "match.span():", match.span()
#    print "text[match.start():match.end]:", text[match.start():match.end()]


# ## Alternation (`|`)

# `pattern_A|pattern_B` matches either `pattern_A` *or* `pattern_B`

# In[15]:

import re

text = "I love a dog. You love a cat."
pattern = r"dog|cat"

match = re.search(pattern, text)

if match:
    print "match:", match.group()
else:
    print "no match"


# ## Escaping Meta-characters

# In[16]:

import re

text = "re.search() returns the 1st match. re.findall() returns a [list]"
pattern = r"\w+\(\)"    # use the slash to escape

match = re.search(pattern, text)

if match:
    print "match:", match.group()
else:
    print "no match"


# ## Options or Compilation Flags

# - `I` or `IGNORECASE` performs case-insentive matching
# - `M` or `MULTILINE` does multi-line matching, affecting `^` and `$`
# - `S` or `DOTALL` makes the dot `.` match any character including the newline `\n`
# - Multiple options can be specified by concatenating with pipes (`|`)

# In[17]:

import re

text = """Substitution can be done with re.sub(pattern, text).
and splits with re.split(pattern, text).
"""
pattern = r"sub.+"

match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

if match:
    print "match:", match.group()
else:
    print "no match"


# ## Quiz: Write a regex pattern to match any adverb

# Hint: Let's define an adverb as a word that ends with "ly". You can use any text, or use the text given below.
# 
# 

# In[18]:

import re

text = """
Once upon a time, there was a beautiful princess who had a golden ball.
She lived in a palace with her father, the King, and her seven sisters.
Every day she played with her ball in the garden of the palace.
At the end of the garden there was a deep, dark lake. Unfortunately, 
one day she dropped her golden ball into the water. She was very unhappy
and she sat on the grass and started to cry. Suddenly, she heard a voice:
"Don't cry, princess".
She opened her eyes and saw a large green frog. "Oh, please help me!"
she said, "I can't get my ball."
"I'll help you", said the frog, "if I can com and live with you in the
palace!"
"Yes, yes, of course. I promise," said the princess.
So the frog jumped into the water and cam back with the ball.
The princess laghed and took the ball. She ran quickly back to the palace
and forgot all about the frog.
"""


# In[ ]:




# ## Quiz. Find all the adverbs in the text

# Hint: The function `re.findall(pattern, text)` returns all the matching sub-text as a list.
# 

# In[ ]:




# ## Quiz. Validate a poker hand

# Suppose that you are writing a poker program where a player's
# hand is represented as a five-character string with each character
# representing a card, "a" for ace, "k" for king, "q" for queen, "j"
# for jack, 't" for 10, and "2" through "9" representing the card
# with that value.
# 
# Write a pattern to validate a hand. It does not have to be very thorough. Just to pass the test cases shown below.

# In[19]:

import re

pattern = r""  # replace this with your pattern

match = re.search(pattern, "245")         # match == None
match = re.search(pattern, "a 334")       # match == None
match = re.search(pattern, "akt5q")       # match.group() == "akt5q"
match = re.search(pattern, "akt5e")       # match == None
match = re.search(pattern, "727ak")       # match.group() == "727ak"
match = re.search(pattern, " akt34")      # match == None
match = re.search(pattern, "23456  ")     # match == None


# ## Learning Resources

# - Official [Reference](https://docs.python.org/2/library/re.html) and Kuchling's [HowTo](https://docs.python.org/2/howto/regex.html#regex-howto)
# - Friedl's book, [Mastering Regular Expressions](http://www.amazon.com/Mastering-Regular-Expressions-Jeffrey-Friedl/dp/0596528124/)
# - Google Developers site Python Course [Chapter](https://developers.google.com/edu/python/regular-expressions)
# - Tartley (Jonathan Hartley)'s [Cheatsheet](https://github.com/tartley/python-regex-cheatsheet/releases/download/v0.3.3/cheatsheet.pdf)
