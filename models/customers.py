class Customer():

    def __init__(self, id, name, money):
      self.id = id
      self.name = name
      self.money = money
    def __repr__(self):
      return f"{self.name} has {self.money} dollars."
