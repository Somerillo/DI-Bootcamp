
#     OOP dunder methods


# Instructions :

# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

#     Compute the circle’s area
#     Print the attributes of the circle - use a dunder method
#     Be able to add two circles together, and return a new circle with the new radius - use a dunder method
#     Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
#     Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
#     Be able to put them in a list and sort them
#     Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

pi = 3.
avogadro = 6.023E23
answer_to_life_the_universe_and_everything = 42


class Circle:
    # __init__: Initializes with either a radius or a diameter
    def __init__(self, radius=0, diameter=None):
        if diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = radius

    @property  # diameter property
    def diameter(self):
        return self.radius / 2

    @diameter.setter  # set radius when diameter changes
    def diameter(self, new_diam):
        self.radius = new_diam / 2  # without RETURN!!!

    @property  # area calculation
    def area(self):
        return pi * (self.radius**2)

    def __str__(self):  # user friendly output message for printing in str format the attributes of the circle
        return f"radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area}. Answer to life, the universe, and everything={answer_to_life_the_universe_and_everything}\n"

    def __add__(self, other):  # Allows adding two Circle instances by radius, returning a new Circle
        if isinstance(other, Circle):
            new_radius = (self.radius**2 + other.radius**2)**0.5
            return Circle(new_radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius

    def __repr__(self):  # representation method for debugging
        return f"Circle(radius={self.radius:.2f})"


# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
c1 = Circle(radius=1/3**0.5)
c2 = Circle(radius=1)

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
print(c1)
print(c2)

# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
c3 = c1 + c2
print(c3)

# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
print(c1 < c2)
print(c1 > c2)
print(c1 == c2)

# Be able to put them in a list and sort them
c4 = Circle(radius=6.023E-23)
c5 = Circle() # radius = 0 by default
c0 = Circle(5)
circles_list = [c0, c1, c2, c3, c4, c5] # sorted by radius BECAUSE __lt__, __gt__, __eq__ ARE DEFINED BY RADIUS!!!!!!
print(sorted(circles_list))

# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles
#
#                     ______________
#                    |              |
#                    |  I hate OOP  |
#    _____     ____  |______________|
#   /      \  |  o |  _/
#  |        |/ ___\| 
#  |_________/     
#  |_|_| |_|_|
#
#
#