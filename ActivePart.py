import math.pi

class ActivePart:
  def __init__(self, raw_mass, fuel_mass, thrust, specific_impelse, diameter)
    self.raw_mass = raw_mass
    self.fuel_mass = fuel_mass
    self.thrust = thrust
    self.fuel_burned_per_second = thrust / specific_impelse
    self.active_area = math.pi * diameter**2
