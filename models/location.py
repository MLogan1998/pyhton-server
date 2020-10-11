class Location():
    def __init__(self, id, name, city):
      self.id = id
      self.name = name
      self.city = city

    def __repr__(self):
      return f"{self.name} is in {self.city}."
