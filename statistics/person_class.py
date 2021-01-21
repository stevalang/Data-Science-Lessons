class Person:
  def __init__(self, name, height, age):
    self.name = name
    self.height = height
    self.age = age

    if age >= 21:
      self.adult = True
    else:
      self.adult = False

lance = Person('Lance', 70, 38)
print(lance.adult)