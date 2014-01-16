
"""defines Person and CoolPerson types."""

import webbrowser  # for CoolPerson.show_off()

class Person:
    """ person with first and last name and birth_year """

    def __init__(self, first, last, birth_year):
        self.first_name = first
        self.last_name = last
        self.birth_year = birth_year

    def full_name(self):
        return self.first_name + " " + self.last_name

    def age(self, current_year):
        return (current_year - self.birth_year)


class CoolPerson(Person):
    """ Goes by with a single name only and shows off a mv. """

    def __init__(self, name, birth_year, mv):
        Person.__init__(self, name, None, birth_year)
        self.mv = mv

    def full_name(self):
        return self.first_name

    def show_off(self):
        url = "http://www.youtube.com/watch?v={0}"
        webbrowser.open(url.format(self.mv))

if __name__ == "__main__":
    print "testing Person"
    mary = Person("Mary", "Smith", 1990)
    print "mary:", str(mary)
    print "mary.full_name():", mary.full_name()
    print "mary.age(2014):", mary.age(2014)
    print
    print "testing CoolPerson"
    psy = CoolPerson("PSY", 1977, "9bZkp7q19f0")
    print "psy.full_name():", psy.full_name()
    print "psy.age(2012):", psy.age(2012)
    print "psy.show_off():", psy.show_off()

