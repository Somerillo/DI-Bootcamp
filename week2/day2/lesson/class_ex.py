#EX1 in class

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(2)
# #output:2

# nc.diameter = 4
# print(nc.diameter)

# nc.grow()
# #8
# print(nc.diameter)

#EX2 in class

# class Door():
#     def __init__(self, is_opened=True):
#         self.is_opened = is_opened

#     def open_door(self):
#         if self.is_opened:
#             print('The door was already opened')
#         else:
#             print('The door is now opened')

#     def close_door(self):
#         if not self.is_opened:
#             print('The door was already closed')
            
#         else:
#             print('The door is now closed')
#             self.is_opened = False

# class BlockedDoor(Door):
#     def open_door(self):
#         raise Exception('Blocked Door cannot be open')

#     def close_door(self):
#         raise Exception('Blocked Door cannot be close')


# door1 = Door()
# door2 = BlockedDoor()

# door1.close_door()
# print(door1.is_opened)

# door2.close_door()

#EX3

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

try:
    sum(my_list)
except:
    raise TypeError('There are strings in the list')