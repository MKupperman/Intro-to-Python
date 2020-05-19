"""
objects.py

We can make an object and use it in the same script
"""


class polynomial(object):
    def __init__(self, coef_list):
        """
        The __init__ method is called whenever a new instance of an object is created.
        All attributes should be created within the __init__ method.
        :param coef:
        """
        assert type(coef_list) is list, 'error message indicating that coef is not a list'
        self.degree = len(coef_list) - 1
        self.coefs = []
        for coef in coef_list:
            self.coefs.append(coef)

    # methods are implemented similar to functions, but take a required argument self
    # self is a method argument when the method is called.
    def evaluate(self, x):
        total = 0
        for degree, coef in enumerate(self.coefs):
            # degree -= 1
            power = x ** degree
            total = total + coef * power

        return total

    # We can add overload the + operator and return a new object of the same class
    def __add__(self, other):
        max_coefs = max(len(self.coefs), len(other.coefs))-1
        min_coefs = min(len(self.coefs), len(other.coefs))-1
        new_coef = [None] * (min_coefs + 1)  # pre-allocate
        for degree in range(min_coefs+1):
            # we know that the first min_coefs exist
            new_coef[degree] = self.coefs[degree] + other.coefs[degree]
        if min_coefs < max_coefs:  # the degrees are different
            for degree in range(min_coefs+1, max_coefs+1):
                # we know that the first min_coefs exist
                try:
                    new_coef.append(self.coefs[degree])
                except IndexError:  # if the first attempt returns an IndexError, keep going
                    new_coef.append(other.coefs[degree])
        return polynomial(coef_list=new_coef)

    def __str__(self):
        """ A string representation of the object, called by print and str functions """
        string = ''
        for degree, coef in enumerate(self.coefs, 1):
            degree = degree - 1
            string += str(coef)+'x^' + str(degree) + ' + '
        string = string[0:-3]  # remove the last ' + '
        return string


# Subclassing can be done
class monoid(polynomial):
    def __init__(self, degree):
        coef = [1] * degree
        super(monoid, self).__init__(coef_list=coef)


# Or we can use a function to build a polynomial object that's mathematically a monoid
def make_monoid(degree):
    return polynomial(coef_list=[1] * degree)

# What's the difference? We've made a new class vs a function call that returns an object with specified properties
# Very flexable!

