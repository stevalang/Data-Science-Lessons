# print(help(list))

# def avg(lst):
#     return sum(lst) / len(lst)
#self, diameter, width, color, material, count

# def __init__(self, diameter, width, color, material, count):

# class Wheels:
#   def __init__(self, diameter, width, color, material, count):

# class Wheelset:
#     def __init__(self, diameter, width, color, material, count):
#       self.diameter = diameter
#       self.width = width
#       self.color = color
#       self.material = material
#       self.count = count


# dope_wheels = Wheelset(17, 23, 'silver', 'aluminum', 4)


# class Car:
#   def __init__(self, name, wheelset, color, spoiler_color=None, oversize=False,location=[0, 0]):
#     self.wheelset = wheelset
#     self.color = color
#     self.location = location
#     self.spoiler_color = spoiler_color
#     self.oversized = False

#     if wheelset.count > 4:
#       self.oversized = True

#   def drive_north(self, distance):
#     self.location[0] += int(distance/10)




# no_sp_car = Car('Pontiac', 4, 'Red')

# sp_car = Car('Ferrari', dope_wheels, 'Red', 'Red')

# # print(no_sp_car)
# print(sp_car.location)
# print(sp_car.drive_north(10))
# print(sp_car.location)


# class Person:
#   def __init__(self, name, height, age):
#     self.name = name
#     self.height = height
#     self.age = age

#     if age >= 21:
#       self.adult = True
#     else:
#       self.adult = False

# lance = Person('Lance', 70, 38)
# print(lance.adult)

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if rank >= 10:
            self.points = 10
        elif rank == 1:
            self.points = 11
        else:
            self.points = rank

    def __repr__(self):
        d = {11: 'Jack', 12:'Queen', 13:'King', 1:'Ace'}

        if self.rank > 10 or self.rank ==1:
            return f'{d[self.rank]} of {self.suit}'
        return f'{self.rank} of {self.suit}'

hearts_9 = Card('Hearts', 9)

# print(hearts_9)


class Deck:
    def __init__(self, shuffled=False):
        self.stack = []
        self.shuffled = shuffled



class Stack():
    def __init__(self, lst):

        self.length = 0

        for _ in lst:
            self.length += 1

        self.stack = [None] * self.length

        for i in range(self.length):
            self.stack[i] = lst[i]

            if i == self.length -1:
                self.top = lst[i]

    def __len__(self):
        return self.length

    def push(self):

        self.length += 1
        tmp = [None] * self.length

        for i in range(self.length - 1):
            tmp[i] = self.stack[i]

        tmp[-1] = self.top
        return tmp

    def peek(self):
        return self.top


    def pop(self):

        self.length -= 1
        tmp = self.top
        tmp_stack = [None] * self.length

        for i in range(self.length):
            tmp_stack[i] = self.stack[i]

        self.stack = tmp_stack
        self.top = self.stack[-1]

        return tmp

    def empy(self):
        return Stack([])

my_stack = Stack(list(range(10)))
print('length:', my_stack.push())
print('')