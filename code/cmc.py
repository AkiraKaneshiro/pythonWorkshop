def cmc(year, month):
    ''' returns DHS Century Month Code '''

    if year < 1900 or year > 2099:
        print "year out of range"
        return

    if month < 1 or month > 12:
        print "month out of range"
        return

    return (year - 1900) * 12 + month

# call the function
print cmc(2014, 1)
# 1369

print cmc(2014, 15)
# month out of range
\
