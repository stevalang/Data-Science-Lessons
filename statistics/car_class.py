class Car:
  def __init__(self, name, wheelset, color, spoiler_color=None, oversize=False,location=[0, 0]):
    self.wheelset = wheelset
    self.color = color
    self.location = location
    self.spoiler_color = spoiler_color
    self.oversized = False

    if wheelset.count > 4:
      self.oversized = True

  def drive_north(self, distance):
    self.location[0] += int(distance/10)




no_sp_car = Car('Pontiac', 4, 'Red')

sp_car = Car('Ferrari', dope_wheels, 'Red', 'Red')

# print(no_sp_car)
print(sp_car.location)
print(sp_car.drive_north(10))
print(sp_car.location)

print(help(list))

def avg(lst):
    return sum(lst) / len(lst)
self, diameter, width, color, material, count

def __init__(self, diameter, width, color, material, count):

class Wheels:
  def __init__(self, diameter, width, color, material, count):

class Wheelset:
    def __init__(self, diameter, width, color, material, count):
      self.diameter = diameter
      self.width = width
      self.color = color
      self.material = material
      self.count = count


dope_wheels = Wheelset(17, 23, 'silver', 'aluminum', 4)
