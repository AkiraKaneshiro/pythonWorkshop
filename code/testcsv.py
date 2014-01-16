
import csv

with open("test.csv", "wb") as f:
    my_writer = csv.writer(f, quoting=csv.doublequote)
    i = 15
    while i < 30:
      my_writer.writerow([i, "yahoo!"])
      i += 3


