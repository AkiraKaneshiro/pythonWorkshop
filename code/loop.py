import timeit

code = """
total = 0
for i in range(1000):
    for j in range(1000):
        total += i
print total
"""
t = timeit.Timer(code)
dur = t.timeit(number=1)
print "ran in: {0:.3f} sec".format(dur)


# manual optimization
code = """
print sum( [1000 * i for i in range(1000)] )
"""
t = timeit.Timer(code)
dur = t.timeit(number=1)
print "ran in: {0:.3f} sec".format(dur)

