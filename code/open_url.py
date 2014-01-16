import urllib2

# let us open a web page
url = "http://opr.princeton.edu"
opr = urllib2.urlopen(url)
print opr.getcode()
# 200 -- means OK

# if uncommented, then will raise an exception and stop
# url = "http://opr.princeton.edu/nosuchpage"
# opr = urllib2.urlopen(url)
# urllib2.HTTPError: HTTP Error 404: Not Found
# print opr.getcode()

# handling exception and keep going
print
L = ["http://google.com",
     "http://google.com/somethingfantastic",
     "http://yahoo.com"]

for url in L:
    try:
        page = urllib2.urlopen(url)
        print page.getcode()
    except urllib2.HTTPError:
        print "failed to open: {0}".format(url)

