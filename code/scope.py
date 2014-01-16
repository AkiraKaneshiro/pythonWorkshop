import sys

def ex(header):
    print "\n#", header


ex("local var is independent of global var")
x = 1
def func():
    x = 2          # local
    print x
func()             # 2
print x            # 1


ex("cannot assign to a global")
x = 1
def func():
    x = x + 1     # x += 1 also fails
try:
    func()
except:
    print sys.exc_info()[0]


ex("unless declared so")
x = 1
def func():
    global x
    x = x + 1
func()
print x          # 2


ex("globals readable, of course")
x = 1
def func():
   y  = x + 1
   print y
func()
print x


ex("2.7* does not have the nonlocal." +
   " a way around is to use a mutable")
def outer():
    D = {'x': 1}
    def inner():
        D['x'] = 2
        print D['x']
    inner()
    print D['x']
outer()

